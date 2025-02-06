import streamlit as st
import time
from datetime import datetime, timedelta

# Target date (25th February at midnight)
target_date = datetime(datetime.today().year, 2, 25, 0, 0, 0)

# If today is past 25th February, set target for next year
if datetime.today() > target_date:
    target_date = datetime(datetime.today().year + 1, 2, 25, 0, 0, 0)

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
        .stApp {
            background-image: url('https://wallpapers.com/images/hd/funny-cat-flying-peacefully-mtd434pqnxc308j4.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        body {
            background-image: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366');
            background-size: cover;
            background-color:rgb(25, 92, 210);
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
            color:rgb(255, 218, 96);
            text-align: center;
            font-weight: bold;
        }
        .countdown-container {
            text-align: center;
            font-size: 2rem;
            color:rgb(255, 255, 255);;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">! Countdown to Birthday !</h1>', unsafe_allow_html=True)

# Create placeholders for the countdown and animation
countdown_placeholder = st.empty()
image_placeholder = st.empty()
title_placeholder = st.empty()

# Animation Loop
while True:
    # Update countdown time
    now = datetime.now()
    time_remaining = target_date - now

    # Extract days, hours, minutes, seconds
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Show countdown timer
    if time_remaining.total_seconds() > 0:
        countdown_placeholder.markdown(
            f'<p class="countdown-container">{days} Days : {hours:02d} Hours : {minutes:02d} Minutes : {seconds:02d} Seconds</p>',
            unsafe_allow_html=True,
        )
    else:
        countdown_placeholder.markdown(
            '<p class="countdown-text">Happy Birthday 🎂</p>',
            unsafe_allow_html=True
        )

    # Update position of the moving cat
    st.session_state.position += st.session_state.direction

    # Reverse direction at top or bottom limits
    if st.session_state.position >= 200:
        st.session_state.direction = -5
        if time_remaining.total_seconds() > 0:
            title_placeholder.markdown('<p class="countdown-text">Almost there! 🎉</p>', unsafe_allow_html=True)
        else:
            title_placeholder.markdown('<p class="countdown-text">Have an amazing day! 🎉</p>', unsafe_allow_html=True)
        time.sleep(1)
    elif st.session_state.position <= 50:
        st.session_state.direction = 5
        if time_remaining.total_seconds() > 0:
            title_placeholder.markdown('<p class="countdown-text">Get ready! 🎈</p>', unsafe_allow_html=True)
        else:
            title_placeholder.markdown('<p class="countdown-text">Pagga!!</p>', unsafe_allow_html=True)
        
        time.sleep(1)

    # Display the moving image with smooth animation
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
