import streamlit as st
import requests
import json
import time

def generate_word_by_word_response(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {'Content-Type': 'application/json'}
    data = {
        "model": "ScriptSavvy",
        "prompt": prompt,
        "stream": True  
    }
    with requests.post(url, headers=headers, data=json.dumps(data), stream=True) as response:
        response.raise_for_status()
        for line in response.iter_lines():
            if line:
                yield json.loads(line.decode('utf-8'))

def main():
    st.title("ScriptSavvy Chatbot 🤖")

    with st.sidebar:
        st.markdown("<h2 style='text-align: left; color: white;'>Drawer Content</h2>", unsafe_allow_html=True)
        st.write("")

    prompt = st.text_input("Enter your prompt:")
    if st.button("Generate Response"):
        word_generator = generate_word_by_word_response(prompt)
        output_slot = st.empty() 
        response_text = []
        for json_obj in word_generator:
            response_text.append(json_obj.get('response', ''))
            response_html = "".join(response_text)
            output_slot.markdown(response_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
