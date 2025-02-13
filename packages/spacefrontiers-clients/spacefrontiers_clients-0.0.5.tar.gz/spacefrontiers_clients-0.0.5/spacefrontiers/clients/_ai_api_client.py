import asyncio
import json
import typing

import grpc
from izihawa_loglib.request_context import RequestContext

from .protos.service_pb2 import (
    EmbedRequest,
    EmbedResponse,
    RerankRequest,
    RerankResponse,
)
from .protos.service_pb2_grpc import AiStub


class AiApiClient:
    def __init__(
        self,
        endpoint: str = "api.spacefrontiers.org",
        port: int = 81,
        api_key: str = None,
        max_attempts: int = 5,
        initial_backoff_s: float = 0.5,
        max_backoff_s: float = 10,
        backoff_multiplier: int = 2,
    ):
        """Initialize the AI API client with gRPC connection settings.

        Args:
            endpoint: The server endpoint to connect to
            port: The server port number (default: 81)
            api_key: Optional API key for authentication
            max_attempts: Maximum number of retry attempts (default: 5)
            initial_backoff_s: Initial backoff time in seconds (default: 0.5)
            max_backoff_s: Maximum backoff time in seconds (default: 10)
            backoff_multiplier: Multiplier for backoff time between retries (default: 2)
        """
        json_config = json.dumps(
            {
                "methodConfig": [
                    {
                        "name": [{}],
                        "retryPolicy": {
                            "maxAttempts": max_attempts,
                            "initialBackoff": f"{initial_backoff_s}s",
                            "maxBackoff": f"{max_backoff_s}s",
                            "backoffMultiplier": backoff_multiplier,
                            "retryableStatusCodes": ["UNAVAILABLE"],
                        },
                    }
                ]
            }
        )
        self._channel = grpc.aio.insecure_channel(
            f"{endpoint}:{port}",
            options=[
                ("grpc.service_config", json_config),
                ("grpc.lb_policy_name", "round_robin"),
            ],
        )
        self._stub = AiStub(self._channel)
        self._api_key = api_key

    def _prepare_metadata(self, request_context: RequestContext | None = None) -> list[tuple[str, typing.Any]]:
        """Prepare gRPC metadata with optional request context.

        Args:
            request_context: Optional RequestContext object containing request_id and session_id

        Returns:
            List of metadata key-value tuples
        """
        metadata = []
        if request_context:
            if hasattr(request_context, 'request_id'):
                metadata.append(("x-request-id", request_context.request_id))
            if hasattr(request_context, 'session_id'):
                metadata.append(("x-session-id", request_context.session_id))
        if self._api_key is not None:
            metadata.append(("x-sf-api-key", self._api_key))
        return metadata

    async def embed(
        self,
        embed_request: EmbedRequest,
        chunk_size: int = 17,
        request_context: RequestContext | None = None,
    ) -> EmbedResponse:
        """Generate embeddings for a list of texts.

        Args:
            embed_request: EmbedRequest containing texts and task type (one of "classification", "retrieval.passage", "retrieval.query", "separation" or "text-matching")
            chunk_size: Number of texts to process in each batch (default: 17)
            request_context: Optional RequestContext object for request tracking

        Returns:
            EmbedResponse containing embeddings for each text and total token count
        """
        metadata = self._prepare_metadata(request_context)
        splitted_embed_responses = await asyncio.gather(
            *[
                self._stub.embed(
                    EmbedRequest(
                        texts=embed_request.texts[i : i + chunk_size],
                        task=embed_request.task,
                    ),
                    metadata=metadata,
                )
                for i in range(0, len(embed_request.texts), chunk_size)
            ]
        )
        embeddings = []
        processed_tokens = 0
        for splitted_embed_response in splitted_embed_responses:
            embeddings.extend(splitted_embed_response.embeddings)
            processed_tokens += splitted_embed_response.processed_tokens
        return EmbedResponse(
            embeddings=embeddings,
            processed_tokens=processed_tokens,
        )

    async def rerank(
        self,
        rerank_request: RerankRequest,
        chunk_size: int = 17,
        request_context: RequestContext | None = None,
    ) -> RerankResponse:
        """Rerank a list of texts based on their relevance to a query.

        Args:
            rerank_request: RerankRequest containing query and texts to rerank
            chunk_size: Number of texts to process in each batch (default: 17)
            request_context: Optional RequestContext object for request tracking

        Returns:
            RerankResponse containing scores for each text and total token count
        """
        metadata = self._prepare_metadata(request_context)
        splitted_rerank_responses = await asyncio.gather(
            *[
                self._stub.rerank(
                    RerankRequest(
                        query=rerank_request.query,
                        texts=rerank_request.texts[i : i + chunk_size],
                    ),
                    metadata=metadata,
                )
                for i in range(0, len(rerank_request.texts), chunk_size)
            ]
        )
        scores = []
        processed_tokens = 0
        for splitted_rerank_response in splitted_rerank_responses:
            scores.extend(splitted_rerank_response.scores)
            processed_tokens += splitted_rerank_response.processed_tokens
        for i, score in enumerate(scores):
            score.index = i
        return RerankResponse(scores=scores, processed_tokens=processed_tokens)
