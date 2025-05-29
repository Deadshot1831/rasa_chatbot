import streamlit as st
import requests

st.title("Mental Wellness Chatbot 💬")

# Store messages
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", "")

# On message send
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # Send message to Rasa REST endpoint
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input}
        )

        # Get bot reply
        for r in response.json():
            bot_msg = r.get("text")
            if bot_msg:
                st.session_state.chat_history.append(("Bot", bot_msg))
    except Exception as e:
        st.session_state.chat_history.append(("Bot", f"⚠️ Could not reach Rasa server. Error: {e}"))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
