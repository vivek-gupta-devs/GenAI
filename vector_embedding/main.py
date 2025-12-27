from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.embeddings.create(
    input="Having a guava in your tiff or snack time might just aid in strengthening your heart.",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)