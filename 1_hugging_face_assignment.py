from transformers import DistilBertTokenizer, DistilBertModel, pipeline
from datasets import load_dataset

data = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
text = data[10]["text"]
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-cased')
tokenized_sequence = tokenizer.tokenize(data[10]['text'])
sixth_token = tokenized_sequence[5]

# mask token
text = text.replace(sixth_token, "[MASK]", 1)

unmasker = pipeline('fill-mask', model='distilbert-base-cased')
unmasked = unmasker(text)
most_probable_predicted_token = unmasked[0]["token_str"]
print(most_probable_predicted_token)