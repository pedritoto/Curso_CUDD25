import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

archivo = st.sidebar.file_uploader("Sube un archivo .txt con el contexto",type='txt')
st.sidebar.image("https://images.seeklogo.com/logo-png/5/1/facultad-de-ciencias-quimicas-logo-png_seeklogo-51591.png")
st.sidebar.markdown("""### Autor: Juan Pedro Palomares Báez
""")
if archivo is None:
    st.info("💡 Esperando archivo...")
    st.stop()


if "messages" not in st.session_state:
        st.session_state.messages = []
contexto_local = archivo.read().decode("utf-8")  
#txt="What is up?"#+contexto
prompt = st.chat_input("que onda")
#promptfinal=contexto+prompt
if prompt==None:
   st.stop()

for message in st.session_state.messages:
   with st.chat_message(message["role"]):
   st.markdown(message["user",avatar="😾","content"])
#with st.chat_message("user",avatar="😾"):
#   st.markdown(prompt)

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
st.session_state.messages.append({"role": "assistant", "content": respuesta})