from word_filter import AC_automation
from utils import sen_parse
import pickle
import os
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import pkuseg
import word2vec

w2v = word2vec.load('corpusWord2Vec.bin')
the_lstm = torch.load('lstm_1117')
the_lstm.batch_size = 1
seg = pkuseg.pkuseg(model_name='web')
the_filter = AC_automation()
with open('sensitive_words.pkl', 'rb') as f:
    wordlist = pickle.load(f)
for w in wordlist:
    the_filter.addword(w)
the_filter.make_backlink()

# Return the ban level of a given sentence
# 2: contain the sentitive words, should be blocked before post
# 1: detected by the lstm_model, administrator alerted
# 0: seem to be OK
def sen_detect(sen):
	if the_filter.words_replace(sen) != sen:
		return 2
	sen_seg = sen_parse(sen, seg)
	x = torch.tensor([w2v[w] if w in w2v.vocab else [0.]*300 for w in sen_seg], dtype=torch.float32).unsqueeze(0)
	y = the_lstm(x, [len(sen_seg)]).squeeze(0)
	if y[0]>y[1]:
		return 1
	return 0