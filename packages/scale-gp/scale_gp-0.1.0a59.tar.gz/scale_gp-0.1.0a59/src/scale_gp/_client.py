# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    alias,
    users,
    agents,
    chunks,
    themes,
    accounts,
    questions,
    completions,
    interactions,
    question_sets,
    model_templates,
    studio_projects,
    chat_completions,
    application_specs,
    evaluation_configs,
    application_schemas,
    application_threads,
    deployment_packages,
    application_variants,
    application_deployments,
    application_variant_reports,
    knowledge_base_data_sources,
    application_test_case_outputs,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, SGPClientError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.beta import beta
from .resources.models import models
from .resources.evaluations import evaluations
from .resources.applications import applications
from .resources.chat_threads import chat_threads
from .resources.model_groups import model_groups
from .resources.model_servers import model_servers
from .resources.knowledge_bases import knowledge_bases
from .resources.fine_tuning_jobs import fine_tuning_jobs
from .resources.training_datasets import training_datasets
from .resources.evaluation_datasets import evaluation_datasets

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "SGPClient",
    "AsyncSGPClient",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.egp.scale.com",
    "development": "http://127.0.0.1:5003/public",
}


class SGPClient(SyncAPIClient):
    knowledge_bases: knowledge_bases.KnowledgeBasesResource
    knowledge_base_data_sources: knowledge_base_data_sources.KnowledgeBaseDataSourcesResource
    chunks: chunks.ChunksResource
    agents: agents.AgentsResource
    completions: completions.CompletionsResource
    chat_completions: chat_completions.ChatCompletionsResource
    models: models.ModelsResource
    model_groups: model_groups.ModelGroupsResource
    users: users.UsersResource
    accounts: accounts.AccountsResource
    question_sets: question_sets.QuestionSetsResource
    evaluations: evaluations.EvaluationsResource
    evaluation_configs: evaluation_configs.EvaluationConfigsResource
    evaluation_datasets: evaluation_datasets.EvaluationDatasetsResource
    studio_projects: studio_projects.StudioProjectsResource
    application_specs: application_specs.ApplicationSpecsResource
    questions: questions.QuestionsResource
    model_templates: model_templates.ModelTemplatesResource
    fine_tuning_jobs: fine_tuning_jobs.FineTuningJobsResource
    training_datasets: training_datasets.TrainingDatasetsResource
    deployment_packages: deployment_packages.DeploymentPackagesResource
    application_variants: application_variants.ApplicationVariantsResource
    application_deployments: application_deployments.ApplicationDeploymentsResource
    application_variant_reports: application_variant_reports.ApplicationVariantReportsResource
    application_test_case_outputs: application_test_case_outputs.ApplicationTestCaseOutputsResource
    application_schemas: application_schemas.ApplicationSchemasResource
    interactions: interactions.InteractionsResource
    applications: applications.ApplicationsResource
    application_threads: application_threads.ApplicationThreadsResource
    chat_threads: chat_threads.ChatThreadsResource
    themes: themes.ThemesResource
    beta: beta.BetaResource
    model_servers: model_servers.ModelServersResource
    alias: alias.AliasResource
    with_raw_response: SGPClientWithRawResponse
    with_streaming_response: SGPClientWithStreamedResponse

    # client options
    api_key: str
    account_id: str | None

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        account_id: str | None = None,
        environment: Literal["production", "development"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SGPClient client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SGP_API_KEY`
        - `account_id` from `SGP_ACCOUNT_ID`
        """
        if api_key is None:
            api_key = os.environ.get("SGP_API_KEY")
        if api_key is None:
            raise SGPClientError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SGP_API_KEY environment variable"
            )
        self.api_key = api_key

        if account_id is None:
            account_id = os.environ.get("SGP_ACCOUNT_ID")
        self.account_id = account_id

        self._environment = environment

        base_url_env = os.environ.get("SGP_CLIENT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SGP_CLIENT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.knowledge_bases = knowledge_bases.KnowledgeBasesResource(self)
        self.knowledge_base_data_sources = knowledge_base_data_sources.KnowledgeBaseDataSourcesResource(self)
        self.chunks = chunks.ChunksResource(self)
        self.agents = agents.AgentsResource(self)
        self.completions = completions.CompletionsResource(self)
        self.chat_completions = chat_completions.ChatCompletionsResource(self)
        self.models = models.ModelsResource(self)
        self.model_groups = model_groups.ModelGroupsResource(self)
        self.users = users.UsersResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.question_sets = question_sets.QuestionSetsResource(self)
        self.evaluations = evaluations.EvaluationsResource(self)
        self.evaluation_configs = evaluation_configs.EvaluationConfigsResource(self)
        self.evaluation_datasets = evaluation_datasets.EvaluationDatasetsResource(self)
        self.studio_projects = studio_projects.StudioProjectsResource(self)
        self.application_specs = application_specs.ApplicationSpecsResource(self)
        self.questions = questions.QuestionsResource(self)
        self.model_templates = model_templates.ModelTemplatesResource(self)
        self.fine_tuning_jobs = fine_tuning_jobs.FineTuningJobsResource(self)
        self.training_datasets = training_datasets.TrainingDatasetsResource(self)
        self.deployment_packages = deployment_packages.DeploymentPackagesResource(self)
        self.application_variants = application_variants.ApplicationVariantsResource(self)
        self.application_deployments = application_deployments.ApplicationDeploymentsResource(self)
        self.application_variant_reports = application_variant_reports.ApplicationVariantReportsResource(self)
        self.application_test_case_outputs = application_test_case_outputs.ApplicationTestCaseOutputsResource(self)
        self.application_schemas = application_schemas.ApplicationSchemasResource(self)
        self.interactions = interactions.InteractionsResource(self)
        self.applications = applications.ApplicationsResource(self)
        self.application_threads = application_threads.ApplicationThreadsResource(self)
        self.chat_threads = chat_threads.ChatThreadsResource(self)
        self.themes = themes.ThemesResource(self)
        self.beta = beta.BetaResource(self)
        self.model_servers = model_servers.ModelServersResource(self)
        self.alias = alias.AliasResource(self)
        self.with_raw_response = SGPClientWithRawResponse(self)
        self.with_streaming_response = SGPClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "x-selected-account-id": self.account_id if self.account_id is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        account_id: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            account_id=account_id or self.account_id,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSGPClient(AsyncAPIClient):
    knowledge_bases: knowledge_bases.AsyncKnowledgeBasesResource
    knowledge_base_data_sources: knowledge_base_data_sources.AsyncKnowledgeBaseDataSourcesResource
    chunks: chunks.AsyncChunksResource
    agents: agents.AsyncAgentsResource
    completions: completions.AsyncCompletionsResource
    chat_completions: chat_completions.AsyncChatCompletionsResource
    models: models.AsyncModelsResource
    model_groups: model_groups.AsyncModelGroupsResource
    users: users.AsyncUsersResource
    accounts: accounts.AsyncAccountsResource
    question_sets: question_sets.AsyncQuestionSetsResource
    evaluations: evaluations.AsyncEvaluationsResource
    evaluation_configs: evaluation_configs.AsyncEvaluationConfigsResource
    evaluation_datasets: evaluation_datasets.AsyncEvaluationDatasetsResource
    studio_projects: studio_projects.AsyncStudioProjectsResource
    application_specs: application_specs.AsyncApplicationSpecsResource
    questions: questions.AsyncQuestionsResource
    model_templates: model_templates.AsyncModelTemplatesResource
    fine_tuning_jobs: fine_tuning_jobs.AsyncFineTuningJobsResource
    training_datasets: training_datasets.AsyncTrainingDatasetsResource
    deployment_packages: deployment_packages.AsyncDeploymentPackagesResource
    application_variants: application_variants.AsyncApplicationVariantsResource
    application_deployments: application_deployments.AsyncApplicationDeploymentsResource
    application_variant_reports: application_variant_reports.AsyncApplicationVariantReportsResource
    application_test_case_outputs: application_test_case_outputs.AsyncApplicationTestCaseOutputsResource
    application_schemas: application_schemas.AsyncApplicationSchemasResource
    interactions: interactions.AsyncInteractionsResource
    applications: applications.AsyncApplicationsResource
    application_threads: application_threads.AsyncApplicationThreadsResource
    chat_threads: chat_threads.AsyncChatThreadsResource
    themes: themes.AsyncThemesResource
    beta: beta.AsyncBetaResource
    model_servers: model_servers.AsyncModelServersResource
    alias: alias.AsyncAliasResource
    with_raw_response: AsyncSGPClientWithRawResponse
    with_streaming_response: AsyncSGPClientWithStreamedResponse

    # client options
    api_key: str
    account_id: str | None

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        account_id: str | None = None,
        environment: Literal["production", "development"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async SGPClient client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SGP_API_KEY`
        - `account_id` from `SGP_ACCOUNT_ID`
        """
        if api_key is None:
            api_key = os.environ.get("SGP_API_KEY")
        if api_key is None:
            raise SGPClientError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SGP_API_KEY environment variable"
            )
        self.api_key = api_key

        if account_id is None:
            account_id = os.environ.get("SGP_ACCOUNT_ID")
        self.account_id = account_id

        self._environment = environment

        base_url_env = os.environ.get("SGP_CLIENT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SGP_CLIENT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResource(self)
        self.knowledge_base_data_sources = knowledge_base_data_sources.AsyncKnowledgeBaseDataSourcesResource(self)
        self.chunks = chunks.AsyncChunksResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.completions = completions.AsyncCompletionsResource(self)
        self.chat_completions = chat_completions.AsyncChatCompletionsResource(self)
        self.models = models.AsyncModelsResource(self)
        self.model_groups = model_groups.AsyncModelGroupsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.question_sets = question_sets.AsyncQuestionSetsResource(self)
        self.evaluations = evaluations.AsyncEvaluationsResource(self)
        self.evaluation_configs = evaluation_configs.AsyncEvaluationConfigsResource(self)
        self.evaluation_datasets = evaluation_datasets.AsyncEvaluationDatasetsResource(self)
        self.studio_projects = studio_projects.AsyncStudioProjectsResource(self)
        self.application_specs = application_specs.AsyncApplicationSpecsResource(self)
        self.questions = questions.AsyncQuestionsResource(self)
        self.model_templates = model_templates.AsyncModelTemplatesResource(self)
        self.fine_tuning_jobs = fine_tuning_jobs.AsyncFineTuningJobsResource(self)
        self.training_datasets = training_datasets.AsyncTrainingDatasetsResource(self)
        self.deployment_packages = deployment_packages.AsyncDeploymentPackagesResource(self)
        self.application_variants = application_variants.AsyncApplicationVariantsResource(self)
        self.application_deployments = application_deployments.AsyncApplicationDeploymentsResource(self)
        self.application_variant_reports = application_variant_reports.AsyncApplicationVariantReportsResource(self)
        self.application_test_case_outputs = application_test_case_outputs.AsyncApplicationTestCaseOutputsResource(self)
        self.application_schemas = application_schemas.AsyncApplicationSchemasResource(self)
        self.interactions = interactions.AsyncInteractionsResource(self)
        self.applications = applications.AsyncApplicationsResource(self)
        self.application_threads = application_threads.AsyncApplicationThreadsResource(self)
        self.chat_threads = chat_threads.AsyncChatThreadsResource(self)
        self.themes = themes.AsyncThemesResource(self)
        self.beta = beta.AsyncBetaResource(self)
        self.model_servers = model_servers.AsyncModelServersResource(self)
        self.alias = alias.AsyncAliasResource(self)
        self.with_raw_response = AsyncSGPClientWithRawResponse(self)
        self.with_streaming_response = AsyncSGPClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "x-selected-account-id": self.account_id if self.account_id is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        account_id: str | None = None,
        environment: Literal["production", "development"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            account_id=account_id or self.account_id,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SGPClientWithRawResponse:
    def __init__(self, client: SGPClient) -> None:
        self.knowledge_bases = knowledge_bases.KnowledgeBasesResourceWithRawResponse(client.knowledge_bases)
        self.knowledge_base_data_sources = knowledge_base_data_sources.KnowledgeBaseDataSourcesResourceWithRawResponse(
            client.knowledge_base_data_sources
        )
        self.chunks = chunks.ChunksResourceWithRawResponse(client.chunks)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.completions = completions.CompletionsResourceWithRawResponse(client.completions)
        self.chat_completions = chat_completions.ChatCompletionsResourceWithRawResponse(client.chat_completions)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.model_groups = model_groups.ModelGroupsResourceWithRawResponse(client.model_groups)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.question_sets = question_sets.QuestionSetsResourceWithRawResponse(client.question_sets)
        self.evaluations = evaluations.EvaluationsResourceWithRawResponse(client.evaluations)
        self.evaluation_configs = evaluation_configs.EvaluationConfigsResourceWithRawResponse(client.evaluation_configs)
        self.evaluation_datasets = evaluation_datasets.EvaluationDatasetsResourceWithRawResponse(
            client.evaluation_datasets
        )
        self.studio_projects = studio_projects.StudioProjectsResourceWithRawResponse(client.studio_projects)
        self.application_specs = application_specs.ApplicationSpecsResourceWithRawResponse(client.application_specs)
        self.questions = questions.QuestionsResourceWithRawResponse(client.questions)
        self.model_templates = model_templates.ModelTemplatesResourceWithRawResponse(client.model_templates)
        self.fine_tuning_jobs = fine_tuning_jobs.FineTuningJobsResourceWithRawResponse(client.fine_tuning_jobs)
        self.training_datasets = training_datasets.TrainingDatasetsResourceWithRawResponse(client.training_datasets)
        self.deployment_packages = deployment_packages.DeploymentPackagesResourceWithRawResponse(
            client.deployment_packages
        )
        self.application_variants = application_variants.ApplicationVariantsResourceWithRawResponse(
            client.application_variants
        )
        self.application_deployments = application_deployments.ApplicationDeploymentsResourceWithRawResponse(
            client.application_deployments
        )
        self.application_variant_reports = application_variant_reports.ApplicationVariantReportsResourceWithRawResponse(
            client.application_variant_reports
        )
        self.application_test_case_outputs = (
            application_test_case_outputs.ApplicationTestCaseOutputsResourceWithRawResponse(
                client.application_test_case_outputs
            )
        )
        self.application_schemas = application_schemas.ApplicationSchemasResourceWithRawResponse(
            client.application_schemas
        )
        self.interactions = interactions.InteractionsResourceWithRawResponse(client.interactions)
        self.applications = applications.ApplicationsResourceWithRawResponse(client.applications)
        self.application_threads = application_threads.ApplicationThreadsResourceWithRawResponse(
            client.application_threads
        )
        self.chat_threads = chat_threads.ChatThreadsResourceWithRawResponse(client.chat_threads)
        self.themes = themes.ThemesResourceWithRawResponse(client.themes)
        self.beta = beta.BetaResourceWithRawResponse(client.beta)
        self.model_servers = model_servers.ModelServersResourceWithRawResponse(client.model_servers)
        self.alias = alias.AliasResourceWithRawResponse(client.alias)


class AsyncSGPClientWithRawResponse:
    def __init__(self, client: AsyncSGPClient) -> None:
        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse(client.knowledge_bases)
        self.knowledge_base_data_sources = (
            knowledge_base_data_sources.AsyncKnowledgeBaseDataSourcesResourceWithRawResponse(
                client.knowledge_base_data_sources
            )
        )
        self.chunks = chunks.AsyncChunksResourceWithRawResponse(client.chunks)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.completions = completions.AsyncCompletionsResourceWithRawResponse(client.completions)
        self.chat_completions = chat_completions.AsyncChatCompletionsResourceWithRawResponse(client.chat_completions)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.model_groups = model_groups.AsyncModelGroupsResourceWithRawResponse(client.model_groups)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.question_sets = question_sets.AsyncQuestionSetsResourceWithRawResponse(client.question_sets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithRawResponse(client.evaluations)
        self.evaluation_configs = evaluation_configs.AsyncEvaluationConfigsResourceWithRawResponse(
            client.evaluation_configs
        )
        self.evaluation_datasets = evaluation_datasets.AsyncEvaluationDatasetsResourceWithRawResponse(
            client.evaluation_datasets
        )
        self.studio_projects = studio_projects.AsyncStudioProjectsResourceWithRawResponse(client.studio_projects)
        self.application_specs = application_specs.AsyncApplicationSpecsResourceWithRawResponse(
            client.application_specs
        )
        self.questions = questions.AsyncQuestionsResourceWithRawResponse(client.questions)
        self.model_templates = model_templates.AsyncModelTemplatesResourceWithRawResponse(client.model_templates)
        self.fine_tuning_jobs = fine_tuning_jobs.AsyncFineTuningJobsResourceWithRawResponse(client.fine_tuning_jobs)
        self.training_datasets = training_datasets.AsyncTrainingDatasetsResourceWithRawResponse(
            client.training_datasets
        )
        self.deployment_packages = deployment_packages.AsyncDeploymentPackagesResourceWithRawResponse(
            client.deployment_packages
        )
        self.application_variants = application_variants.AsyncApplicationVariantsResourceWithRawResponse(
            client.application_variants
        )
        self.application_deployments = application_deployments.AsyncApplicationDeploymentsResourceWithRawResponse(
            client.application_deployments
        )
        self.application_variant_reports = (
            application_variant_reports.AsyncApplicationVariantReportsResourceWithRawResponse(
                client.application_variant_reports
            )
        )
        self.application_test_case_outputs = (
            application_test_case_outputs.AsyncApplicationTestCaseOutputsResourceWithRawResponse(
                client.application_test_case_outputs
            )
        )
        self.application_schemas = application_schemas.AsyncApplicationSchemasResourceWithRawResponse(
            client.application_schemas
        )
        self.interactions = interactions.AsyncInteractionsResourceWithRawResponse(client.interactions)
        self.applications = applications.AsyncApplicationsResourceWithRawResponse(client.applications)
        self.application_threads = application_threads.AsyncApplicationThreadsResourceWithRawResponse(
            client.application_threads
        )
        self.chat_threads = chat_threads.AsyncChatThreadsResourceWithRawResponse(client.chat_threads)
        self.themes = themes.AsyncThemesResourceWithRawResponse(client.themes)
        self.beta = beta.AsyncBetaResourceWithRawResponse(client.beta)
        self.model_servers = model_servers.AsyncModelServersResourceWithRawResponse(client.model_servers)
        self.alias = alias.AsyncAliasResourceWithRawResponse(client.alias)


class SGPClientWithStreamedResponse:
    def __init__(self, client: SGPClient) -> None:
        self.knowledge_bases = knowledge_bases.KnowledgeBasesResourceWithStreamingResponse(client.knowledge_bases)
        self.knowledge_base_data_sources = (
            knowledge_base_data_sources.KnowledgeBaseDataSourcesResourceWithStreamingResponse(
                client.knowledge_base_data_sources
            )
        )
        self.chunks = chunks.ChunksResourceWithStreamingResponse(client.chunks)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.completions = completions.CompletionsResourceWithStreamingResponse(client.completions)
        self.chat_completions = chat_completions.ChatCompletionsResourceWithStreamingResponse(client.chat_completions)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.model_groups = model_groups.ModelGroupsResourceWithStreamingResponse(client.model_groups)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.question_sets = question_sets.QuestionSetsResourceWithStreamingResponse(client.question_sets)
        self.evaluations = evaluations.EvaluationsResourceWithStreamingResponse(client.evaluations)
        self.evaluation_configs = evaluation_configs.EvaluationConfigsResourceWithStreamingResponse(
            client.evaluation_configs
        )
        self.evaluation_datasets = evaluation_datasets.EvaluationDatasetsResourceWithStreamingResponse(
            client.evaluation_datasets
        )
        self.studio_projects = studio_projects.StudioProjectsResourceWithStreamingResponse(client.studio_projects)
        self.application_specs = application_specs.ApplicationSpecsResourceWithStreamingResponse(
            client.application_specs
        )
        self.questions = questions.QuestionsResourceWithStreamingResponse(client.questions)
        self.model_templates = model_templates.ModelTemplatesResourceWithStreamingResponse(client.model_templates)
        self.fine_tuning_jobs = fine_tuning_jobs.FineTuningJobsResourceWithStreamingResponse(client.fine_tuning_jobs)
        self.training_datasets = training_datasets.TrainingDatasetsResourceWithStreamingResponse(
            client.training_datasets
        )
        self.deployment_packages = deployment_packages.DeploymentPackagesResourceWithStreamingResponse(
            client.deployment_packages
        )
        self.application_variants = application_variants.ApplicationVariantsResourceWithStreamingResponse(
            client.application_variants
        )
        self.application_deployments = application_deployments.ApplicationDeploymentsResourceWithStreamingResponse(
            client.application_deployments
        )
        self.application_variant_reports = (
            application_variant_reports.ApplicationVariantReportsResourceWithStreamingResponse(
                client.application_variant_reports
            )
        )
        self.application_test_case_outputs = (
            application_test_case_outputs.ApplicationTestCaseOutputsResourceWithStreamingResponse(
                client.application_test_case_outputs
            )
        )
        self.application_schemas = application_schemas.ApplicationSchemasResourceWithStreamingResponse(
            client.application_schemas
        )
        self.interactions = interactions.InteractionsResourceWithStreamingResponse(client.interactions)
        self.applications = applications.ApplicationsResourceWithStreamingResponse(client.applications)
        self.application_threads = application_threads.ApplicationThreadsResourceWithStreamingResponse(
            client.application_threads
        )
        self.chat_threads = chat_threads.ChatThreadsResourceWithStreamingResponse(client.chat_threads)
        self.themes = themes.ThemesResourceWithStreamingResponse(client.themes)
        self.beta = beta.BetaResourceWithStreamingResponse(client.beta)
        self.model_servers = model_servers.ModelServersResourceWithStreamingResponse(client.model_servers)
        self.alias = alias.AliasResourceWithStreamingResponse(client.alias)


class AsyncSGPClientWithStreamedResponse:
    def __init__(self, client: AsyncSGPClient) -> None:
        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse(client.knowledge_bases)
        self.knowledge_base_data_sources = (
            knowledge_base_data_sources.AsyncKnowledgeBaseDataSourcesResourceWithStreamingResponse(
                client.knowledge_base_data_sources
            )
        )
        self.chunks = chunks.AsyncChunksResourceWithStreamingResponse(client.chunks)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.completions = completions.AsyncCompletionsResourceWithStreamingResponse(client.completions)
        self.chat_completions = chat_completions.AsyncChatCompletionsResourceWithStreamingResponse(
            client.chat_completions
        )
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.model_groups = model_groups.AsyncModelGroupsResourceWithStreamingResponse(client.model_groups)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.question_sets = question_sets.AsyncQuestionSetsResourceWithStreamingResponse(client.question_sets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)
        self.evaluation_configs = evaluation_configs.AsyncEvaluationConfigsResourceWithStreamingResponse(
            client.evaluation_configs
        )
        self.evaluation_datasets = evaluation_datasets.AsyncEvaluationDatasetsResourceWithStreamingResponse(
            client.evaluation_datasets
        )
        self.studio_projects = studio_projects.AsyncStudioProjectsResourceWithStreamingResponse(client.studio_projects)
        self.application_specs = application_specs.AsyncApplicationSpecsResourceWithStreamingResponse(
            client.application_specs
        )
        self.questions = questions.AsyncQuestionsResourceWithStreamingResponse(client.questions)
        self.model_templates = model_templates.AsyncModelTemplatesResourceWithStreamingResponse(client.model_templates)
        self.fine_tuning_jobs = fine_tuning_jobs.AsyncFineTuningJobsResourceWithStreamingResponse(
            client.fine_tuning_jobs
        )
        self.training_datasets = training_datasets.AsyncTrainingDatasetsResourceWithStreamingResponse(
            client.training_datasets
        )
        self.deployment_packages = deployment_packages.AsyncDeploymentPackagesResourceWithStreamingResponse(
            client.deployment_packages
        )
        self.application_variants = application_variants.AsyncApplicationVariantsResourceWithStreamingResponse(
            client.application_variants
        )
        self.application_deployments = application_deployments.AsyncApplicationDeploymentsResourceWithStreamingResponse(
            client.application_deployments
        )
        self.application_variant_reports = (
            application_variant_reports.AsyncApplicationVariantReportsResourceWithStreamingResponse(
                client.application_variant_reports
            )
        )
        self.application_test_case_outputs = (
            application_test_case_outputs.AsyncApplicationTestCaseOutputsResourceWithStreamingResponse(
                client.application_test_case_outputs
            )
        )
        self.application_schemas = application_schemas.AsyncApplicationSchemasResourceWithStreamingResponse(
            client.application_schemas
        )
        self.interactions = interactions.AsyncInteractionsResourceWithStreamingResponse(client.interactions)
        self.applications = applications.AsyncApplicationsResourceWithStreamingResponse(client.applications)
        self.application_threads = application_threads.AsyncApplicationThreadsResourceWithStreamingResponse(
            client.application_threads
        )
        self.chat_threads = chat_threads.AsyncChatThreadsResourceWithStreamingResponse(client.chat_threads)
        self.themes = themes.AsyncThemesResourceWithStreamingResponse(client.themes)
        self.beta = beta.AsyncBetaResourceWithStreamingResponse(client.beta)
        self.model_servers = model_servers.AsyncModelServersResourceWithStreamingResponse(client.model_servers)
        self.alias = alias.AsyncAliasResourceWithStreamingResponse(client.alias)


Client = SGPClient

AsyncClient = AsyncSGPClient
