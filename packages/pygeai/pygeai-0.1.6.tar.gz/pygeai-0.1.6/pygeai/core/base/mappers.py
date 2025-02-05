from pygeai.core.base.models import Organization, Assistant, AssistantIntent, AssistantRevision, \
    AssistantRevisionMetadata, Project, Error, ProjectUsageLimit, ProjectSearchProfile, ProjectToken, ProjectItem
from pygeai.core.base.responses import ErrorListResponse, EmptyResponse


class ErrorMapper:
    """
    A utility class for mapping error-related data structures.

    This class provides methods to convert raw error data from API responses into structured
    `Error` objects, `ErrorListResponse`, or a list of `Error` objects.
    """
    @classmethod
    def map_to_error(cls, data: dict) -> Error:
        """
        Maps a single error dictionary to an `Error` object.

        :param data: dict - The dictionary containing error details.
        :return: Error - An `Error` object with extracted error details.
        """
        return Error(
            error_id=data.get('id'),
            description=data.get('description')
        )

    @classmethod
    def map_to_error_list_response(cls, data: dict) -> ErrorListResponse:
        """
       Maps an API response dictionary to an `ErrorListResponse` object.

       This method extracts errors from the given data, converts them into a list of `Error` objects,
       and returns an `ErrorListResponse` containing the list.

       :param data: dict - The dictionary containing error response data.
       :return: ErrorListResponse - A structured response containing a list of errors.
       """
        error_list = cls.map_to_error_list(data)

        return ErrorListResponse(
            errors=error_list
        )

    @classmethod
    def map_to_error_list(cls, data: dict) -> list[Error]:
        """
        Extracts and maps a list of errors from an API response dictionary.

        This method iterates through the `errors` field in the given data and converts
        each error entry into an `Error` object.

        :param data: dict - The dictionary containing error response data.
        :return: list[Error] - A list of `Error` objects.
        """
        error_list = list()
        errors = data.get('errors')
        if errors is not None and any(errors):
            for error_data in errors:
                error = cls.map_to_error(error_data)
                error_list.append(error)

        return error_list


class ResponseMapper:

    @classmethod
    def map_to_empty_response(cls, data: dict) -> EmptyResponse:
        return EmptyResponse(
            content=data
        )


