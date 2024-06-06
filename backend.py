from flask import Flask, request, jsonify
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import io
import os
from flask_cors import CORS

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
app = Flask(__name__)
CORS(app)

kabyle = "C:/Users/sarah/Documents/3EMME ANNEE/SECOND SEMESTER/GROUP PROJECT/model/meluxina/team1trained-kab"
arab ="C:/Users/sarah/Documents/3EMME ANNEE/SECOND SEMESTER/GROUP PROJECT/model/meluxina/team1trained-arq"

processor_kabyle = WhisperProcessor.from_pretrained("openai/whisper-medium")
processor_darija = WhisperProcessor.from_pretrained("openai/whisper-small")

model_kabyle = WhisperForConditionalGeneration.from_pretrained(kabyle)
model_darija = WhisperForConditionalGeneration.from_pretrained(arab)
@app.route("/transcribekabyle", methods=["POST"])
def transcribe_audio_kabyle():
    if request.method == "POST":
        try:
            if 'audio_data' not in request.files:
                return jsonify({"error": "No audio file provided"}), 400
            
            audio_file = request.files['audio_data']
            print(f"Received file: {audio_file.filename}")
            audio_bytes = audio_file.read()
            print(f"Audio bytes length: {len(audio_bytes)}")
            
            try:
                audio_stream = io.BytesIO(audio_bytes)
                waveform, sampling_rate = librosa.load(audio_stream, sr=16000)
                print(f"Waveform shape: {waveform.shape}, Sampling rate: {sampling_rate}")
            except Exception as e:
                print(f"Librosa load error: {e}")
                return jsonify({"error": f"Librosa load error: {e}"}), 500
            
            input_features = processor_kabyle(waveform, sampling_rate=sampling_rate, return_tensors="pt").input_features
            predicted_ids = model_kabyle.generate(input_features)
            transcription = processor_kabyle.batch_decode(predicted_ids, skip_special_tokens=True)

            return jsonify({"transcription": transcription[0]})
            
        except Exception as e:
            print(f"Error during transcription: {e}")
            return jsonify({"error": f"cannot transcribe: {e}"}), 500
        
@app.route("/transcribedarija", methods=["POST"])
def transcribe_audio_darija():
    if request.method == "POST":
        try:
            if 'audio_data' not in request.files:
                return jsonify({"error": "No audio file provided"}), 400
            
            audio_file = request.files['audio_data']
            print(f"Received file: {audio_file.filename}")
            audio_bytes = audio_file.read()
            print(f"Audio bytes length: {len(audio_bytes)}")
            
            try:
                audio_stream = io.BytesIO(audio_bytes)
                waveform, sampling_rate = librosa.load(audio_stream, sr=16000)
                print(f"Waveform shape: {waveform.shape}, Sampling rate: {sampling_rate}")
            except Exception as e:
                print(f"Librosa load error: {e}")
                return jsonify({"error": f"Librosa load error: {e}"}), 500
            
            input_features = processor_darija(waveform, sampling_rate=sampling_rate, return_tensors="pt").input_features
            predicted_ids = model_darija.generate(input_features)
            transcription = processor_darija.batch_decode(predicted_ids, skip_special_tokens=True)

            return jsonify({"transcription": transcription[0]})
            
        except Exception as e:
            print(f"Error during transcription: {e}")
            return jsonify({"error": f"cannot transcribe: {e}"}), 500
if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
