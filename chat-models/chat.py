from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=1024,
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("write a jaun elia type shayari in hinglish, dont break lines")
print(response.content)