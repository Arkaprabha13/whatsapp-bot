# WhatsApp Web Automation Bot


This Python script automates replying to specific messages on WhatsApp Web using natural language processing and GUI automation tools. The bot interacts with the chat interface and analyzes the conversation history to generate contextually appropriate responses.

# Features
Automated Message Scanning: Uses pyautogui to select and copy recent chat messages from WhatsApp Web.
Intelligent Response Generation: Integrates with the Groq API to generate replies using a large language model (LLM). The bot takes on the persona of a coder from India named Priyanshu, who can communicate in both English and Hindi.
Seamless Interaction: Replies are automatically typed and sent through the WhatsApp Web interface.
Sender-Specific Logic: Detects if the last message in the conversation is from a specific sender (e.g., "Harsh (Roommate)") before responding.

# Dependencies
pyautogui: For simulating mouse and keyboard actions.
pyperclip: For handling clipboard operations.
time: To add delays and manage the timing of actions.
Groq API: For generating AI-driven responses to chat messages.

# How It Works
WhatsApp Web Access: The script uses pyautogui to click on the Mozilla Firefox icon (or another browser) to open WhatsApp Web.
Message Scanning: Recent chats are selected and copied to the clipboard for analysis.
Message Analysis: The chat history is passed to the Groq API to generate an intelligent response in the voice of Priyanshu.
Replying: The response is pasted into the chat input field and sent automatically.

# Configuration
Coordinates: Ensure that the screen coordinates for clicking, selecting, and typing are configured correctly for your setup.
Groq API Key: Replace the placeholder API key in the script with your actual API key.
Sender Name: Update the sender's name (sender_name) to the desired contact you want the bot to reply to.

# Usage
Install the required dependencies using pip install pyautogui pyperclip.
Update the script with the correct screen coordinates and Groq API key.
Run the script: python whatsapp_bot.py.

# Disclaimer
This script automates GUI interactions and depends on specific screen coordinates, which may need to be adjusted based on your screen resolution and WhatsApp Web layout.
Use responsibly and ensure compliance with WhatsApp’s terms of service.
