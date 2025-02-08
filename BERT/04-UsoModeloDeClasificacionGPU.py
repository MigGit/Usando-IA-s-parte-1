from transformers import pipeline
import torch

# 1. Seleccionar el dispositivo (0 si hay GPU disponible, -1 si no)
device = 0 if torch.cuda.is_available() else -1

# Carga del modelo y tokenizador fine-tuneado
ner_pipeline = pipeline("token-classification", 
                        model="bert_monedas_model", 
                        tokenizer="bert_monedas_model", 
                        aggregation_strategy="simple",
                        device=device)

text = "El producto tiene un valor de 200 USD, por hora"
predicciones = ner_pipeline(text)
print("-------------------")
print(predicciones)
print("-------------------")