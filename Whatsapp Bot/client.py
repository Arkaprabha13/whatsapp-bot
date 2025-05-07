from groq import Groq

client = Groq(
    api_key="<your_api_key>"
)

command = '''
<test command to check that it produce response>
'''
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are person named <YOUR NAME> who speaks both english and hindi. You are from India and you are a coder. You Analyze the chat history and resond like <YOUR NAME>. Output should be next chat response (text message only)"
        },
        {
            "role": "user",
            "content": command
        },
        
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

response = ""
for chunk in completion:
    response += chunk.choices[0].delta.content or ""

print(response)
