from datetime import datetime

from pydantic.main import BaseModel
from typing import Optional


class Error(BaseModel):
    id: int
    description: str

    def __str__(self):
        error = {
            "id": self.id,
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
    default_revision: float
    description: str
    id: str
    name: str
    revisions: Optional[list[AssistantRevision]] = []

    def __str__(self):
        intent = {
            "assistantIntentDefaultRevision": self.default_revision,
            "assistantIntentDescription": self.description,
            "assistantIntentId": self.id,
            "assistantIntentName": self.name
        }
        if any(self.revisions):
            intent["revisions"] = self.revisions

        return str(intent)


class Organization(BaseModel):
    id: str
    name: str

    def __str__(self):
        organization = {
            "organizationId": self.id,
            "organizationName": self.name
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
    email: Optional[str] = None
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

        if self.search_profiles is not None and any(self.search_profiles):
            project["searchProfiles"] = self.search_profiles

        if self.tokens is not None and any(self.tokens):
            project["tokens"] = self.tokens

        if self.usage_limit is not None:
            project["usageLimit"] = self.usage_limit

        return str(project)


class ProjectItem(BaseModel):
    """
    {
      "assistant": "string",
      "intent": "string",
      "timestamp": "string",
      "prompt": "string",
      "output": "string",
      "inputText": "string",
      "status": "string"
    }
    """
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


class LlmSettings(BaseModel):
    """
    "llmSettings": {
        "providerName": "string",
        "modelName": "string",
        "temperature": "decimal",
        "maxTokens": "integer",
        "uploadFiles": "boolean",
        "llmOutputGuardrail": "boolean",
        "inputModerationGuardrail": "boolean",
        "promptInjectionGuardrail": "boolean"
      }
    """
    provider_name: str
    model_name: str
    temperature: float
    max_tokens: int
    upload_files: bool
    llm_output_guardrail: bool
    input_moderation_guardrail: bool
    prompt_injection_guardrail: bool

    def to_dict(self):
        return {
            "providerName": self.provider_name,
            "modelName": self.model_name,
            "temperature": self.temperature,
            "maxTokens": self.max_tokens,
            "uploadFiles": self.upload_files,
            "llmOutputGuardrail": self.llm_output_guardrail,
            "inputModerationGuardrail": self.input_moderation_guardrail,
            "promptInjectionGuardrail": self.prompt_injection_guardrail
        }

    def __str__(self):
        llm_setting = self.to_dict()
        return str(llm_setting)


class WelcomeDataFeature(BaseModel):
    """
    {
        "title": "string",
        "description": "string"
    }
    """
    title: str
    description: str

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description
        }

    def __str__(self):
        feature = self.to_dict()
        return str(feature)


class WelcomeDataExamplePrompt(BaseModel):
    """
    {
        "title": "string",
        "description": "string",
        "promptText": "string"
    }
    """
    title: str
    description: str
    prompt_text: str

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "promptText": self.prompt_text
        }

    def __str__(self):
        example_prompt = self.to_dict()
        return str(example_prompt)


class WelcomeData(BaseModel):
    """
    "title": "string",
    "description": "string",
    "features": [
        ],
        "examplesPrompt": [
        ]
      }
    """
    title: str
    description: str
    features: list[WelcomeDataFeature]
    examples_prompt: list[WelcomeDataExamplePrompt]


class Assistant(BaseModel):
    """
    {
      "assistantId": "string",
      "assistantName": "string",
      "intents": [ /* full option */

      ]
    }
    """
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    status: Optional[bool] = None
    type: Optional[str] = None
    prompt: Optional[str] = None
    intents: Optional[list[AssistantIntent]] = []
    project: Optional[Project] = None
    welcome_data: Optional[WelcomeData] = None

    def __str__(self):
        assistant = {
            "assistantId": self.id,
            "assistantName": self.name,
            "assistantType": self.type
        }
        if self.intents is not None and any(self.intents):
            assistant["intents"] = self.intents

        return str(assistant)


class TextAssistant(Assistant):
    pass


class ChatAssistant(Assistant):
    pass


class DataAnalystAssistant(Assistant):
    pass


class ChatWithDataAssistant(Assistant):
    pass


class RAGAssistant(Assistant):
    pass



