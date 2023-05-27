import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from utils import clean_text
data=pd.read_csv("labeled_data.csv")
data=data.iloc[::,2::]
data.tweet=data.tweet.map(clean_text)
TextData=data.tweet.to_list()
datay=data[["hate_speech","offensive_language","neither"]]
for column in datay.columns:
    datay[column]=(datay[column]-datay[column].min())/(datay[column].max()-datay[column].min())
datay=datay.to_numpy()
tok=tf.keras.preprocessing.text.Tokenizer(50000)
tok.fit_on_texts(TextData)
numericData=tok.texts_to_sequences(TextData)
MAX=0
for i in numericData:
    if len(i)>MAX:
        MAX=len(i)
numericData=tf.keras.utils.pad_sequences(numericData,MAX,padding="post")
model=tf.keras.Sequential([
    tf.keras.layers.Embedding(50000,64,input_length=MAX),
    tf.keras.layers.LSTM(128,return_sequences=True),
    tf.keras.layers.SimpleRNN(32),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(3,activation="softmax")
])
model.compile(optimizer="adam",loss=tf.keras.losses.MeanSquaredError(),metrics=["accuracy"])
model.fit(numericData,datay,epochs=50,batch_size=128)
model.save("model.h5")