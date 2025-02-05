from pygeai.core.base.mappers import ModelMapper
from pygeai.core.base.models import ProjectToken, ProjectSearchProfile, Assistant, Project, ProjectItem
from pygeai.organization.responses import AssistantListResponse, ProjectListResponse, ProjectDataResponse, \
    ProjectTokensResponse, ProjectItemListResponse


class OrganizationResponseMapper:

    @classmethod
    def map_to_assistant_list_response(cls, data: dict) -> AssistantListResponse:
        assistant_list = cls.map_to_assistant_list(data)

        project = ModelMapper.map_to_project(data)

        return AssistantListResponse(
            assistants=assistant_list,
            project=project
        )

    @classmethod
    def map_to_assistant_list(cls, data: dict) -> list[Assistant]:
        assistant_list = list()
        assistants = data.get("assistants")
        if assistants is not None and any(assistants):
            for assistant_data in assistants:
                assistant = ModelMapper.map_to_assistant(assistant_data)
                assistant_list.append(assistant)

        return assistant_list

    @classmethod
    def map_to_project_list_response(cls, data: dict) -> ProjectListResponse:
        project_list = cls.map_to_project_list(data)

        return ProjectListResponse(
            projects=project_list
        )

    @classmethod
    def map_to_project_list(cls, data: dict) -> list[Project]:
        project_list = list()
        projects = data.get("projects")
        if projects is not None and any(projects):
            for project_data in projects:
                project = ModelMapper.map_to_project(project_data)
                project_list.append(project)

        return project_list

    @classmethod
    def map_to_project_data(cls, data: dict) -> ProjectDataResponse:
        organization = ModelMapper.map_to_organization(data)
        project = ModelMapper.map_to_project(data)
        search_profile_list = cls.map_to_search_profile_list(data)
        token_list = cls.map_to_token_list(data)
        usage_limit = ModelMapper.map_to_usage_limit(data)

        return ProjectDataResponse(
            organization=organization,
            project=project,
            search_profiles=search_profile_list,
            tokens=token_list,
            usage_limit=usage_limit
        )

    @classmethod
    def map_to_search_profile_list(cls, data: dict) -> list[ProjectSearchProfile]:
        search_profile_list = list()
        search_profiles = data.get('search_profiles')
        if search_profiles is not None and any(search_profiles):
            for search_profile_data in search_profiles:
                search_profile = ModelMapper.map_to_search_profile(search_profile_data)
                search_profile_list.append(search_profile)

        return search_profile_list

    @classmethod
    def map_to_token_list_response(cls, data: dict) -> ProjectTokensResponse:
        token_list = cls.map_to_token_list(data)

        return ProjectTokensResponse(
            tokens=token_list
        )

    @classmethod
    def map_to_token_list(cls, data: dict) -> list[ProjectToken]:
        token_list = list()
        tokens = data.get('tokens')
        if tokens is not None and any(tokens):
            for token_data in tokens:
                token = ModelMapper.map_to_token(token_data)
                token_list.append(token)

        return token_list

    @classmethod
    def map_to_item_list_response(cls, data: dict) -> ProjectItemListResponse:
        item_list = cls.map_to_item_list(data)

        return ProjectItemListResponse(
            items=item_list
        )

    @classmethod
    def map_to_item_list(cls, data: dict) -> list[ProjectItem]:
        item_list = list()
        items = data.get('items')
        if items is not None and any(items):
            for item_data in items:
                item = ModelMapper.map_to_item(item_data)
                item_list.append(item)

        return item_list
