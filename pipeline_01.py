from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

classifier = pipeline("sentiment-analysis")

result = classifier("This movie was great!", truncation=True)

print(result)

gpt = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(gpt)
tokenizer = AutoTokenizer.from_pretrained(gpt)

classifier = pipeline("sentiment-analysis")

result = classifier("This movie was great!", truncation=True)

print(result)
