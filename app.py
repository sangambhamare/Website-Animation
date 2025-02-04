import streamlit as st

# Replace with your GitHub raw URL
video_url = "https://github.com/sangambhamare/Website-Animation/blob/master/Blue%20Neon%20Tech%20Coming%20Soon%20Video.mp4"

st.markdown(
    f"""
    <style>
    body, html {{
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}
    .video-background {{
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -1;
        background-size: cover;
    }}
    .content {{
        position: relative;
        z-index: 1;
        color: white;
        text-align: center;
        padding: 50px;
    }}
    </style>
    
    <video autoplay muted loop class="video-background">
      <source src="{video_url}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    
    <div class="content">
      <h1>Welcome to My Streamlit App</h1>
      <p>This content is displayed over the video background.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Main app content goes here.")
