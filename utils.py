import pickle
import os
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import pkuseg

def sen_parse(raw_sen, seg):
    text = seg.cut(raw_sen.replace("\\", "").replace("\'", "").replace('/', '').replace('"', '').replace(',', '').replace('.', '').replace('?', '').replace('(', '').replace(')', '').replace(" ", "").replace("，", "").replace("。", "").replace("…", "").replace("“", "").replace("”", "").replace("（", "").replace("）", "").replace("#MISSED","").replace("#DELETED","").replace("—","").replace("\x00",""))
    return text

class hole_dzdataset(Dataset):
    def __init__(self, pos, neg, batch_size, word2vec_model):
        self.batch_size = batch_size
        print('A')
        self.x_word = pos+neg
        self.x_lens = torch.tensor([len(s) for s in self.x_word], requires_grad=False)
        self.x = [torch.tensor([word2vec_model[w] if w in word2vec_model.vocab else [0.]*300 for w in s], requires_grad=False, dtype=torch.float32) for s in self.x_word]
        self.y = torch.tensor([[0.,1.]]*len(pos) + [[1.,0.]]*len(neg), requires_grad=False, dtype=torch.float32)
        self.len = len(self.x_lens)
        
    def __getitem__(self, index):
        return self.x[index], self.x_lens[index], self.y[index]

    def __len__(self):
        return self.len
    
def split_train(data,test_ratio):
    shuffled_indices=np.random.permutation(len(data))
    test_set_size=int(len(data)*test_ratio)
    test_indices =shuffled_indices[:test_set_size]
    train_indices=shuffled_indices[test_set_size:]
    return data[train_indices],data[test_indices]

def collate_fn(X_batch):
    z = list(zip(*X_batch))
    return [z[0]]+[torch.utils.data.dataloader.default_collate(a) for a in z[1:]]

class lstm_model(nn.Module):
    def __init__(self, emb_size, batch_size):
        super().__init__()
        self.rnn = nn.LSTM(emb_size, emb_size)
        self.score = nn.Sequential(
            nn.Linear(emb_size, 10),
            nn.ReLU(True),
            nn.Linear(10, 2),
            nn.Softmax()
        )
        self.batch_size = batch_size
        
    def forward(self, X_batch, len_batch):
        assert(len(X_batch)==self.batch_size)
        assert(len(len_batch)==self.batch_size)
        
        #new_length, new_length_idx = torch.sort(len_batch, descending=True) 
        longest_l = max(len_batch)
        #_, re_new_idx = torch.sort(new_length_idx) 
        #new_X = X_batch.index_select(1,new_length_idx) 
        train_data = nn.utils.rnn.pad_sequence(X_batch, batch_first=True, padding_value=0)
        pad_data = nn.utils.rnn.pack_padded_sequence(train_data, len_batch, batch_first=True, enforce_sorted=False) 
        output, (h_n, c_n) = self.rnn(pad_data) 
        h_n = h_n.squeeze(0)
        # h_n: bsz * emb_size
        scores = self.score(h_n)
        # scores: bsz * 2
        return scores
    
def test_eval(test_dataloader, the_lstm, require_y_pre=False):
    total_cnt = 0
    correct_cnt = 0
    for i,(x,lens,y) in enumerate(train_dataloader):
        ans = y.argmax(dim=1)
        y_predict = the_lstm(x, lens)
        predict = y_predict.argmax(dim=1)
        total_cnt = total_cnt + ans.size(0)
        for i in range(ans.size(0)):
            if ans[i]==predict[i]: correct_cnt = correct_cnt + 1
        if require_y_pre:
            print(y, y_predict)
    return correct_cnt / total_cnt

if __name__ == '__main__':
    import word2vec
    model = word2vec.load('corpusWord2Vec.bin')
    ds = hole_dzdataset([['贵校','隔壁','保研'],['保研','百讲']], [['清华','北大'],['中华','人民','共和国']], 2, model)
    the_lstm = lstm_model(300, 2)
    optimizer = torch.optim.SGD(the_lstm.parameters(), lr = 0.01, momentum = 0.9)
    loss_fn = torch.nn.MSELoss()
    train_dataloader = DataLoader(dataset = ds,
                              batch_size = 2,
                              drop_last = False,
                              collate_fn=collate_fn)
    for epoch in range(200):
        for i,(x,lens,y) in enumerate(train_dataloader):
            optimizer.zero_grad()
            y_predict = the_lstm(x, lens)
            loss = loss_fn(y_predict, y)
            loss.backward()
            optimizer.step()
        print(test_eval(train_dataloader, the_lstm, require_y_pre=True))