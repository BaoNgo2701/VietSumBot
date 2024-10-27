from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained translation model
model_name = 'Helsinki-NLP/opus-mt-vi-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_vi_to_en(text):
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_text[0]

def detect_category(text):
    categories = ['Backpacks', 'Clothing', 'Stationery']
    text_lower = text.lower()
    for category in categories:
        if category.lower() in text_lower:
            return category
    return 'Unknown'