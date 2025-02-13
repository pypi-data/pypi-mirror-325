from typing import Optional

from pydantic.main import BaseModel

from pygeai.core.base.models import Assistant, Project, AssistantIntent, Assistant, LlmSettings, WelcomeData


class AssistantResponse(BaseModel):
    assistant: Assistant
