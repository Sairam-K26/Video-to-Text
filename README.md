This is an Video to Text transcription with help of ffmpeg and whisper ai

It changes the given video format to the specified audio format using **"ffmpeg"** and feeds it to **"whisper"** and transcribes the audio to text witrh specified language

Step -1 
Install FFmpeg
```
pip install ffmpeg
```
Test ffmpeg using 
```
ffmpeg -i ["sample file with format"] ["aimed file convertion format"]
```

step - 2 
Install Whisper
```
pip install whisper
```

step - 3
Then run the voice_to_audio.py using 
```
streamlit run voice_to_text.py
```
