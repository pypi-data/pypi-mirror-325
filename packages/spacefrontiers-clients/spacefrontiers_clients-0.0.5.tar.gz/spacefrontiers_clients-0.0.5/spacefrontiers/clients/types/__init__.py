from datetime import datetime
from typing import Annotated, Any, Literal

from document_storage.types import BaseChunk, SearchDocument
from pydantic import BaseModel, ConfigDict, Field, PlainSerializer

StrBool = Annotated[
    bool, PlainSerializer(lambda x: str(x), return_type=str, when_used="unless-none")
]
ModelName = Literal[
    "deepseek-ai/DeepSeek-V3",
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/llama-3.1-8b-instruct",
    "meta-llama/llama-3.3-70b-versatile",
    "mistralai/mixtral-8x7b-instruct-v0.1",
    "sonnet-3.5",
    "opus-3",
    "haiku-3",
    "qwen/qwen-2.5-72b-instruct",
]


class RetrievedChunk(BaseChunk):
    source: str
    text: str | None = None


class ScoredChunk(BaseModel):
    chunk: RetrievedChunk
    score: float = 0.0
    vector: list[float] | None = None


class ScoredGroup(BaseModel):
    source: str
    document_id: str
    scored_chunks: list[ScoredChunk]


class LlmConfig(BaseModel):
    model_name: ModelName = "meta-llama/llama-3.3-70b-versatile"
    api_key: str | None = None
    max_context_length: int | None = None

    model_config = ConfigDict(protected_namespaces=tuple())


class RagResponse(BaseModel):
    answer: str
    references: list[int]
    text_related_queries: list[dict[str, str]] = Field(default_factory=lambda: [])

    model_config = ConfigDict(protected_namespaces=tuple())


class Range(BaseModel):
    left: int
    right: int


class RerankConfig(BaseModel):
    limit: int = 10
    reranking_limit: int = 25
    score_threshold: float | None = None


class DiversityConfig(BaseModel):
    min_cluster_size: int = 2
    min_samples: int | None = None
    cluster_selection_epsilon: float = 0.0
    alpha: float = 1.0
    cluster_selection_method: str = "leaf"


class TopsRequest(BaseModel):
    limit: int
    offset: int = 0
    days: int = 1


class RecentRequest(BaseModel):
    limit: int


class Query(BaseModel):
    original_query: str | None = None
    reformulated_query: str | None = None
    keywords: list[str] = Field(default_factory=list)
    ids: list[str] = Field(default_factory=list)
    is_recent: bool = False
    date: tuple[datetime, datetime] | None = None
    content_type: str | None = None
    related_queries: list[str] = Field(default_factory=list)
    query_language: str | None = None

    @staticmethod
    def default_query(query: str | None) -> "Query":
        return Query(
            original_query=query,
            reformulated_query=query,
        )


class QueryRouterConfig(BaseModel):
    related_queries: int = 0
    llm_config: LlmConfig | None = None


class QueryClassifierConfig(BaseModel):
    llm_config: LlmConfig | None = None


class L1Request(BaseModel):
    source: str
    limit: int = Field(default=10, ge=0, le=1024 * 16)
    filters: dict[str, list[Any]] = Field(default_factory=dict)


class RecommendRequest(BaseModel):
    positive_ids: list[str] = Field(default_factory=lambda: [])
    l1_request: L1Request
    should_fill_with_abstract: bool = False


class RagConfig(BaseModel):
    llm_config: LlmConfig = Field(default_factory=LlmConfig)
    instruction: str | None = None
    prompt_template_name: str = "default"
    target_language: str | None = None
    translate_api_key: str | None = None
    with_text_related_queries: bool = False
    should_fill_with_abstract: bool = False
    previous_messages: list[dict] = Field(default_factory=lambda: [])


class L2Ranking(BaseModel):
    pass


class PipelineRequest(BaseModel):
    l1_requests: list[L1Request]
    query: str | None = None
    query_router: QueryRouterConfig | None = None
    query_classifier: QueryClassifierConfig | None = None
    l2_ranking: L2Ranking | None = None
    diversity: DiversityConfig | None = None
    rag: RagConfig | None = None
    query_language: str | None = None
    rerank: RerankConfig | None = None


class PipelineResponse(BaseModel):
    search_documents: list[SearchDocument]
    rag_response: RagResponse | None = None
    query: Query | None = None

    @staticmethod
    def empty_response() -> "PipelineResponse":
        return PipelineResponse(
            search_documents=[],
        )
