import streamlit as st
import subprocess
import os

# Title and description
st.title("Video to Text Transcription")
st.write("Upload your video and get the transcription!")

# Upload the video file
video_file = st.file_uploader("Upload a video", type=["mp4", "mov"])

if video_file is not None:
    # Save the uploaded video to a temporary location
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.getbuffer())

    # Extract audio from the video using FFmpeg
    with st.spinner("Converting video to audio..."):
        subprocess.run(["ffmpeg", "-i", "temp_video.mp4", "-vn", "output_audio.wav"])

    # Transcribe the audio using Whisper AI
    with st.spinner("Transcribing audio..."):
        transcription = subprocess.check_output(["whisper", "output_audio.wav", "--language", "English"])

    # Display the transcription
    st.header("Transcription")
    st.write(transcription.decode("utf-8"))

    # Clean up the temporary video and audio files
    os.remove("temp_video.mp4")
    os.remove("output_audio.wav")
