import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

archivo = st.file_uploader("Sube un archivo .txt con el contexto",type='txt')

if archivo is None:
    st.info("💡 Esperando archivo...")
    st.stop()

contexto_local = archivo.read().decode("utf-8")  
#txt="What is up?"#+contexto
prompt = st.chat_input("que onda")
#promptfinal=contexto+prompt
if prompt==None:
   st.stop()

with st.chat_message("user",avatar="😾"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": f"""Eres un asistente que actúa como H. P Lovecraft, 
            y debes usar el siguiente contexto:\n\n {contexto_local}"""},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content

with st.chat_message("assistant"):
   st.write(respuesta)
