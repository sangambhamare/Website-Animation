import streamlit as st

# CSS code for an animated gradient background
css_animation = """
<style>
/* Full-screen container for the animation */
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
}

/* The animated gradient background */
.animated-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
    z-index: -1;
}

/* Keyframes for the gradient animation */
@keyframes gradientAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Optional styling for overlay content */
.content {
    position: relative;
    z-index: 1;
    text-align: center;
    color: white;
    padding: 50px;
}
</style>

<div class="animated-bg"></div>
<div class="content">
  <h1>Welcome to My Animated Streamlit App</h1>
  <p>This is an example of a custom CSS animated background.</p>
</div>
"""

st.markdown(css_animation, unsafe_allow_html=True)

st.write("Main app content goes here...")
