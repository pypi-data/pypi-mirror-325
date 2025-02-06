from pygeai.assistant.clients import AssistantClient
from pygeai.assistant.mappers import AssistantResponseMapper
from pygeai.assistant.responses import AssistantResponse
from pygeai.core.base.clients import BaseClient
from pygeai.core.base.mappers import ErrorMapper, ResponseMapper
from pygeai.core.base.models import ProjectUsageLimit, Project, Assistant, LlmSettings, WelcomeData, TextAssistant, \
    ChatAssistant
from pygeai.core.base.responses import EmptyResponse
from pygeai.organization.clients import OrganizationClient
from pygeai.organization.mappers import OrganizationResponseMapper
from pygeai.organization.responses import AssistantListResponse, ProjectListResponse, ProjectDataResponse, \
    ProjectTokensResponse, ProjectItemListResponse


class Geai(BaseClient):
    """
    Meta-client that operates as an abstraction level over the rest of the clients, designed to handle calls receiving and
    returning objects when appropriate.
    If errors are found in the response, they are processed using `ErrorMapper` to return a list of Errors.
    """

    def get_assistant_list(
            self,
            detail: str = "summary"
    ) -> AssistantListResponse:
        """
        Retrieves a list of assistants with the specified level of detail.

        This method calls `OrganizationClient.get_assistant_list` to fetch assistant data
        and maps the response using `OrganizationResponseMapper` into an `AssistantListResponse` object.

        :param detail: str - The level of detail to include in the response. Possible values:
            - "summary": Provides a summarized list of assistants. (Default)
            - "full": Provides a detailed list of assistants. (Optional)
        :return: AssistantListResponse - The mapped response containing the list of assistants.
        """
        response_data = OrganizationClient().get_assistant_list(detail=detail)
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_assistant_list_response(response_data)
        return result

    def get_project_list(
            self,
            detail: str = "summary",
            name: str = None
    ) -> ProjectListResponse:
        """
        Retrieves a list of projects with the specified level of detail and optional filtering by name.

        This method calls `OrganizationClient.get_project_list` to fetch project data
        and maps the response using `OrganizationResponseMapper` into a `ProjectListResponse` object.

        :param detail: str - The level of detail to include in the response. Possible values:
            - "summary": Provides a summarized list of projects. (Default)
            - "full": Provides a detailed list of projects. (Optional)
        :param name: str, optional - Filters projects by name. If not provided, all projects are returned.
        :return: ProjectListResponse - The mapped response containing the list of projects or an error list.
        """
        response_data = OrganizationClient().get_project_list(
            detail=detail,
            name=name
            )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_project_list_response(response_data)
        return result

    def get_project_data(
            self,
            project_id: str
    ) -> ProjectDataResponse:
        """
        Retrieves detailed data for a specific project.

        This method calls `OrganizationClient.get_project_data` to fetch project details
        and maps the response using `OrganizationResponseMapper` into a `ProjectDataResponse` object.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param project_id: str - The unique identifier of the project to retrieve.
        :return: ProjectDataResponse - The mapped response containing project details or an error list.
        """
        response_data = OrganizationClient().get_project_data(
            project_id=project_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_project_data(response_data)
        return result

    def create_project(
            self,
            project: Project,
            usage_limit: ProjectUsageLimit = None

    ):
        """
        Creates a new project with the given details and optional usage limit settings.

        This method calls `OrganizationClient.create_project` to create a new project and maps the response
        using `OrganizationResponseMapper` into a `ProjectDataResponse` object.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param project: Project - The project object containing details such as name, email, and description.
        :param usage_limit: ProjectUsageLimit, optional - Defines usage limits for the project, including subscription type,
                            unit, soft and hard limits, and renewal status. Defaults to None.
        :return: ProjectDataResponse - The mapped response containing the created project details or an error list.
        """
        response_data = OrganizationClient().create_project(
            name=project.name,
            email=project.email,
            description=project.description,
            usage_limit={
                "subscription_type": usage_limit.subscription_type,
                "usage_unit": usage_limit.usage_unit,
                "soft_limit": usage_limit.soft_limit,
                "hard_limit": usage_limit.hard_limit,
                "renewal_status": usage_limit.renewal_status,
            } if usage_limit else None,
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_project_data(response_data)

        return result

    def update_project(
            self,
            project: Project
    ):
        """
        Updates an existing project with the provided details.

        This method calls `OrganizationClient.update_project` to update project information and maps the response
        using `OrganizationResponseMapper` into a `ProjectDataResponse` object.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param project: Project - The project object containing updated details such as project ID, name, and description.
        :return: ProjectDataResponse - The mapped response containing the updated project details or an error list.
        """
        response_data = OrganizationClient().update_project(
            project_id=project.id,
            name=project.name,
            description=project.description
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_project_data(response_data)

        return result

    def delete_project(
            self,
            project_id: str
    ) -> EmptyResponse:
        """
        Deletes a project by its unique identifier.

        This method calls `OrganizationClient.delete_project` to remove a project and maps the response
        using `ResponseMapper.map_to_empty_response`.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param project_id: str - The unique identifier of the project to be deleted.
        :return: EmptyResponse - An empty response indicating successful deletion or an error list if the request fails.
        """
        response_data = OrganizationClient().delete_project(
            project_id=project_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = ResponseMapper.map_to_empty_response(response_data)

        return result

    def get_project_tokens(
            self,
            project_id: str
    ) -> ProjectTokensResponse:
        """
        Retrieves a list of tokens associated with a specific project.

        This method calls `OrganizationClient.get_project_tokens` to fetch token data and maps the response
        using `OrganizationResponseMapper.map_to_token_list_response`.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param project_id: str - The unique identifier of the project whose tokens are to be retrieved.
        :return: ProjectTokensResponse - The mapped response containing the list of project tokens or an error list.
        """
        response_data = OrganizationClient().get_project_tokens(
            project_id=project_id
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_token_list_response(response_data)

        return result

    def export_request_data(
            self,
            assistant_name: str = None,
            status: str = None,
            skip: int = 0,
            count: int = 0
    ) -> ProjectItemListResponse:
        """
        Exports request data based on specified filters.

        This method calls `OrganizationClient.export_request_data` to retrieve request data
        filtered by assistant name, status, and pagination parameters. The response is mapped
        using `OrganizationResponseMapper.map_to_item_list_response`.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param assistant_name: str, optional - Filters requests by assistant name. If not provided, all assistants are included.
        :param status: str, optional - Filters requests by status. If not provided, all statuses are included.
        :param skip: int, optional - The number of records to skip for pagination. Default is 0.
        :param count: int, optional - The number of records to retrieve. Default is 0 (no limit).
        :return: ProjectItemListResponse - The mapped response containing the exported request data or an error list.
        """
        response_data = OrganizationClient().export_request_data(
            assistant_name=assistant_name,
            status=status,
            skip=skip,
            count=count
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = OrganizationResponseMapper.map_to_item_list_response(response_data)

        return result

    def get_assistant_data(
            self,
            assistant_id: str,
            detail: str = "summary"
    ) -> Assistant:
        """
        Retrieves detailed data for a specific assistant.

        This method calls `AssistantClient.get_assistant_data` to fetch assistant details
        and maps the response using `AssistantResponseMapper.map_to_assistant_list_response`.

        If the response contains errors, they are processed using `ErrorMapper` to return an `ErrorListResponse`.

        :param assistant_id: str - The unique identifier of the assistant to retrieve.
        :param detail: str, optional - The level of detail to include in the response. Possible values:
            - "summary": Provides a summarized response. (Default)
            - "full": Provides detailed assistant data.
        :return: AssistantResponse - The mapped response containing assistant details or an error list.
        """
        response_data = AssistantClient().get_assistant_data(
            assistant_id=assistant_id,
            detail=detail
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = AssistantResponseMapper.map_to_assistant_response(response_data)

        return result

    def create_assistant(
            self,
            assistant: Assistant,
            llm_settings: LlmSettings,
            welcome_data: WelcomeData
    ):
        if isinstance(assistant, TextAssistant):
            return self.create_text_assistant(
                assistant,
                llm_settings,
                welcome_data
            )
        elif isinstance(assistant, ChatAssistant):
            return self.create_chat_assistant(
                assistant,
                llm_settings,
                welcome_data
            )

    def create_text_assistant(
            self,
            assistant: TextAssistant,
            llm_settings: LlmSettings,
            welcome_data: WelcomeData
    ) -> AssistantResponse:
        response_data = AssistantClient().create_assistant(
            assistant_type="text",
            name=assistant.name,
            prompt=assistant.prompt,
            description=assistant.description,
            llm_settings=llm_settings.to_dict(),
            welcome_data=welcome_data.to_dict()
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = AssistantResponseMapper.map_to_assistant_data_response(response_data)

        return result

    def create_chat_assistant(
            self,
            assistant: ChatAssistant,
            llm_settings: LlmSettings,
            welcome_data: WelcomeData
    ) -> AssistantResponse:
        response_data = AssistantClient().create_assistant(
            assistant_type="chat",
            name=assistant.name,
            prompt=assistant.prompt,
            description=assistant.description,
            llm_settings=llm_settings.to_dict(),
            welcome_data=welcome_data.to_dict()
        )
        if "errors" in response_data:
            result = ErrorMapper.map_to_error_list_response(response_data)
        else:
            result = AssistantResponseMapper.map_to_assistant_data_response(response_data)

        return result