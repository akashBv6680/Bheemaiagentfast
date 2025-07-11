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
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("https://wallpapercave.com/wp/wp1873327.jpg");
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("HELLO I'M BHEEMA AI Chatbot")

    with st.form("query_form"):
        query = st.text_input("You: ")
        submitted = st.form_submit_button("Submit")

    if submitted:
        response = get_response(query)
        st.write("BHEEMA AI: ", response)

        with st.form("next_query_form"):
            next_query = st.text_input("You (next question): ")
            next_submitted = st.form_submit_button("Submit Next", key="next_submit")

        if next_submitted:
            next_response = get_response(next_query)
            st.write("BHEEMA AI: ", next_response)

if __name__ == "__main__":
    main()
