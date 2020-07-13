import streamlit as st


st.title('Testing')
st.sidebar.title('More')
st.sidebar.checkbox('yellow')
st.write('StreamLit Version:', st.__version__)