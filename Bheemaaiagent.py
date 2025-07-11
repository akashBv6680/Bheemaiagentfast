import streamlit as st
import os
import requests

# Set API key
api_key = "tgp_v1_BvPlhwF-WQfAOBUmnV8OLm37Sdzbqmp9Uu8faPNSeIA"

# Set API endpoint and model
endpoint = "https://api.together.xyz/v1/chat/completions"
model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

def get_response(query):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "max_tokens": 512,
        "temperature": 0
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    else:
        return "Error: " + str(response.status_code)

def main():
    st.markdown(
        """
        <style>
        body {
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("https://picsum.photos/2000/1000");
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("HELLO I'M BHEEMA AI Chatbot")

    container = st.container()
    with container:
        query = st.text_input("You: ", key="query")
        if query:
            response = get_response(query)
            st.write("BHEEMA AI: ", response)
            st.session_state.query = ""
            with st.empty():
                next_query = st.text_input("You (next question): ", key="next_query")
                if next_query:
                    next_response = get_response(next_query)
                    st.write("B", next_response)

if __name__ == "__main__":
    main()
