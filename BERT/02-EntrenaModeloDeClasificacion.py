import os
import numpy as np

# Instala e importa librerías de HuggingFace
# pip install transformers datasets seqeval

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import DataCollatorForTokenClassification, TrainingArguments, Trainer
from seqeval.metrics import f1_score, precision_score, recall_score

# 1) Carga el dataset desde un archivo JSON
#    Si tienes un solo archivo .json y lo usas todo como 'train', haz:
dataset = load_dataset("json", data_files="ejemplos.json", split="train")
# Si tuvieras varios archivos (ej: train, val):
# dataset = load_dataset("json", data_files={
#    "train": "my_ner_data_train.json",
#    "validation": "my_ner_data_val.json"
# })

# 2) Opcional: dividir en train/validation si tienes un único archivo
#    (por ejemplo, 80% train y 20% validación)
dataset = dataset.train_test_split(test_size=0.2)
train_dataset = dataset["train"]
val_dataset = dataset["test"]

print("Ejemplos de train:", train_dataset.num_rows)
print("Ejemplos de val:  ", val_dataset.num_rows)

# 3) Definir el mapeo de etiquetas a IDs
label2id = {
    "O": 0,
    "B-MONEDA": 1,
    "I-MONEDA": 2
}
id2label = {v: k for k, v in label2id.items()}

# 4) Cargar tokenizador y modelo base (BERT en español)
model_name = "dccuchile/bert-base-spanish-wwm-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 5) Función para tokenizar y alinear etiquetas
def tokenize_and_align_labels(examples):
    # Tokenizamos la lista de tokens, indicando que 'examples["tokens"]' ya es lista de strings
    tokenized_inputs = tokenizer(
        examples["tokens"], 
        truncation=True, 
        is_split_into_words=True
    )

    all_labels = []
    for i, labels in enumerate(examples["ner_tags"]):
        # labels es la lista de etiquetas (ej: ["O", "O", "B-MONEDA", ...])
        
        # 'word_ids' mapea cada subtoken al índice de palabra original
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                # sub-tokens especiales, ignorarlos en la pérdida
                label_ids.append(-100)
            else:
                # Convertimos la etiqueta string a su ID numérico
                label_ids.append(label2id[labels[word_idx]])
        all_labels.append(label_ids)

    # Añadimos 'labels' al diccionario
    tokenized_inputs["labels"] = all_labels

    return tokenized_inputs

# 6) Aplicar la función anterior con .map
train_tokenized = train_dataset.map(tokenize_and_align_labels, batched=True)
val_tokenized = val_dataset.map(tokenize_and_align_labels, batched=True)

# 7) Creamos el modelo para clasificación de tokens
model = AutoModelForTokenClassification.from_pretrained(
    model_name,
    num_labels=len(label2id),
    id2label=id2label,
    label2id=label2id
)

# 8) Creamos el data collator (maneja padding dinámico)
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

# 9) Definimos métrica para NER (F1, Precision, Recall con seqeval)
def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)

    true_predictions = [
        [id2label[pred] for (pred, lab) in zip(pred_row, lab_row) if lab != -100]
        for pred_row, lab_row in zip(predictions, labels)
    ]
    true_labels = [
        [id2label[lab] for (pred, lab) in zip(pred_row, lab_row) if lab != -100]
        for pred_row, lab_row in zip(predictions, labels)
    ]

    precision = precision_score(true_labels, true_predictions)
    recall = recall_score(true_labels, true_predictions)
    f1 = f1_score(true_labels, true_predictions)
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

# 10) Configuramos argumentos de entrenamiento
training_args = TrainingArguments(
    output_dir="bert_monedas_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=3,
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    logging_steps=10,
    load_best_model_at_end=True
)

# 11) Creamos el Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_tokenized,
    eval_dataset=val_tokenized,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

# 12) Entrenamos
trainer.train()

# 13) Guardamos el modelo y el tokenizador
trainer.save_model("bert_monedas_model")
tokenizer.save_pretrained("bert_monedas_model")

print("¡Entrenamiento finalizado y modelo guardado!")
