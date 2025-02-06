# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...pagination import SyncTopLevelArray, AsyncTopLevelArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.knowledge_bases import async_job_list_params
from ...types.knowledge_bases.async_job_list_response import AsyncJobListResponse

__all__ = ["AsyncJobsResource", "AsyncAsyncJobsResource"]


class AsyncJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    def list(
        self,
        knowledge_base_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        status: Literal["Active", "All", "Pending", "Running", "Completed", "Failed", "Canceled"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncTopLevelArray[AsyncJobListResponse]:
        """
        List Upload Jobs

        Args:
          limit: Maximum number of artifacts to be returned by the given endpoint. Defaults to
              100 and cannot be greater than 10k.

          page: Page number for pagination to be returned by the given endpoint. Starts at page
              1

          status: Optional search by status type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get_api_list(
            f"/v4/knowledge-bases/{knowledge_base_id}/async-jobs",
            page=SyncTopLevelArray[AsyncJobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    async_job_list_params.AsyncJobListParams,
                ),
            ),
            model=AsyncJobListResponse,
        )


class AsyncAsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return AsyncAsyncJobsResourceWithStreamingResponse(self)

    def list(
        self,
        knowledge_base_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        status: Literal["Active", "All", "Pending", "Running", "Completed", "Failed", "Canceled"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AsyncJobListResponse, AsyncTopLevelArray[AsyncJobListResponse]]:
        """
        List Upload Jobs

        Args:
          limit: Maximum number of artifacts to be returned by the given endpoint. Defaults to
              100 and cannot be greater than 10k.

          page: Page number for pagination to be returned by the given endpoint. Starts at page
              1

          status: Optional search by status type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get_api_list(
            f"/v4/knowledge-bases/{knowledge_base_id}/async-jobs",
            page=AsyncTopLevelArray[AsyncJobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    async_job_list_params.AsyncJobListParams,
                ),
            ),
            model=AsyncJobListResponse,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, async_jobs: AsyncJobsResource) -> None:
        self._async_jobs = async_jobs

        self.list = to_raw_response_wrapper(
            async_jobs.list,
        )


class AsyncAsyncJobsResourceWithRawResponse:
    def __init__(self, async_jobs: AsyncAsyncJobsResource) -> None:
        self._async_jobs = async_jobs

        self.list = async_to_raw_response_wrapper(
            async_jobs.list,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, async_jobs: AsyncJobsResource) -> None:
        self._async_jobs = async_jobs

        self.list = to_streamed_response_wrapper(
            async_jobs.list,
        )


class AsyncAsyncJobsResourceWithStreamingResponse:
    def __init__(self, async_jobs: AsyncAsyncJobsResource) -> None:
        self._async_jobs = async_jobs

        self.list = async_to_streamed_response_wrapper(
            async_jobs.list,
        )
