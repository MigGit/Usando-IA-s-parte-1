# Helsinki-NLP/OPUS
## Ejemplo de uso de OPUS

El proyecto Helsinki-NLP/OPUS es una iniciativa de código abierto enfocada en la traducción automática.
Los ejemplos contemplan traducciones de 

 - Inglés a Español
 - Español a Inglés
 - Español a Francés

## Requerimientos

Para este ejemplo se utilizó Python 3.11.9 y se deben instalar todas estas librerías

Actualizar el pip

```sh
python.exe -m pip install --upgrade pip
```
## Enviromen

Creación de ambiente de ejecución, para la carga de las librerías sin afectar el ambiente principal

```sh
python -m venv ejemplo_opus
# Linux
    # Activa Enviroment
    source ejemplo_opus/Scripts/activate 

# Windows
    # Activa Enviroment
    ejemplo_opus\Scripts\activate.bat
    # Desactiva Enviroment
    ejemplo_opus\Scripts\deactivate.bat
```

## Ejemplos

Para ejecutar los ejemplos, se requiere la siguiente librería:

```sh
pip install transformers
pip install sentencepiece
pip install torch
```

### Traslada_EN_ES.py

```sh
python.exe .\Traslada_EN_ES.py
......
ES: 
this is the way
 
EN: 
Este es el camino.
```

### Traslada_ES_EN.py

```sh
python.exe .\Traslada_ES_EN.py
......
Texto en español: El producto tiene un valor de 200 USD por hora
Traducción en inglés: The product has a value of USD 200 per hour
```

### Traslada_ES_FR.py

```sh
python.exe .\Traslada_ES_FR.py
......
Texto en español: El producto tiene un valor de 200 USD por hora
Traducción en frances: Le produit a une valeur de 200 USD par heure
```
