import json
import re

def preprocess_data(data):
    processed_data = []
    for item in data:
        question = item['question']
        answer = item['answer']
        context = item['context']
        context = re.sub(r'http\S+', '', context)  
        context = re.sub(r'\d+', '', context)     
        context = re.sub(r'[^\w\s]', '', context) 
        context = context.replace('\n', '')        
        processed_data.append({
            'question': question,
            'answer': answer,
            'context': context
        })
    return processed_data
