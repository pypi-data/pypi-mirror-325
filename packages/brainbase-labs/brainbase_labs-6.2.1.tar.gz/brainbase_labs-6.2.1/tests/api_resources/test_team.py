# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from brainbase_labs import BrainbaseLabs, AsyncBrainbaseLabs
from brainbase_labs.types import TeamListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeam:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BrainbaseLabs) -> None:
        team = client.team.list()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: BrainbaseLabs) -> None:
        team = client.team.list(
            include_integrations=True,
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BrainbaseLabs) -> None:
        response = client.team.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BrainbaseLabs) -> None:
        with client.team.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTeam:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBrainbaseLabs) -> None:
        team = await async_client.team.list()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrainbaseLabs) -> None:
        team = await async_client.team.list(
            include_integrations=True,
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrainbaseLabs) -> None:
        response = await async_client.team.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrainbaseLabs) -> None:
        async with async_client.team.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True
