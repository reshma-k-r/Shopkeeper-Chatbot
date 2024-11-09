# Shop Inventory Chatbot

Welcome to the **Shop Inventory Chatbot** repository! This chatbot is built to assist users in retrieving product details, stock information, prices, and recommendations from a shop inventory using a Retrieval-Augmented Generation (RAG) approach.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Module Documentation](#module-documentation)
   - [`main.py`](#mainpy)
   - [`classify_query.py`](#classify_querypy)
   - [`embeddings.py`](#embeddingspy)
   - [`retriever.py`](#retrieverpy)
   - [`config.py`](#configpy)
   - [`utils.py`](#utilspy)
   - [`requirements.txt`](#requirementstxt)
6. [Future Enhancements](#future-enhancements)
7. [License](#license)

---

## Overview

The **Shop Inventory Chatbot** is designed to assist users with inventory-related questions, such as product availability, price information, and recommendations. It leverages a Retrieval-Augmented Generation (RAG) approach, where data embeddings are stored and queried to enhance the language model’s ability to respond accurately based on product data.

---

## Features

- **Natural Language Query Support**: Ask about product details, availability, and recommendations.
- **Customizable Inventory Data**: Easily load CSV files for different inventories.
- **Interactive Interface**: Powered by Streamlit for a responsive user experience.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/shop-inventory-chatbot.git
   cd shop-inventory-chatbot


2. **Install Requirements Create a virtual environment (optional but recommended) and install the dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt

3. **API Keys**
   - Replace placeholders in main.py with your actual groq_api_key and google_api_key values.
  
4. **Run the Application**
   ```bash
   streamlit run main.py

