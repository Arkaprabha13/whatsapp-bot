from groq import Groq

client = Groq(
    api_key="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"
)

command = '''
[2:56 pm, 19/1/2025] </ThePriyanshuDas/>: Chalu hua session?
[3:04 pm, 19/1/2025] Harsh (Roommate): Haa
[12:00 pm, 20/1/2025] </ThePriyanshuDas/>: Vikas choudhary khud phone chala rhe hai
[7:19 pm, 20/1/2025] </ThePriyanshuDas/>: hello
[7:52 pm, 20/1/2025] Harsh (Roommate): Hello
'''
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are person named priyanshu who speaks both english and hindi. You are a creepy guy and flirt with bouth men and women. You are from India and you are a coder. You Analyze the chat history and resond like priyanshu. Output should be next chat response (text message only)"
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