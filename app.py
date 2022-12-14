from email.mime import image
from PIL import Image
from shutil import which
import requests
from turtle import left, right
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open("images/test1.png")
img_lottie_animation = Image.open("images/img_lottie_animation.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Agus Pribadi :wave:")
    st.title("Mahasiswa Teknik Informatika UM Pontianak")
    st.write("Saya Secara Khusus Menekuni Project Python dan Data Science.")
    st.write(
        "[Kunjungi saya di Linkedin>](https://www.linkedin.com/in/agus-pribadi-2923b7162)"
    )

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write("""
                ---
                ---
                ---
                ---
                ---
                ---
                ---            
                """)
            st.write(
                "[Youtube Channel >](https://www.youtube.com/channel/UCLhfvhpgO1_wCQIGJ4r844Q)"
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate lottie Animations Inside Your Streamlit App")
        st.write("""
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do
            In this tutorial, I'll show you exactly how to do it
            """)
        st.markdown(
            "[Watch Video](https://www.youtube.com/channel/UCLhfvhpgO1_wCQIGJ4r844Q)"
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To You Streamlit App")
        st.write("""
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app Using
            """)
        st.markdown(
            "[Watch Video](https://www.youtube.com/channel/UCLhfvhpgO1_wCQIGJ4r844Q)"
        )

# --- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/aguspribadi368@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
     """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
