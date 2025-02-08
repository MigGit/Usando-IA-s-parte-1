# BERT
## Ejemplo de uso de BERT

Este repositorio contiene 2 tipos de ejemplo con BART.
 - Clasificación de sentimientos.
 - Clasificación de patrones.

## Requerimientos

Para este ejemplo se utilizó Python 3.11.9 y se deben instalar todas estas librerías

Actualizar el pip

```sh
python.exe -m pip install --upgrade pip
```
## Enviromen

Creación de ambiente de ejecución, para la carga de las librerías sin afectar el ambiente principal

```sh
python -m venv ejemple_bert
# Linux
    # Activa Enviroment
    source ejenplo_bert/Scripts/activate 

# Windows
    # Activa Enviroment
    ejenplo_bert\Scripts\activate.bat
    # Desactiva Enviroment
    ejenplo_bert\Scripts\deactivate.bat
```

## Ejemplos
### 01-Clasificaci0n_Sentimientos.py

Ejemplo de clasificación de sentimientos usando BERT, para poder correr correctamente el código se réquiem las siguientes librerías:

```sh
pip install torch
pip install transformers
```

Una vez que ejecuta nos muestra un resumen con los 3 ejemplos y su clasificación donde 0 es muy negativo y 1 es muy positivo

```sh
python .\01-Clasificaci0n_Sentimientos.py

Device set to use cpu
Texto: Este producto es increíble, me encanta.
Resultado: {'label': '5 stars', 'score': 0.8997379541397095}

Texto: No me gustó la experiencia, el servicio fue pésimo.
Resultado: {'label': '1 star', 'score': 0.6251131892204285}

Texto: No quiero saber nada más de su producto
Resultado: {'label': '1 star', 'score': 0.3365054130554199}
```


### 02-EntrenaModeloDeClasificacion.py

Ejemplo de reconocimiento de patrones con BERT, El entrenamiento del modelo básicamente reconoce el valor en dólares de una frase, para poder ejecutar se requiere las siguientes librerías:

```sh
pip install torch
pip install transformers
pip install datasets seqeval
pip install accelerate>=0.26.0
```

Una vez que se ejecuta correctamente, genera un directorio *bert_monedas_model* con él fine tune de BERT.

### 03-UsoModeloDeClasificacion.py

Uso de modelo preentrenado para detectar patrones de moneda dólar, para ejecutar se requiere la siguiente librería:

```sh
pip install transformers
```

Una vez que se ejecuta correctamente, muestra una lista con los valores encontrados (para el ejemplo 1 dato)

```sh
python.exe .\03-UsoModeloDeClasificacion.py

Device set to use cpu
-------------------
[{'entity_group': 'MONEDA', 'score': np.float32(0.44992995), 'word': '200 USD', 'start': 30, 'end': 37}]
-------------------
```

## 04-UsoModeloDeClasificacionGPU.py GPU

Para uso de GPU en la clasificación se deben instalar las siguientes librerías: 

```sh
pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install numpy==1.26.0
```

Una vez que se ejecuta correctamente, muestra una lista con los valores encontrados (para el ejemplo 1 dato)


```sh
python.exe .\04-UsoModeloDeClasificacionGPU.py
.....
Device set to use cuda:0
-------------------
[{'entity_group': 'MONEDA', 'score': 0.44992998, 'word': '200 USD', 'start': 30, 'end': 37}]
-------------------
```

