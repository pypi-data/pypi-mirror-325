# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncChunkPagination, AsyncChunkPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.chunks_response import Chunk
from ...types.knowledge_bases import chunk_list_params

__all__ = ["ChunksResource", "AsyncChunksResource"]


class ChunksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return ChunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return ChunksResourceWithStreamingResponse(self)

    def list(
        self,
        knowledge_base_id: str,
        *,
        chunk_id: str | NotGiven = NOT_GIVEN,
        max_chunks: int | NotGiven = NOT_GIVEN,
        metadata_filters: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncChunkPagination[Chunk]:
        """
        ### Description

        Get chunks from a knowledge base using chunk IDs or a matching metadata field.
        This API will query from the Vector Database using the passed in filters and
        optionally can return the embeddings.

            ### Details
            This API can be used to get a list of chunks from a knowledge base. Given a chunk id,             a metadata field and value, or both, matching chunks are searched for in the knowledge base             given by knowledge base id.

        Args:
          chunk_id: Optional search by chunk_id

          max_chunks: Maximum number of chunks returned by the get_chunks endpoint. Defaults to 10 and
              cannot be greater than 2000.

          metadata_filters: Optional search by metadata fields, encoded as a JSON object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get_api_list(
            f"/v4/knowledge-bases/{knowledge_base_id}/chunks",
            page=SyncChunkPagination[Chunk],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chunk_id": chunk_id,
                        "max_chunks": max_chunks,
                        "metadata_filters": metadata_filters,
                    },
                    chunk_list_params.ChunkListParams,
                ),
            ),
            model=Chunk,
        )


class AsyncChunksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return AsyncChunksResourceWithStreamingResponse(self)

    def list(
        self,
        knowledge_base_id: str,
        *,
        chunk_id: str | NotGiven = NOT_GIVEN,
        max_chunks: int | NotGiven = NOT_GIVEN,
        metadata_filters: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Chunk, AsyncChunkPagination[Chunk]]:
        """
        ### Description

        Get chunks from a knowledge base using chunk IDs or a matching metadata field.
        This API will query from the Vector Database using the passed in filters and
        optionally can return the embeddings.

            ### Details
            This API can be used to get a list of chunks from a knowledge base. Given a chunk id,             a metadata field and value, or both, matching chunks are searched for in the knowledge base             given by knowledge base id.

        Args:
          chunk_id: Optional search by chunk_id

          max_chunks: Maximum number of chunks returned by the get_chunks endpoint. Defaults to 10 and
              cannot be greater than 2000.

          metadata_filters: Optional search by metadata fields, encoded as a JSON object

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get_api_list(
            f"/v4/knowledge-bases/{knowledge_base_id}/chunks",
            page=AsyncChunkPagination[Chunk],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chunk_id": chunk_id,
                        "max_chunks": max_chunks,
                        "metadata_filters": metadata_filters,
                    },
                    chunk_list_params.ChunkListParams,
                ),
            ),
            model=Chunk,
        )


class ChunksResourceWithRawResponse:
    def __init__(self, chunks: ChunksResource) -> None:
        self._chunks = chunks

        self.list = to_raw_response_wrapper(
            chunks.list,
        )


class AsyncChunksResourceWithRawResponse:
    def __init__(self, chunks: AsyncChunksResource) -> None:
        self._chunks = chunks

        self.list = async_to_raw_response_wrapper(
            chunks.list,
        )


class ChunksResourceWithStreamingResponse:
    def __init__(self, chunks: ChunksResource) -> None:
        self._chunks = chunks

        self.list = to_streamed_response_wrapper(
            chunks.list,
        )


class AsyncChunksResourceWithStreamingResponse:
    def __init__(self, chunks: AsyncChunksResource) -> None:
        self._chunks = chunks

        self.list = async_to_streamed_response_wrapper(
            chunks.list,
        )
