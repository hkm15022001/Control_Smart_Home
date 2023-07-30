from sklearn.metrics import classification_report
from training_phobert import model, tokenizer, tags_set, device
import torch
import json
import numpy as np


with open('test_content.json', 'r', encoding="utf-8") as c:
    contents = json.load(c)

tags_test = []
X_test = []
y_test = []

for content in contents['intents']:
    tag = content['tag']
    for pattern in content['patterns']:
        X_test.append(pattern)
        tags_test.append(tag)

for tag in tags_test:
    label = tags_set.index(tag)
    y_test.append(label)
token_test = {}
token_test = tokenizer.batch_encode_plus(
    X_test,
    max_length=13,
    padding='max_length',
    truncation=True
)
X_test_mask = torch.tensor(token_test['attention_mask'])
X_test = torch.tensor(token_test['input_ids'])
y_test = torch.tensor(y_test)

path = 'saved_weights.pth'
model.load_state_dict(torch.load(path))
with torch.no_grad():
    preds = model(X_test.to(device), X_test_mask.to(device))
    preds = preds.detach().cpu().numpy()

preds = np.argmax(preds, axis=1)
# print(classification_report(y_test, preds))
