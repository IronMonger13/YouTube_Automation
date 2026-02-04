from fastapi import FastAPI, HTTPException
from faster_whisper import WhisperModel
import os

app = FastAPI()

model = WhisperModel(
    "small",      # change model size if needed
    device="cpu",
    compute_type="int8"
)

@app.post("/asr")
async def transcribe(data: dict):
    audio_file = data.get("audio_file")

    if not audio_file or not os.path.exists(audio_file):
        raise HTTPException(status_code=400, detail="Audio file not found")

    segments, info = model.transcribe(audio_file, word_timestamps=True)

    full_text = ""
    output_segments = []

    for segment in segments:
        full_text += segment.text

        words = []
        if segment.words:
            for word in segment.words:
                words.append({
                    "word": word.word,
                    "start": word.start,
                    "end": word.end
                })

        output_segments.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "words": words
        })

    return {
        "text": full_text.strip(),
        "segments": output_segments
    }
