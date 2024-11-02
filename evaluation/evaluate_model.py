# evaluate_model.py
import json
from evaluation.evaluate_rouge import evaluate_rouge_scores

# Function to load and evaluate summaries
def evaluate_summaries(reference_path, hypothesis_path):
    with open(reference_path, 'r', encoding='utf-8') as ref_file:
        reference_summaries = json.load(ref_file)
    
    with open(hypothesis_path, 'r', encoding='utf-8') as hyp_file:
        generated_summaries = json.load(hyp_file)
    
    all_scores = []
    for ref, hyp in zip(reference_summaries, generated_summaries):
        scores = evaluate_rouge_scores(ref['summary'], hyp['summary'])
        all_scores.append(scores)
    
    return all_scores

if __name__ == '__main__':
    reference_path = 'path_to_reference_summaries.json'
    hypothesis_path = 'path_to_generated_summaries.json'
    scores = evaluate_summaries(reference_path, hypothesis_path)
    print(scores)
