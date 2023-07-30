import torch.nn as nn
from transformers import AutoModel

class PhoBERT_finetuned(nn.Module):
    def __init__(self, phobert, hidden_size, num_class):
        super(PhoBERT_finetuned, self).__init__()
        self.phobert = phobert
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
        self.layer1 = nn.Linear(768, hidden_size)
        self.layer2 = nn.Linear(hidden_size, num_class)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, sent_id, mask):
        outputs = self.phobert(sent_id, attention_mask=mask)
        cls_hs = outputs.pooler_output
        x = self.layer1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.layer2(x)
        x = self.softmax(x)
        return x