import streamlit as st
import openai
import whisper
from pydub import AudioSegment
import tempfile

openai.api_key = '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'

model = whisper.load_model("base")


def transcribe_audio(model, audio_file_path):
    # Convert the audio file to WAV format as Whisper works well with WAV
    audio = AudioSegment.from_file(audio_file_path, format="m4a")
    with tempfile.NamedTemporaryFile(suffix=".wav") as temp_audio_file:
        audio.export(temp_audio_file.name, format="wav")
        temp_audio_file.seek(0)

        # Use Whisper model to transcribe the audio file
        result = model.transcribe(temp_audio_file.name)
        return result["text"]


def summarize_text(text):
    messages = [{"role": "system", "content": "You are an office administrator, summarize the text in key points"}]
    messages.append({"role": "user", "content": text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]



st.title("Audio Transcription and Summary")

uploaded_file = st.file_uploader("Choose an M4A file", type="m4a")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    transcript = transcribe_audio(model, tmp_file_path)
    st.text_area("Transcription", transcript, height=250)

    if st.button("Generate Summary"):
        summary = summarize_text(transcript)
        st.text_area("Summary", summary, height=150)
