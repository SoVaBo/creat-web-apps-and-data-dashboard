import streamlit as st
import pandas
from pydub import AudioSegment
from pathlib import Path
from speech_recognition import Recognizer, AudioFile
import nltk
nltk.download('vader_lexicon')
nltk.download('twitter_samples')
from nltk.sentiment import SentimentIntensityAnalyzer
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
analyzer = SentimentIntensityAnalyzer()
P=0
N=0
for i in range(0,30000):
    text = nltk.corpus.twitter_samples.strings()[i]
    if analyzer.polarity_scores(text)['compound'] > 0:
        P += 1
    else:
        N += 1

#show the result
analyzer = SentimentIntensityAnalyzer()
P=0
N=0
if analyzer.polarity_scores(text)['compound'] > 0:
  st.write('The Audio mood is :)')
else:
  st.write('Sad Audio :(')