from litellm import api_key, completion
import os

api_key = os.getenv('GROQ_API_KEY')

response = completion(
    model="qwen/qwen3.8-27b", 
    api_key = api_key,
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
)
print(response)