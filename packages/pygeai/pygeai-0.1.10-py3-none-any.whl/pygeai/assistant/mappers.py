from pygeai.assistant.responses import AssistantResponse
from pygeai.core.base.mappers import ModelMapper
from pygeai.core.base.models import Assistant, Project


class AssistantResponseMapper:

    @classmethod
    def map_to_assistant_response(cls, data: dict) -> Assistant:
        assistant = ModelMapper.map_to_assistant(data)

        return assistant

    @classmethod
    def map_to_assistant_created_response(cls, data: dict) -> Project:
        project = ModelMapper.map_to_project(data)

        return project

