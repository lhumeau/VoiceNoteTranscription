from fastapi import FastAPI, HTTPException, status, File, UploadFile
import io
import speech_recognition as sr
from pydub import AudioSegment

app = FastAPI()

def convert_audio_to_wav(audio_data, format):
    audio = AudioSegment.from_file(audio_data, format=format)
    wav_audio = io.BytesIO()
    audio.export(wav_audio, format="wav")
    wav_audio.seek(0)
    return wav_audio

def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language='es-ES')
        return text
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return "No se pudo obtener resultados; {0}".format(e)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    audio_data = io.BytesIO(await file.read())
    file_extension = file.filename.split(".")[-1].lower()

    # Asumiendo que 'octet-stream' se maneja como 'm4a'
    file_format = 'm4a' if file.content_type == 'application/octet-stream' else file_extension

    if file_format not in ["3gp", "caf", "ogg", "m4a"]:
        return {"error": "Formato de archivo no admitido"}

    wav_audio = convert_audio_to_wav(audio_data, file_format)
    transcription = transcribe_audio(wav_audio)
    return {"transcription": transcription}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")

