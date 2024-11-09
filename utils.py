# utils.py

import streamlit as st


def display_conversation_history():
    if "conversation_history" in st.session_state:
        st.write("### Conversation History")
        for interaction in st.session_state.conversation_history:
            if "user" in interaction:
                st.write(f"*User:* {interaction['user']}")
            if "bot" in interaction:
                st.write(f"*Bot:* {interaction['bot']}")
