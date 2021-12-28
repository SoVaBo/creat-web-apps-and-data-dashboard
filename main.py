import streamlit as st
import pandas

data = {
  "series_1":[1,3,4,5,7],
  "series_2":[10,30,40,100,250]
}
df=pandas.DataFrame(data)

st.title("First Webb App")
st.subheader("it is going to be awsome")
st.write('''just wait for it''')
st.write(df)

st.line_chart(df)
st.area_chart(df)

myslider=st.slider("Pound")
st.write(myslider,"in Pounds is",myslider*0.453592,"in Kgs")