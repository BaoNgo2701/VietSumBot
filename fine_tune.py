from transformers import BartForConditionalGeneration, BartTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
import logging

def fine_tune_model(train_dataset, eval_dataset):
    model_name = 'facebook/bart-large-cnn'
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    training_args = TrainingArguments(
        output_dir='./server/models/fine_tuned_model',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    trainer.train()

    # Save the model
    model.save_pretrained('./server/models/fine_tuned_model')
    tokenizer.save_pretrained('./server/models/fine_tuned_model')
    logging.info("Fine-tuning completed and model saved.")

def tokenize_function(examples):
    model_name = 'facebook/bart-large-cnn'
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model_inputs = tokenizer(examples["description"], max_length=512, truncation=True)

    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["summary"], max_length=128, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

if __name__ == '__main__':
    # Load datasets from JSON files
    train_dataset = load_dataset('json', data_files='./server/cleaned_data/train_data.json')['train']
    eval_dataset = load_dataset('json', data_files='./server/cleaned_data/eval_data.json')['train']  # using 'train' because load_dataset always returns a DatasetDict

    # Tokenize datasets
    train_dataset = train_dataset.map(tokenize_function, batched=True)
    eval_dataset = eval_dataset.map(tokenize_function, batched=True)

    fine_tune_model(train_dataset, eval_dataset)
