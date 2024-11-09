import os
import time
import streamlit as st
from langchain_groq import ChatGroq
from embeddings import vector_embedding  # Assuming the embeddings are loaded in embeddings.py
from retriever import retrieve_answer  # Assuming retrieve_answer is in retriever.py
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit title and header
st.set_page_config(page_title="Shop Inventory Chatbot", page_icon="🛒", layout="centered")
st.title("Shop Inventory Chatbot")
st.markdown(
    """
    Welcome to the **Shop Inventory Assistant**! I'm here to help you with product details, stock information, prices, and more.
    Just type in your question, and I'll assist you. 😊
    """
)

# Initialize the language model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question

    <context>
    {context}
    </context>

    Questions:{input}
    """
)

# Initialize the embeddings and vector store only once when the app starts
if "vectors" not in st.session_state:
    vector_embedding()  # Initialize the embeddings and vector store

# Sidebar with instructions
st.sidebar.header("How to Use")
st.sidebar.markdown(
    """
    ## Instructions:
    - **Ask about the shop's inventory**: Type your query in the input box below. For example:
        - "What is the price of product X?"
        - "How much stock of product Y is available?"
        - "Can you suggest a product similar to product A?"
    
    - **Press "Search"** or **Hit Enter**: After typing your question, press the **Search** button or simply hit **Enter** to submit your query.
    
    - **Clear Conversation**: 
        - To reset the conversation and start fresh, click on the **Clear Conversation** button. This will remove all previous messages and start a new interaction.
            
    If you face any issues, just ask me again, and I’ll be happy to help!
    """
)


# Display a friendly greeting at the top
message = "Hello! How can I assist you today? 😊"
typing_placeholder = st.empty()

typing_message = ""
for char in message:
    typing_message += char
    typing_placeholder.markdown(f"<h5>{typing_message}</h5>", unsafe_allow_html=True)
    time.sleep(0.01)

# Text input for user query with placeholder text and styling
user_query = st.text_input("Ask about the inventory:", placeholder="e.g., 'What is the price of product X?'")

# Search button to trigger the response
search_button = st.button("Search")

# Function to render chat bubbles with styling
def render_chat_bubbles():
    if "conversation_history" in st.session_state:
        for interaction in st.session_state.conversation_history:
            if "user" in interaction:
                st.markdown(
                    f'<div style="text-align:left; margin-bottom:10px; background-color:#f1f1f1; color:#333; border-radius:15px; padding:12px 20px; box-shadow:0px 2px 5px rgba(0, 0, 0, 0.1); width:80%; max-width: 80%;">'
                    f'<strong>User:</strong><br>{interaction["user"]}</div>',
                    unsafe_allow_html=True
                )
            if "bot" in interaction:
                st.markdown(
                    f'<div style="text-align:right; margin-bottom:10px; background-color:#4CAF50; color:white; border-radius:15px; padding:12px 20px; box-shadow:0px 2px 5px rgba(0, 0, 0, 0.1); width:80%; max-width: 80%;">'
                    f'<strong>Bot:</strong><br>{interaction["bot"]}</div>',
                    unsafe_allow_html=True
                )

# Show chat history with bubbles
render_chat_bubbles()

# Clear the conversation button
if st.button("Clear Conversation"):
    # Clear the conversation history from session state
    if "conversation_history" in st.session_state:
        del st.session_state["conversation_history"]
    
    # Rerun the app to reset the UI
    st.rerun()

# Process the query when the user presses "Search" or "Enter"
if user_query and (search_button or st.session_state.get("submitted", False)):
    # Mark that the query has been submitted
    st.session_state.submitted = True

    # Show loading spinner while processing
    with st.spinner('Fetching response...'):
        # Check if vectors are initialized before accessing
        if "vectors" not in st.session_state:
            st.error("Vector store not initialized. Please make sure embeddings have been loaded.")
        else:
            # Call the retriever to process the input and fetch the response
            response = retrieve_answer(llm, st.session_state.vectors, prompt, user_query)

            # Display the chatbot response in a nice format
            st.write("### Chatbot Response:")
            st.markdown(f"**{response}**")

            # Store the conversation history
            if "conversation_history" not in st.session_state:
                st.session_state.conversation_history = []

            # Add the current interaction to the conversation history
            st.session_state.conversation_history.append({"user": user_query, "bot": response})

            # Show updated conversation history with chat bubbles
            render_chat_bubbles()

# Reset the session state after processing (Optional)
if user_query and not search_button:
    st.session_state.submitted = False
