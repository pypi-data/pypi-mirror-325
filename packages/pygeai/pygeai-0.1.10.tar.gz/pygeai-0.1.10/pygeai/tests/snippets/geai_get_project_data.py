from pygeai.core.clients import Geai

client = Geai()


response = client.get_project_data("2ca6883f-6778-40bb-bcc1-85451fb11107")
print(f"response: {response}")
