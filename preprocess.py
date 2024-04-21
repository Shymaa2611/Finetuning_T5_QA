import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re


nltk.download('punkt')
nltk.download('stopwords')

def preprocess_data():
   with open('questions_answers.json', 'r') as f:
     data = json.load(f)


     ps = PorterStemmer()
     stop_words = set(stopwords.words('english'))


     processed_data = []
     for item in data:
       question = item['question']
       answer = item['answer']
       context = item['context']

       question = question.lower()
       answer = answer.lower()
       context = context.lower()
       question = re.sub(r'http\S+', '', question)
       question = re.sub(r'\d+', '', question)
       question = re.sub(r'[^\w\s]', '', question)

       answer = re.sub(r'http\S+', '', answer)
       answer = re.sub(r'\d+', '', answer)
       answer = re.sub(r'[^\w\s]', '', answer)

       context = re.sub(r'http\S+', '', context)
       context = re.sub(r'\d+', '', context)
       context = re.sub(r'[^\w\s]', '', context)
       question_tokens = word_tokenize(question)
       answer_tokens = word_tokenize(answer)
       context_tokens = word_tokenize(context)
       question_filtered = [ps.stem(word) for word in question_tokens if word not in stop_words]
       answer_filtered = [ps.stem(word) for word in answer_tokens if word not in stop_words]
       context_filtered = [ps.stem(word) for word in context_tokens if word not in stop_words]
       question_processed = ' '.join(question_filtered)
       answer_processed = ' '.join(answer_filtered)
       context_processed = ' '.join(context_filtered)

       processed_data.append({
        'question': question_processed,
        'answer': answer_processed,
        'context': context_processed
    })

   with open('questions_answers.json', 'w') as f:
       json.dump(processed_data, f, indent=4)

   print("Processed data saved to processed_data.json")
