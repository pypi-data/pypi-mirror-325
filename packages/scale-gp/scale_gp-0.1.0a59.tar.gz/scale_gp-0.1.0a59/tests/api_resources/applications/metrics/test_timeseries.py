# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from scale_gp import SGPClient, AsyncSGPClient
from tests.utils import assert_matches_type
from scale_gp.types import TimeseriesData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SGPClient) -> None:
        timesery = client.applications.metrics.timeseries.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        )
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SGPClient) -> None:
        timesery = client.applications.metrics.timeseries.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
            account_id="account_id",
            from_ts=1,
            to_ts=1,
            variants=["string"],
        )
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SGPClient) -> None:
        response = client.applications.metrics.timeseries.with_raw_response.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timesery = response.parse()
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SGPClient) -> None:
        with client.applications.metrics.timeseries.with_streaming_response.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timesery = response.parse()
            assert_matches_type(TimeseriesData, timesery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SGPClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_spec_id` but received ''"):
            client.applications.metrics.timeseries.with_raw_response.retrieve(
                metric_id="total_requests",
                application_spec_id="",
            )


class TestAsyncTimeseries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSGPClient) -> None:
        timesery = await async_client.applications.metrics.timeseries.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        )
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSGPClient) -> None:
        timesery = await async_client.applications.metrics.timeseries.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
            account_id="account_id",
            from_ts=1,
            to_ts=1,
            variants=["string"],
        )
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSGPClient) -> None:
        response = await async_client.applications.metrics.timeseries.with_raw_response.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timesery = await response.parse()
        assert_matches_type(TimeseriesData, timesery, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSGPClient) -> None:
        async with async_client.applications.metrics.timeseries.with_streaming_response.retrieve(
            metric_id="total_requests",
            application_spec_id="application_spec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timesery = await response.parse()
            assert_matches_type(TimeseriesData, timesery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSGPClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_spec_id` but received ''"):
            await async_client.applications.metrics.timeseries.with_raw_response.retrieve(
                metric_id="total_requests",
                application_spec_id="",
            )
