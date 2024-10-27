from transformers import MarianMTModel, MarianTokenizer
import torch

# Load pre-trained translation model
model_name = 'Helsinki-NLP/opus-mt-vi-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_vi_to_en(text):
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_text[0]
