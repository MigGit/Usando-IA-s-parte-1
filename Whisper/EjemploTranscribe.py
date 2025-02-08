
import whisper

# Cargar el modelo preentrenado
model = whisper.load_model("base")  # Puedes cambiar a "medium" o "large" para más precisión

# Cargar y procesar el audio
audio_path = "Todo_es_negociable.mp3"  # Ruta de tu archivo de audio en español
result = model.transcribe(audio_path, task="translate")

# Mostrar la traducción al inglés
print(result["text"])