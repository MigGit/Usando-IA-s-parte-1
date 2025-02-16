# Whisper
## _Ejemplo uso de Wisper_

En este ejemplo se presenta una trascripción y una traducción de un archivo de prueba MP3 de duración 18,3 Minutos

Para el ejemplo se utilizar el audio del video de 
[Carolina Rojas y Regina Lena - "Todo es negociable" Anímate/Anime-se +Liderazgo LATAM](https://www.youtube.com/watch?v=dtXoJIbhv_Y&t=504s)

## Detalle de modelo de Whisper

Para este ejemplo tener en cuenta la cantidad de memoria VRAM de la tarjeta grafica para su correcto funcionamiento se debe seleccionar el modelo según el detalle de la siguiente tabla:

| Modelo | Tamaño | GPU RAM |
| ------ | ------ | ------- |
|tiny|39M|2G VRAM|
|base|74M|4G VRAM|
|medium|139M|8G VRAM|
|large|295M|16G VRAM|
|mega|680M|32G VRAM|

## Requerimientos

Para este ejemplo se utilizó Python 3.11.9 y se deben instalar todas estas librerías

Actualizar el pip

```sh
python.exe -m pip install --upgrade pip
```
## Enviromen

Creación de ambiente de ejecución, para la carga de las librerías sin afectar el ambiente principal

```sh
python -m venv ejemplo_whisper
# Linux
    # Activa Enviroment
    source ejemplo_whisper/Scripts/activate 

# Windows
    # Activa Enviroment
    ejemplo_whisper\Scripts\activate.bat
    # Desactiva Enviroment
    ejemplo_whisper\Scripts\deactivate.bat
```

## Ejecucion del ejemplo 

Para poder ejecutar el ejemplo se requiere las siguientes librerías:

```sh
pip install openai-whisper
pip install numpy==1.26.0
```

## Para ejecutar Whisper en CMD
Para este ejemplo tenemos un archivo mp3 ("Todo_es_negociable.mp3" de 18 minutos de duración) para la prueba. El audio está en español.

Whisper traduce automáticamente al inglés. Los archivos quedarán en el directorio “traduccion”.

```sh
whisper "Todo_es_negociable.mp3" --model base --task translate --output_dir traduccion
```

Para transcribir a texto directamente. Los archivos quedaran en el directorio “transcripcion”.

```sh
whisper "Todo_es_negociable.mp3" --model base --task transcribe --output_dir transcripcion
```

## Ejemplo dos Mp3 pequeño

Modelo "base" Mp3 duracion 43 Segundo - Traduccion 12 segundos

```sh
whisper "Todo_es_negociable_muestra.mp3" --language es --model base --task translate --output_dir traduccion
```

Modelo "base" Mp3 duracion 43 Segundo - Traduccion 9 segundos

```sh
whisper "Todo_es_negociable_muestra.mp3" --language es --model base --task transcribe --output_dir transcripcion
```

## Para ejecutar Whisper en script python

Whisper traduce al inglés. Muestra por consola el resultado de la traducción.

```sh
python.exe .\01_EjemploTranslate.py
```

Para transcribir a texto. Muestra por consola el resultado de la trascripción.

```sh
python.exe .\02_EjemploTranscribe.py
```