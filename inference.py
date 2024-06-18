from transformers import T5ForConditionalGeneration, T5Tokenizer
checkpoint_path = 'model'
checkpoint_path_tokenizer='tokenizer'

tokenizer = T5Tokenizer.from_pretrained(checkpoint_path)
model = T5ForConditionalGeneration.from_pretrained(checkpoint_path_tokenizer)
input_text = "Translate this sentence into French: Hello, how are you?"
input_ids = tokenizer.encode(input_text, return_tensors='pt')
output_ids = model.generate(input_ids, max_length=50, num_beams=4, early_stopping=True)
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("Input:", input_text)
print("Output:", output_text)
