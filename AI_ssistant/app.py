import openai
# import os

# openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = None


foo = openai.Completion.create(
    model="text-davinci-003", 
    prompt="Say this is a test", 
    max_tokens=7, 
    temperature=0
    )

print(foo)