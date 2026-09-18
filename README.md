# Piper TTS API

A minimal HTTP wrapper around Piper TTS.

POST to `/speak` with a form field `text` to receive back a WAV audio file.

Example:
curl -X POST https://YOUR-RENDER-URL.onrender.com/speak -F "text=Hello from Piper" --output out.wav
