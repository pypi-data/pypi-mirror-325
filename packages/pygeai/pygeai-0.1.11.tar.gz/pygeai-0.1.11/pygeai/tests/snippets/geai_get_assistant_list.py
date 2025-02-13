from pygeai.core.clients import Geai


client = Geai()


response = client.get_assistant_list("full")
print(f"response: {response}")
