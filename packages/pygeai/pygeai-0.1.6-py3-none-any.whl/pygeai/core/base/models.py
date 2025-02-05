from datetime import datetime

from pydantic.main import BaseModel
from typing import Optional


class Error(BaseModel):
    error_id: int
    description: str

    def __str__(self):
        error = {
            "id": self.error_id,
            "description": self.description
        }
        return str(error)


class AssistantRevisionMetadata(BaseModel):
    """
    {
      "key": "string",
      "type": "string",
      "value": "string"
    }
    """
    key: str
    type: str
    value: str

    def __str__(self):
        metadata = {
            "key": self.key,
            "type": self.type,
            "value": self.value
        }
        return str(metadata)


class AssistantRevision(BaseModel):
    """
    {
      "metadata": [
        ...
      ],
      "modelId": "string",
      "modelName": "string",
      "prompt": "string",
      "providerName": "string",
      "revisionDescription": "string",
      "revisionId": "string",
      "revisionName": "string",
      "timestamp": "timestamp"
    }
    """
    metadata: Optional[list[AssistantRevisionMetadata]] = []
    model_id: str
    model_name: str
    prompt: str
    provider_name: str
    revision_description: str
    revision_id: str
    revision_name: str
    timestamp: datetime

    def __str__(self):
        revision = {
            "modelId": self.model_id,
            "modelName": self.model_name,
            "prompt": self.prompt,
            "providerName": self.provider_name,
            "revisionDescription": self.revision_description,
            "revisionId": self.revision_id,
            "revisionName": self.revision_name,
            "timestamp": self.timestamp
        }
        if any(self.metadata):
            revision["metadata"] = self.metadata

        return str(revision)


class AssistantIntent(BaseModel):
    """
    {
          "assistantIntentDefaultRevision": "number",
          "assistantIntentDescription": "string",
          "assistantIntentId": "string",
          "assistantIntentName": "string",
          "revisions": [
            ...
          ]
        }
    """
    assistant_intent_default_revision: float
    assistant_intent_description: str
    assistant_intent_id: str
    assistant_intent_name: str
    revisions: Optional[list[AssistantRevision]] = []

    def __str__(self):
        intent = {
            "assistantIntentDefaultRevision": self.assistant_intent_default_revision,
            "assistantIntentDescription": self.assistant_intent_description,
            "assistantIntentId": self.assistant_intent_id,
            "assistantIntentName": self.assistant_intent_name
        }
        if any(self.revisions):
            intent["revisions"] = self.revisions

        return str(intent)


class Assistant(BaseModel):
    """
    {
      "assistantId": "string",
      "assistantName": "string",
      "intents": [ /* full option */

      ]
    }
    """
    id: str
    name: str
    type: str
    intents: Optional[list[AssistantIntent]] = []

    def __str__(self):
        assistant = {
            "assistantId": self.id,
            "assistantName": self.name,
            "assistantType": self.type
        }
        if any(self.intents):
            assistant["intents"] = self.intents

        return str(assistant)


class Organization(BaseModel):
    organization_id: str
    organization_name: str

    def __str__(self):
        organization = {
            "organizationId": self.organization_id,
            "organizationName": self.organization_name
        }
        return str(organization)


class ProjectSearchProfile(BaseModel):
    """
     {
      "name": "string",
      "description": "string"
    }
    """
    name: str
    description: str

    def __str__(self):
        search_profile = {
            "name": self.name,
            "description": self.description
        }
        return str(search_profile)


class ProjectToken(BaseModel):
    """
     {
      "description": "string",
      "id": "string",
      "name": "string",
      "status": "string", /* Active, Blocked */
      "timestamp": "timestamp"
    }
    """
    description: str
    token_id: str
    name: str
    status: str
    timestamp: datetime

    def __str__(self):
        token = {
            "description": self.description,
            "id": self.token_id,
            "name": self.name,
            "status": self.status,
            "timestamp": self.timestamp
        }
        return str(token)


class ProjectUsageLimit(BaseModel):
    """
    "hardLimit": "number",                // Upper usage limit
    "id": "string",                       // Usage limit ID
    "relatedEntityName": "string",        // Name of the related entity
    "remainingUsage": "number",           // Remaining usage
    "renewalStatus": "string",            // Renewal status (Renewable, NonRenewable)
    "softLimit": "number",                // Lower usage limit
    "status": "integer",                  // Status (1: Active, 2: Expired, 3: Empty, 4: Cancelled)
    "subscriptionType": "string",         // Subscription type (Freemium, Daily, Weekly, Monthly)
    "usageUnit": "string",                // Usage unit (Requests, Cost)
    "usedAmount": "number",               // Amount used (decimal or scientific notation)
    "validFrom": "timestamp",             // Start date of the usage limit
    "validUntil": "timestamp"             // Expiration or renewal date
    """
    hard_limit: float
    usage_limit_id: str
    related_entity_name: str
    remaining_usage: float
    renewal_status: str
    soft_limit: float
    status: int
    subscription_type: str
    usage_unit: str
    used_amount: float
    valid_from: datetime
    valid_until: datetime

    def __str__(self):
        usage_limit = {
            "hardLimit": self.hard_limit,
            "id": self.usage_limit_id,
            "relatedEntityName": self.related_entity_name,
            "remainingUsage": self.remaining_usage,
            "renewalStatus": self.renewal_status,
            "softLimit": self.soft_limit,
            "status": self.status,
            "subscriptionType": self.subscription_type,
            "usageUnit": self.usage_unit,
            "usedAmount": self.used_amount,
            "validFrom": self.valid_from,
            "validUntil": self.valid_until
        }
        return str(usage_limit)


class Project(BaseModel):
    """
     {
      "projectActive": "boolean",
      "projectDescription": "string",
      "projectId": "string",
      "projectName": "string",
      "projectStatus": "integer", /* 0:Active, 2:Hidden */
    }
    """
    organization: Optional[Organization] = None
    active: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: str
    email: Optional[str]
    status: Optional[int] = None
    search_profiles: Optional[list[ProjectSearchProfile]] = []
    tokens: Optional[list[ProjectToken]] = []
    usage_limit: Optional[ProjectUsageLimit] = None

    def __str__(self):
        project = {
            "projectName": self.name
        }

        if self.id:
            project["projectId"] = self.id

        if self.organization:
            project["organization"] = self.organization

        if self.active is not None:
            project["projectActive"] = self.active

        if self.description is not None:
            project["projectDescription"] = self.description

        if self.status is not None:
            project["projectStatus"] = self.status

        if any(self.search_profiles):
            project["searchProfiles"] = self.search_profiles

        if any(self.tokens):
            project["tokens"] = self.tokens

        if any(self.usage_limit):
            project["usageLimit"] = self.usage_limit

        return str(project)


class ProjectItem(BaseModel):
    assistant: str
    intent: str
    timestamp: str
    prompt: str
    output: str
    input_text: str
    status: str

    def __str__(self):
        item = {
            "assistant": self.assistant,
            "intent": self.intent,
            "timestamp": self.timestamp,
            "prompt": self.prompt,
            "output": self.output,
            "inputText": self.input_text,
            "status": self.status
        }
        return str(item)