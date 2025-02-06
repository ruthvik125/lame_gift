import streamlit as st
import time
from datetime import date

# Target date (25th February)
target_date = date(date.today().year, 2, 25)

# Today's date
today = date.today()

# If today is past 25th February, calculate for next year
if today > target_date:
    target_date = date(today.year + 1, 2, 25)

# Days remaining
days_left = (target_date - today).days

# Initialize session state for position and direction
if "position" not in st.session_state:
    st.session_state.position = 50  # Initial position
    st.session_state.direction = 5  # Movement step

# Set image URL
image_url = "https://s3.amazonaws.com/freecodecamp/running-cats.jpg"

# Page layout
st.set_page_config(page_title="Countdown to Birthday", page_icon="🎉", layout="wide")

# Background color and header
st.markdown("""
    <style>
        body {
            background-color: #f4f7fc;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            color: #4a90e2;
            font-size: 3rem;
            font-weight: bold;
        }
        .countdown-text {
            font-size: 2rem;
            color: #ff6347;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">! Countdown to Birthday !</h1>', unsafe_allow_html=True)

# Create an empty placeholder for the image
image_placeholder = st.empty()
title_placeholder = st.empty()

# Animation Loop
while True:
    # Update position
    st.session_state.position += st.session_state.direction

    # Reverse direction at top or bottom limits
    if st.session_state.position >= 200:
        st.session_state.direction = -5
        # Show days left or birthday message
        if days_left != 0:
            title_placeholder.markdown(f'<p class="countdown-text">{days_left} days left</p>', unsafe_allow_html=True)
        else:
            title_placeholder.markdown('<p class="countdown-text">Happy Birthday 🎂</p>', unsafe_allow_html=True)
        time.sleep(1)
    elif st.session_state.position <= 50:
        st.session_state.direction = 5
        # Show left to go message or birthday message
        if days_left != 0:
            title_placeholder.markdown('<p class="countdown-text">Get ready! 🎉</p>', unsafe_allow_html=True)
        else:
            title_placeholder.markdown('<p class="countdown-text">Pragya!!!!!! 🎈</p>', unsafe_allow_html=True)
        time.sleep(1)

    # Display the image at the updated position with smooth animation
    image_placeholder.markdown(
        f"""
        <div style="height: 300px; position: relative;">
            <img src="{image_url}" width="100px"
            style="position: absolute; top: {st.session_state.position}px; left: 100px; transition: top 0.1s;">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Pause for animation effect
    time.sleep(0.1)
    st.rerun()
