from MyDataset import CustomTranslationDataset
# 加载数据集
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
train_dataset = CustomTranslationDataset("datas/train.csv")
test_dataset = CustomTranslationDataset("datas/test.csv")

# model_path = "Helsinki-NLP/opus-mt-en-zh"
model_path = "fine-tuned-model/last"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def collate_fn(batch):
    sources = [item["input_ids"] for item in batch]
    targets = [item["labels"] for item in batch]
    
    # 编码输入（英文）和输出（中文）
    inputs = tokenizer(sources, truncation=True, padding="max_length", return_tensors="pt", max_length=128)
    labels = tokenizer(text_target=targets, truncation=True, padding="max_length", return_tensors="pt", max_length=128)
    
    return {
        "input_ids": inputs.input_ids,
        "attention_mask": inputs.attention_mask,
        "labels": labels.input_ids
    }

from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./fine-tuned-model",
    num_train_epochs=8,
    per_device_train_batch_size=160,
    per_device_eval_batch_size=160,
    save_strategy="epoch",
    learning_rate=3e-5,
    evaluation_strategy="epoch", 
    logging_steps=500,
    load_best_model_at_end=True,
    metric_for_best_model="loss",
)

from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collate_fn,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

trainer.train()
model.save_pretrained("./fine-tuned-model/last")
tokenizer.save_pretrained("./fine-tuned-model/last")
