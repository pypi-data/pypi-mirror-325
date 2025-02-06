# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scale_gp import SGPClient, AsyncSGPClient
from tests.utils import assert_matches_type
from scale_gp.types import ChatThread
from scale_gp.pagination import SyncTopLevelArray, AsyncTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SGPClient) -> None:
        chat_thread = client.applications.chat_threads.list(
            "application_variant_id",
        )
        assert_matches_type(SyncTopLevelArray[ChatThread], chat_thread, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SGPClient) -> None:
        response = client.applications.chat_threads.with_raw_response.list(
            "application_variant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_thread = response.parse()
        assert_matches_type(SyncTopLevelArray[ChatThread], chat_thread, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SGPClient) -> None:
        with client.applications.chat_threads.with_streaming_response.list(
            "application_variant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_thread = response.parse()
            assert_matches_type(SyncTopLevelArray[ChatThread], chat_thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: SGPClient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `application_variant_id` but received ''"
        ):
            client.applications.chat_threads.with_raw_response.list(
                "",
            )


class TestAsyncChatThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSGPClient) -> None:
        chat_thread = await async_client.applications.chat_threads.list(
            "application_variant_id",
        )
        assert_matches_type(AsyncTopLevelArray[ChatThread], chat_thread, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSGPClient) -> None:
        response = await async_client.applications.chat_threads.with_raw_response.list(
            "application_variant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_thread = await response.parse()
        assert_matches_type(AsyncTopLevelArray[ChatThread], chat_thread, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSGPClient) -> None:
        async with async_client.applications.chat_threads.with_streaming_response.list(
            "application_variant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_thread = await response.parse()
            assert_matches_type(AsyncTopLevelArray[ChatThread], chat_thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSGPClient) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `application_variant_id` but received ''"
        ):
            await async_client.applications.chat_threads.with_raw_response.list(
                "",
            )
