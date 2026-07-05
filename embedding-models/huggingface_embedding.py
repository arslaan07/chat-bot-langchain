
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpointEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "jinaai/jina-embeddings-v5-omni-small"
)


vector = embeddings.embed_query("You are going to learn Gen Ai")

print(vector)