from sklearn.metrics import classification_report
import torch
import json
import numpy as np
from phobert_finetuned import PhoBERT_finetuned
from transformers import AutoModel,AutoTokenizer
import random

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load train and validation dataset
with open('content.json', 'r', encoding="utf-8") as c:
    contents = json.load(c)

tags = []
X = []


for content in contents['intents']:
    tag = content['tag']
    for pattern in content['patterns']:
        X.append(pattern)
        tags.append(tag)

tags_set = sorted(set(tags))

num_class = len(tags_set)
hidden_size = 512
phobert = AutoModel.from_pretrained('vinai/phobert-base')
tokenizer = AutoTokenizer.from_pretrained('vinai/phobert-base')
model = PhoBERT_finetuned(phobert, hidden_size=hidden_size,
                          num_class=num_class)
# model = model.to(device)

with open('test_content.json', 'r', encoding="utf-8") as c:
    contents = json.load(c)

path = 'saved_weights.pth'
model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))


#func to predict input
def predict_PhoBERT(sentence):
    token = tokenizer(sentence, max_length=13, padding='max_length',
                      truncation=True)
    X_mask = torch.tensor([token['attention_mask']])
    X = torch.tensor([token['input_ids']])
    with torch.no_grad():
        preds = model(X, X_mask)
    preds = torch.argmax(preds, dim=1)
    tag = tags_set[preds.item()]
    for content in contents['intents']:
        if tag == content['tag']:
            answer = random.choice(content['responses'])
    return answer

