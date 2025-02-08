import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# 1. Seleccionar el dispositivo CPU -1
device = -1

# 2. Cargar el modelo y el tokenizer
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

classifier = pipeline(
    "sentiment-analysis", 
    model=model_name, 
    tokenizer=model_name,
    device=device
)

# 3. Frases de ejemplo
text_samples = [
    "Este producto es increíble, me encanta.",
    "No me gustó la experiencia, el servicio fue pésimo.",
    "No quiero saber nada más de su producto"
]

# 4. Inferencia
results = classifier(text_samples)

for text, result in zip(text_samples, results):
    print(f"Texto: {text}\nResultado: {result}\n")