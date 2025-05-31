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
contexto_local = archivo.read().decode("utf-8")  

if "messages" not in st.session_state:
   st.session_state.messages = [{"role": "system", "content": f"""Eres un 
   asistente que se cree H. P. Lovecraft y 
   respondes 
   las ecuaciones claramente, 
   usa los símbolos $ en lugar de los
   símbolos [] para las respuestas
, además vas a ayudarme a recomendar problemas a is alumnos de la
clase de física, utiliza el siguiente contexto para responder:\n\n{contexto_local}"""}]

for message in st.session_state.messages[1:]:
   with st.chat_message(message["role"]):
      st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):


   # Store and display the current prompt.
   st.session_state.messages.append({"role": "user", "content": prompt})
   with st.chat_message("user"):
      st.markdown(prompt)

   stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[{"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
                 ],
               stream=True,
        )    
 
   with st.chat_message("assistant"):
      response = st.write_stream(stream)
   st.session_state.messages.append({"role": "assistant", "content": response})