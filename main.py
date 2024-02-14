## getting started with OpenAI api
import openai
from openai import OpenAI

# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY = 'sk-<your-api-key>'

client = OpenAI(api_key=OPENAI_API_KEY)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

response_message = completion.choices[0].message.content
print(response_message)