class ModelMapper:

    @classmethod
    def map_to_organization(cls, data: dict) -> Organization:
        """
        Maps a dictionary to an `Organization` object.

        :param data: dict - The dictionary containing organization details.
        :return: Organization - The mapped `Organization` object.
        """
        return Organization(
            organization_id=data.get('organizationId'),
            organization_name=data.get('organizationName')
        )

    @classmethod
    def map_to_assistant(cls, data: dict) -> Assistant:
        """
        Maps a dictionary to an `Assistant` object, including associated intents.

        :param data: dict - The dictionary containing assistant details.
        :return: Assistant - The mapped `Assistant` object.
        """
        intent_list = cls.map_to_intent_list(data)

        return Assistant(
            assistant_id=data.get("assistantId"),
            assistant_name=data.get("assistantName"),
            assistant_type=data.get("assistantType"),
            intents=intent_list
        )

    @classmethod
    def map_to_intent_list(cls, data: dict) -> list[AssistantIntent]:
        """
        Maps a list of intent dictionaries to `AssistantIntent` objects.

        :param data: dict - The dictionary containing the list of intents.
        :return: list[AssistantIntent] - A list of mapped `AssistantIntent` objects.
        """
        intent_list = list()
        intents = data.get('intents')
        if intents is not None and any(intents):
            for intent_data in intents:
                intent = cls.map_to_intent(intent_data)
                intent_list.append(intent)

        return intent_list

    @classmethod
    def map_to_intent(cls, data: dict) -> AssistantIntent:
        """
        Maps a dictionary to an `AssistantIntent` object, including revisions.

        :param data: dict - The dictionary containing intent details.
        :return: AssistantIntent - The mapped `AssistantIntent` object.
        """
        revision_list = cls.map_to_revision_list(data)

        return AssistantIntent(
            assistant_intent_default_revision=data.get("assistantIntentDefaultRevision"),
            assistant_intent_description=data.get("assistantIntentDescription"),
            assistant_intent_id=data.get("assistantIntentId"),
            assistant_intent_name=data.get("assistantIntentName"),
            revisions=revision_list,
        )

    @classmethod
    def map_to_revision_list(cls, data: dict) -> list[AssistantRevision]:
        """
        Maps a list of revision dictionaries to `AssistantRevision` objects.

        :param data: dict - The dictionary containing the list of revisions.
        :return: list[AssistantRevision] - A list of mapped `AssistantRevision` objects.
        """
        revision_list = list()
        revisions = data.get("revisions")
        if revisions is not None and any(revisions):
            for revision_data in revisions:
                revision = cls.map_to_revision(revision_data)
                revision_list.append(revision)

        return revision_list

    @classmethod
    def map_to_revision(cls, data: dict) -> AssistantRevision:
        """
        Maps a dictionary to an `AssistantRevision` object, including metadata.

        :param data: dict - The dictionary containing revision details.
        :return: AssistantRevision - The mapped `AssistantRevision` object.
        """
        metadata_list = cls.map_to_metadata_list(data)

        return AssistantRevision(
            metadata=metadata_list,
            model_id=data.get("modelId"),
            model_name=data.get("modelName"),
            prompt=data.get("prompt"),
            provider_name=data.get("providerName"),
            revision_description=data.get("revisionDescription"),
            revision_id=data.get("revisionId"),
            revision_name=data.get("revisionName"),
            timestamp=data.get("timestamp"),
        )

    @classmethod
    def map_to_metadata_list(cls, data: dict) -> list[AssistantRevisionMetadata]:
        """
       Maps a list of metadata dictionaries to `AssistantRevisionMetadata` objects.

       :param data: dict - The dictionary containing metadata information.
       :return: list[AssistantRevisionMetadata] - A list of mapped `AssistantRevisionMetadata` objects.
       """
        metadata_list = list()
        metadata = data.get('metadata')
        if metadata is not None and any(metadata):
            for metadata_data in metadata:
                metadata = cls.map_to_metadata(metadata_data)
                metadata_list.append(metadata)

        return metadata_list

    @classmethod
    def map_to_metadata(cls, data: dict) -> AssistantRevisionMetadata:
        """
       Maps a dictionary to an `AssistantRevisionMetadata` object.

       :param data: dict - The dictionary containing metadata details.
       :return: AssistantRevisionMetadata - The mapped `AssistantRevisionMetadata` object.
       """
        return AssistantRevisionMetadata(
            key=data.get("key"),
            type=data.get("type"),
            value=data.get("value")
        )

    @classmethod
    def map_to_project(cls, data: dict) -> Project:
        """
        Maps a dictionary to a `Project` object.

        :param data: dict - The dictionary containing project details.
        :return: Project - The mapped `Project` object.
        """

        return Project(
            project_id=data.get('projectId'),
            project_name=data.get('projectName')
        )

    @classmethod
    def map_to_search_profile(cls, data: dict) -> ProjectSearchProfile:
        """
       Maps a dictionary to a `ProjectSearchProfile` object.

       :param data: dict - The dictionary containing search profile details.
       :return: ProjectSearchProfile - The mapped `ProjectSearchProfile` object.
       """
        return ProjectSearchProfile(
            name=data.get('name'),
            description=data.get('description'),
        )

    @classmethod
    def map_to_token(cls, data: dict) -> ProjectToken:
        """
       Maps a dictionary to a `ProjectToken` object.

       :param data: dict - The dictionary containing token details.
       :return: ProjectToken - The mapped `ProjectToken` object.
       """
        return ProjectToken(
            description=data.get('description'),
            token_id=data.get('id'),
            name=data.get('name'),
            status=data.get('status'),
            timestamp=data.get('timestamp'),
        )

    @classmethod
    def map_to_usage_limit(cls, data: dict) -> ProjectUsageLimit:
        """
        Maps a dictionary to a `ProjectUsageLimit` object.

        :param data: dict - The dictionary containing usage limit details.
        :return: ProjectUsageLimit - The mapped `ProjectUsageLimit` object.
        """
        return ProjectUsageLimit(
            hard_limit=data.get("hardLimit"),
            usage_limit_id=data.get("id"),
            related_entity_name=data.get("relatedEntityName"),
            remaining_usage=data.get("remainingUsage"),
            renewal_status=data.get("renewalStatus"),
            soft_limit=data.get("softLimit"),
            status=data.get("status"),
            subscription_type=data.get("subscriptionType"),
            usage_unit=data.get("usageUnit"),
            used_amount=data.get("usedAmount"),
            valid_from=data.get("validFrom"),
            valid_until=data.get("validUntil"),
        )

    @classmethod
    def map_to_item(cls, data: dict) -> ProjectItem:
        return ProjectItem(
            assistant=data.get('assistant'),
            intent=data.get('intent'),
            timestamp=data.get('timestamp'),
            prompt=data.get('prompt'),
            output=data.get('output'),
            input_text=data.get('inputText'),
            status=data.get('status')
        )
