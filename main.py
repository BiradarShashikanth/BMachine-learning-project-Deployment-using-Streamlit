import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle

st.image("https://www.jobvacancyresult.com/storage/company/1976_innomatics.png")


st.title("Emotion Detection using ML")
text = st.text_input("Enter the text")

import os
# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the path to the pickle file relative to the current script
pickle_file_path = os.path.join(current_dir, "estimator.pkl")

# Load the pickle file
with open(pickle_file_path, "rb") as f:
    model = pickle.load(f)
if st.button("Submit")==True:
    result = model.predict([text])[0]

if result == 'anger':
    st.image('https://th.bing.com/th/id/OIP.nPpz-xTWU7hPavd0Dk0tPAHaHa?w=199&h=199&c=7&r=0&o=5&dpr=1.3&pid=1.7')
elif result == 'sad':
    st.image('https://th.bing.com/th/id/OIP.Zm_5bSv5eFmTkAdeQ35YRQHaHa?w=207&h=207&c=7&r=0&o=5&dpr=1.3&pid=1.7')
elif result =='joy':
    st.image('https://th.bing.com/th/id/OIP.IggJ8SkHyM4sKkyz5YNAOAHaFx?w=283&h=220&c=7&r=0&o=5&dpr=1.3&pid=1.7')
elif result =='fear':
    st.image('https://th.bing.com/th/id/OIP.JGHSPZ9bIFX2KX24EZtA9wHaHa?w=199&h=199&c=7&r=0&o=5&dpr=1.3&pid=1.7')
elif result == 'surprise':
    st.image('https://th.bing.com/th/id/OIP.LT8MV_CXaQd-BD3IugwHdwHaHa?w=207&h=207&c=7&r=0&o=5&dpr=1.3&pid=1.7')
elif result=='love':
    st.image('https://th.bing.com/th/id/OIP.goX8rpAM7rzapdumqadctwHaHa?w=200&h=200&c=7&r=0&o=5&dpr=1.3&pid=1.7')                  
