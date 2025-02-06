from pygeai.core.base.models import TextAssistant, LlmSettings, WelcomeData, WelcomeDataFeature, \
    WelcomeDataExamplePrompt
from pygeai.core.clients import Geai

client = Geai()

llm_settings = LlmSettings(
    provider_name="OpenAI",
    model_name="GPT-4",
    temperature=0.7,
    max_tokens=1000,
    upload_files=False,
    llm_output_guardrail=True,
    input_moderation_guardrail=True,
    prompt_injection_guardrail=True
)

welcome_data = WelcomeData(
    title="AI Assistant",
    description="An AI-powered assistant to help with various tasks.",
    features=[
        WelcomeDataFeature(title="Feature 1", description="Description of feature 1"),
        WelcomeDataFeature(title="Feature 2", description="Description of feature 2")
    ],
    examples_prompt=[
        WelcomeDataExamplePrompt(title="Example 1", description="This is an example", prompt_text="How can I help you today?"),
        WelcomeDataExamplePrompt(title="Example 2", description="Another example", prompt_text="Tell me a joke.")
    ]
)

assistant = TextAssistant(
    name="ChatBot",
    description="A chatbot assistant for customer support",
    prompt="Hello! How can I assist you today?",
    type="chat",
    llm_settings=llm_settings,
    welcome_data=welcome_data
)


response = client.create_assistant(assistant)
print(f"response: {response}")
