import streamlit as st
import pandas
from pydub import AudioSegment
from pathlib import Path
from speech_recognition import Recognizer, AudioFile
#design the web app

st.title("Mood from Speech")
st.subheader("We analyze your audio file based on words you use and say if it is positive or not!")


#upload and save Audio file
uploaded_file = st.file_uploader("Please upload your Audio file:",type=['wav'])
if uploaded_file is not None:
  if uploaded_file.name.endswith('wav'):
    audio = pydub.AudioSegment.from_wav(uploaded_file)
    

#turn to text
recognizer = Recognizer()

with AudioFile(audio) as audio_file:
  audio_rec = recognizer.record(audio_file)

text  = recognizer.recognize_google(audio_rec)
#analyzing the text
#show the result