import os

def read_txt_files(folder_path):
    files = os.listdir(folder_path)
    data = []
    for file in files:
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            data.append(f.read())
    return data

def clean_text(text):
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text

def normalize_text(text):
    return text.lower()

def preprocess_texts(texts):
    return [normalize_text(clean_text(text)) for text in texts]

def save_cleaned_data(category, texts):
    base_path = f'server/cleaned_data/{category}'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for i, text in enumerate(texts):
        file_path = os.path.join(base_path, f'cleaned_{i}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

if __name__ == '__main__':
    categories = ['Backpacks', 'Clothing', 'Stationery']
    for category in categories:
        folder_path = f'server/product_data/{category}'
        texts = read_txt_files(folder_path)
        cleaned_texts = preprocess_texts(texts)
        save_cleaned_data(category, cleaned_texts)
