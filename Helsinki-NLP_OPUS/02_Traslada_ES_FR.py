from transformers import MarianMTModel, MarianTokenizer

# Definir el modelo y el tokenizador
modelo_nombre = "Helsinki-NLP/opus-mt-es-fr"
tokenizer = MarianTokenizer.from_pretrained(modelo_nombre)
modelo = MarianMTModel.from_pretrained(modelo_nombre)

# Texto en español para traducir
texto_espanol = "El producto tiene un valor de 200 USD por hora"

# Tokenización y traducción
tokens = tokenizer(texto_espanol, return_tensors="pt", padding=True, truncation=True)
traduccion_tokens = modelo.generate(**tokens)
traduccion_frances = tokenizer.decode(traduccion_tokens[0], skip_special_tokens=True)

# Mostrar resultado
print(f"Texto en español: {texto_espanol}")
print(f"Traducción en frances: {traduccion_frances}")