import streamlit as st   
st.title("Mi primer App")
data='https://youtu.be/VbXEc9vpeIM?si=fhfqG-flXoE8Hzb1'

option = st.selectbox(
    "Video o foto?",
    ("Video", "foto"),
)

if option==Video:
  st.video(data)  
else
  bt=st.button("Click si estás seguro que elegiste foto")
  if bt:
    st.image('par1.png')


#jjlksdjlkjsdlkfjsldkfjsdfsdfs