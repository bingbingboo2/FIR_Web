import streamlit as st
import google.generativeai as palm

# Configure the palm API
palm.configure(api_key="AIzaSyC5iqIChPW9mKJmexmtDbrmjj7_AjBbAYw")

# Load the pre-trained AI model
model_id = "models/chat-bison-001"

# Define the prompt
prompt = "I am an AI-powered legal documentation assistant. I can help you to draft and review legal documents, such as contracts, agreements, and court filings. What kind of legal document do you need help with?"

# Define the examples
examples = [
  ("I need help drafting a contract.", "I can help you with that. What are the key terms of the contract?"),
  ("I need to review an existing contract.", "I can help you with that. Can you please upload the contract to me?"),
  ("I have a question about a legal document.", "I can try to answer your question. Can you please tell me more about the document and your question?"),
]

# Create a Streamlit app
st.title("AI-powered Legal Documentation Assistant")

# Display the prompt
st.write(prompt)

# Get the user's input
user_input = st.text_input("What kind of legal document do you need help with?")

# Check if the user's input is empty
if not user_input:
  st.error("message must include non empty content")
  exit()

# Generate a response from the palm model
response = palm.chat(messages=user_input, temperature=0.2, context="Speak like a lawyer", examples=examples)

# Display the response to the user
st.write(response.last)

# Ask the user if they have any other doubts
st.write("Do you have any other doubts?")
ask_for_other_doubts_button = st.button("Yes")

# Define the function to ask the user for other doubts
def ask_for_other_doubts():
  user_input = st.text_input("What is your doubt?")

# Check if the user's input is empty
if not user_input:
   st.error("message must include non empty content")
   exit()

response = palm.chat(messages=user_input, temperature=0.2, context="Speak like a lawyer", examples=examples)
st.write(response.last)

# If the user clicks the button, ask them for their doubt
if ask_for_other_doubts_button:
  ask_for_other_doubts()
