from typing import Optional

from pydantic.main import BaseModel

from pygeai.core.base.models import Assistant, Project, Organization, ProjectSearchProfile, ProjectToken, \
    ProjectUsageLimit, ProjectItem


class AssistantListResponse(BaseModel):
    assistants: list[Assistant]
    project: Project


class ProjectListResponse(BaseModel):
    projects : list[Project]


class ProjectDataResponse(BaseModel):
    organization: Optional[Organization]
    project: Project
    search_profile: Optional[list[ProjectSearchProfile]]
    tokens: Optional[list[ProjectToken]]
    usage_limit: Optional[ProjectUsageLimit]


class ProjectTokensResponse(BaseModel):
    tokens: list[ProjectToken]


class ProjectItemListResponse(BaseModel):
    items: list[ProjectItem]
