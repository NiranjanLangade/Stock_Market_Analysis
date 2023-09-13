import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st


start = '2010-1-1'
end = '2022-6-13'

st.title('Stock Market Analysis')

user_input = st.text_input('Enter Stock Ticker','^NSEI')
df = data.DataReader(user_input,'yahoo',start,end)

st.subheader('Data from 2010 till Today')
st.write(df.describe())

st.subheader('Opening Price vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Open)
plt.xlabel('Date')
plt.ylabel('Open Price')
st.pyplot(fig)

st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.xlabel('Date')
plt.ylabel('Close Price')
st.pyplot(fig)

st.subheader('Volume vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Volume)
plt.xlabel('Date')
plt.ylabel('Volume Traded')
st.pyplot(fig)

st.subheader('Total Traded vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Open*df.Volume)
plt.plot(label = 'Open Price')
plt.xlabel('Date')
plt.ylabel('Total Traded')
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100,label='ma100')
plt.plot(df.Close,label='Close Price')
plt.legend()
plt.xlabel('Date')
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100,'r',label = 'ma100')
plt.plot(ma200,'g',label = 'ma200')
plt.plot(df.Close,'b',label='Close Price')
plt.legend()
plt.xlabel('Date')
st.pyplot(fig)

st.title('Comparing with another stock')
compare_input = st.text_input('Enter Stock Ticker','TSLA')
df1 = data.DataReader(compare_input,'yahoo',start,end)

st.subheader('Data from 2010 till Today')
st.write(df1.describe())

st.subheader('Opening Price vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Open,label='Open Price of '+user_input)
plt.plot(df1.Open,label='Open Price of '+compare_input)
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
st.pyplot(fig)

st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close,label='Close Price of '+user_input)
plt.plot(df1.Close,label='Close Price Of '+compare_input)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
st.pyplot(fig)

st.subheader('Volume vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Volume,label='Volume Of '+user_input)
plt.plot(df1.Volume,label='Volume Of '+compare_input)
plt.xlabel('Date')
plt.ylabel('Volume Traded')
plt.legend()
st.pyplot(fig)

st.subheader('Total Traded vs Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Open*df.Volume,label='Total Traded '+user_input)
plt.plot(df1.Open*df1.Volume,label='Total Traded '+compare_input)
plt.legend()
plt.xlabel('Date')
plt.ylabel('Total Traded')
st.pyplot(fig)

