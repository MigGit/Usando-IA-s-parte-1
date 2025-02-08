from transformers import pipeline

# Carga del modelo y tokenizador fine-tuneado
ner_pipeline = pipeline("token-classification", 
                        model="bert_monedas_model", 
                        tokenizer="bert_monedas_model", 
                        aggregation_strategy="simple")

text = "El producto tiene un valor de 200 USD, por hora"
predicciones = ner_pipeline(text)
print("-------------------")
print(predicciones)
print("-------------------")