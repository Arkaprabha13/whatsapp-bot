import pyperclip
import pyautogui
import time
from groq import Groq

client = Groq(
    api_key="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"
)

def is_last_message_from_sender(chat_log, sender_name='Harsh (Roommate)'):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# This clicks the mozilla firefox icon to open whatsapp web at co-ordinates 1745,1738
pyautogui.click(1479, 1748)
time.sleep(1)

while True:
    time.sleep(2)
    # select the the chats for reply
    pyautogui.moveTo(1136, 309)
    pyautogui.dragTo(2694, 1631, duration=2.0, button='left')

    # copy the chat in clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1086, 324)

    # paste the chat in a variable called text
    chat_history = pyperclip.paste()

    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "You are person named priyanshu who speaks both english and hindi. You are from India and you are a coder. You Analyze the chat history and resond like priyanshu. Output should be next chat response (text message only)"
                },
                {
                   "role": "system",
                    "content": "Do not start like this [21:02, 12/6/2025] Harsh (Roommate)" 
                },
                {
                    "role": "user",
                    "content": chat_history
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


        pyperclip.copy(response)

        # click at the message section
        pyautogui.click(1790, 1639)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')
    

