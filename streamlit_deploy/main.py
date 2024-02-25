import streamlit as st

st.set_page_config(page_title="MLOps", page_icon="🤖", layout="wide")
st.title("MLOps")
st.write("by Kimberly and Ryan")
st.subheader("Please select your desired prediction:")
st.markdown(
    '<button style="background-color: #F5F5DC; color: maroon; font-size: 20px; border: none; padding: 10px 20px; border-radius: 5px;">'
    '<a href="/mushroom_pred" target="_self" style="text-decoration: none; color: maroon;">'
    '🍄Mushroom Prediction🍄'
    '</a></button>',
    unsafe_allow_html=True
)
