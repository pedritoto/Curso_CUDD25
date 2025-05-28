import streamlit as st   
st.title("Mi primer App")
bt=st.button("Da click")
data='https://www.youtube.com/live/gdluMrQstCU?si=PTwieviPEJ82bh7y'
if bt:
  st.image('par1.png')

st.video(data, start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)
#jjlksdjlkjsdlkfjsldkfjsdfsdfs