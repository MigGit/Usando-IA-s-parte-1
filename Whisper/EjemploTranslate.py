import whisper

# Cargar el modelo preentrenado
model = whisper.load_model("base")  # Puedes usar "medium" o "large" para más precisión

# Ruta del archivo de audio
audio_path = "Todo_es_negociable.mp3"  # Asegúrate de que el archivo existe en la misma carpeta

# Transcribir y traducir el audio al inglés
result = model.transcribe(audio_path, task="translate")

# Mostrar la traducción en inglés
print(result["text"])