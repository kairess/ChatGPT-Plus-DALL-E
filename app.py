import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appeareance of the input. Response it shortly around 20 words"
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])
