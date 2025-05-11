import streamlit as st

st.set_page_config(page_title= "My Website", page_icon = "🌎", layout= "centered")
st.title("Welcome to my First Python Website")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("home page")
    st.write("This is a simple homepage built with Python and Streamlit")
    name = st.text_input("What is your name?")
    if name:
        st.success(f"Hello! {name}, Thanks for visiting.")

elif page == "About":
    st.header("About")
    st.write("This website is built entirely using Python and Streamlit in under 15 minutes")

elif page == "Contact":
    st.header("Contact us")
    email = st.text_input("Your email")
    message = st.text_input("Your message")
    if st.button("Submit"):
        st.success("Thank you, we have received your message.")