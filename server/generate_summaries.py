import json
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

# Load the fine-tuned model
model_name = 'Bao1340/vietsum_finetune'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

# Generate summaries for the descriptions in reference_summaries.json
def generate_summaries(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        description = item['description']
        summary = summarizer(description, max_length=60, min_length=30, do_sample=False)[0]['summary_text']
        item['summary'] = summary
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Saved generated summaries to {output_file}")

# Create generated_summaries.json from reference_summaries.json
generate_summaries('./server/cleaned_data/reference_summaries.json', './server/summaries/generated_summaries.json')
