import streamlit as st   
st.title("Mi primer App")
data='https://youtu.be/VbXEc9vpeIM?si=fhfqG-flXoE8Hzb1'

option = st.selectbox("Video o foto?",(None,"Video", "foto"))

if option=='Video':
  st.video(data)  
elif option=='foto':
  bt=st.button("Click si estás seguro que elegiste foto")
  if bt:
    st.image('par1.png')


#jjlksdjlkjsdlkfjsldkfjsdfsdfs

# mini bot


#st.set_page_config(page_title="Ejemplo Chat", layout="centered")

st.title("💬 Mini Chatbot (solo repite lo que dices)")

# Entrada tipo chat (abajo de la pantalla)
user_input = st.chat_input("Escribe algo...")

# Si el usuario escribe algo, mostramos los mensajes
if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user").write(user_input)

    # Mostrar una respuesta simple del asistente
    st.chat_message("assistant").write(f"{user_input} <- eso dijiste")