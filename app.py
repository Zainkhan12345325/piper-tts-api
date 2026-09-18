from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
import io
import wave
from piper import PiperVoice

app = FastAPI()

voice = PiperVoice.load("model.onnx")


@app.get("/")
def health():
    return {"status": "ok", "message": "Piper TTS API is running"}


@app.post("/speak")
def speak(text: str = Form(...)):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(voice.config.sample_rate)
        voice.synthesize(text, wav_file)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="audio/wav")
