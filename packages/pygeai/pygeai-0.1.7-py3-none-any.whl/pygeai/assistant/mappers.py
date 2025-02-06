from pygeai.assistant.responses import AssistantResponse
from pygeai.core.base.mappers import ModelMapper
from pygeai.core.base.models import Assistant


class AssistantResponseMapper:

    @classmethod
    def map_to_assistant_response(cls, data: dict) -> Assistant:
        assistant = ModelMapper.map_to_assistant(data)

        return assistant

    @classmethod
    def map_to_assistant_data_response(cls, data: dict) -> AssistantResponse:
        assistant = ModelMapper.map_to_assistant(data)
        intent_list = ModelMapper.map_to_intent_list(data)
        project = ModelMapper.map_to_project(data)
        welcome_data = ModelMapper.map_to_welcome_data(data)

        return AssistantResponse(
            assistant=assistant,
            intents=intent_list,
            project=project,
            welcome_data=welcome_data
        )