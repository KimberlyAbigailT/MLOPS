import streamlit as st

st.set_page_config(page_title="MLOps", page_icon="🐸", layout="wide")
st.title("MLOps")
st.sidebar.success("Select your desired prediction above 👀")
st.subheader("Kimberly and Ryan's MLOps Assignment")
st.write("Please select the prediction you would like to get first:")
st.markdown(
    '<button style="background-color: beige; color: brown; font-size: 20px; border: none; padding: 10px 20px; border-radius: 5px;">'
    '<a href="/mushroom_pred" target="_self" style="text-decoration: none; color: brown;">'
    '🏥Medical Prediction'
    '</a></button>',
    unsafe_allow_html=True
)
# st.markdown(
#     '<button style="background-color: beige; color: brown; font-size: 20px; border: none; padding: 10px 20px; border-radius: 5px;">'
#     '<a href="/HDB_Prediction" target="_self" style="text-decoration: none; color: brown;">'
#     '🏘️HDB Prediction'
#     '</a></button>',
#     unsafe_allow_html=True
# )
st.write("Alternatively, you can select the pages you want to go to from the sidebar on the left :)")