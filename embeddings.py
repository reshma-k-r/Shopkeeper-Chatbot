# embeddings.py

import os
import pandas as pd
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Function to load and initialize embeddings
def vector_embedding():
    if "vectors" not in st.session_state:  # Check if embeddings are already initialized
        model_name = "models/embedding-001"
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model=model_name)

        csv_directory = r"./"  # Directory containing your CSV files

        if not os.path.exists(csv_directory):
            st.error("The specified directory does not exist.")
            return

        csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
        if not csv_files:
            st.error("No CSV files found in the specified directory.")
            return

        # Load CSV files and create documents
        st.session_state.docs = []

        for csv_file in csv_files:
            df = pd.read_csv(os.path.join(csv_directory, csv_file))
            for index, row in df.iterrows():
                content = f"Name: {row['Product Name']}\nDescription: {row['Description']}\nPrice: {row['Price']}\nStock: {row['Stock Quantity']}\nSupplier: {row['Supplier Information']}"
                st.session_state.docs.append(Document(page_content=content, metadata={"source": csv_file}))

        if not st.session_state.docs:
            st.error("No documents loaded.")
            return

        # Split documents for better retrieval
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)

        # Initialize the vector store with the documents
        if st.session_state.final_documents:
            st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
            st.success("Embeddings and vector store initialized.")
        else:
            st.error("No documents after splitting. Please check the document content.")
