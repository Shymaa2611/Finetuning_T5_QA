## T5 (Question-Answering)
 - T5, or Text-to-Text Transfer Transformer, is a Transformer based architecture that uses a 
   text-to-text approach. Every task – including translation, question answering, and classification – is cast as feeding the model text as input and training it to generate some target text. This allows for the use of the same model, loss function, hyperparameters, etc. across our diverse set of tasks.



![T5](t5.jpg)

## Dataset
 - dataset is collection of books and slids that related with computer science and information 
   system fields . 

 
## Technologies

 - python
 - torch
 - pytorch_lighting
 - T5 Large
 - transformers
 - scikit-learn


## Create dataset 
 - run create_data.ipynb

## Checkpoint

## Preprocessing
 - pip install data.py

## Train
 - git clone https://github.com/Shymaa2611/Finetuning_T5_QA.git
 - cd Finetuning_T5_QA
 - pip install -r requirements.txt
 - python data.py
 - python train.py


 ## Inference
 - python inference.py
