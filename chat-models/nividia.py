from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import SystemMessage, HumanMessage
model = ChatNVIDIA(
  model="z-ai/glm-5.2",
  api_key="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", 
  temperature=1,
  top_p=1,
  seed=42,
)
response = model.invoke([
    SystemMessage(content="You are a helpful assistant. Always reply in English."),
    HumanMessage(content="are you good at coding if i comapre you with claude opus 4.7")
])

print(response.content)