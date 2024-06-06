import streamlit as st
import requests

# st.title("8drtnaVoice: Upload the kabyle here")
# allowed_extensions = ["mp3", "wav", "ogg"]

# audio_file = st.file_uploader("Upload your Voice (.mp3)", type=allowed_extensions)

# if st.button("Transcribe"):
#     if audio_file is not None:
#         audio_data = audio_file.read()

#         files = {"audio_data": (audio_file.name, audio_data, audio_file.type)}
#         response = requests.post("http://127.0.0.1:5000/transcribekabyle", files=files)

#         if response.status_code == 200:
#             transcription_text = response.json()["transcription"]
#             st.success("Transcription:")
#             st.write(transcription_text)
#         else:
#             error_message = response.json().get("error", "An error occurred")
#             st.error(f"Error: {response.status_code} - {error_message}")
#     else:
#         st.write("Please upload an audio file in MP3 format.")



# st.title("8drtnaVoice: Upload the darija here")
# allowed_extensions = ["mp3", "wav", "ogg"]

# audio_file_darija = st.file_uploader("Upload your Voice (.mp3)", type=allowed_extensions)

# if st.button("Transcribe"):
#     if audio_file_darija is not None:
#         audio_data = audio_file_darija.read()

#         files = {"audio_data": (audio_file_darija.name, audio_data, audio_file_darija.type)}
#         response = requests.post("http://127.0.0.1:5000/transcribedarija", files=files)

#         if response.status_code == 200:
#             transcription_text = response.json()["transcription"]
#             st.success("Transcription:")
#             st.write(transcription_text)
#         else:
#             error_message = response.json().get("error", "An error occurred")
#             st.error(f"Error: {response.status_code} - {error_message}")
#     else:
#         st.write("Please upload an audio file in MP3 format.")











import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="8drtnaVoice",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: black; /* Light blue-purple color */
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: balck; /* Light blue-purple color */
        text-align: center;
    }
    .upload-box {
        border: 2px solid #9370db; /* Light blue-purple color */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        background-color: #e6e6fa;
        margin-bottom: 20px;
    }
    .button {
        background-color: #6a5acd; /* Light blue-purple color */
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 10px;
    }
    .stApp {
        background: linear-gradient(135deg, #6a5acd 40%, #9370db 80%);
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.markdown("<h1 class='title'>8drtnaVoice</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Upload and Transcribe Your Voice</h2>", unsafe_allow_html=True)

allowed_extensions = ["mp3", "wav", "ogg"]

# File upload boxes and buttons in columns with spacing
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("<div class='upload-box'>Upload your Darija Voice (.mp3, .wav, .ogg)</div>", unsafe_allow_html=True)
    audio_file_darija = st.file_uploader(" ", type=allowed_extensions, key="darija")

with col2:
    st.markdown("<div class='upload-box'>Upload your Kabyle Voice (.mp3, .wav, .ogg)</div>", unsafe_allow_html=True)
    audio_file_kabyle = st.file_uploader(" ", type=allowed_extensions, key="kabyle")

# Add some space between the upload boxes and buttons
st.markdown("<br>", unsafe_allow_html=True)

# Transcribe buttons
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    if st.button("Transcribe Darija", key="transcribe_darija"):
        if audio_file_darija is not None:
            audio_data = audio_file_darija.read()

            files = {"audio_data": (audio_file_darija.name, audio_data, audio_file_darija.type)}
            response = requests.post("http://127.0.0.1:5000/transcribedarija", files=files)

            if response.status_code == 200:
                transcription_text = response.json()["transcription"]
                st.success("Transcription:")
                st.write(transcription_text)
            else:
                error_message = response.json().get("error", "An error occurred")
                st.error(f"Error: {response.status_code} - {error_message}")
        else:
            st.warning("Please upload an audio file in MP3, WAV, or OGG format.")

with col2:
    if st.button("Transcribe Kabyle", key="transcribe_kabyle"):
        if audio_file_kabyle is not None:
            audio_data = audio_file_kabyle.read()

            files = {"audio_data": (audio_file_kabyle.name, audio_data, audio_file_kabyle.type)}
            response = requests.post("http://127.0.0.1:5000/transcribekabyle", files=files)

            if response.status_code == 200:
                transcription_text = response.json()["transcription"]
                st.success("Transcription:")
                st.write(transcription_text)
            else:
                error_message = response.json().get("error", "An error occurred")
                st.error(f"Error: {response.status_code} - {error_message}")
        else:
            st.warning("Please upload an audio file in MP3, WAV, or OGG format.")
