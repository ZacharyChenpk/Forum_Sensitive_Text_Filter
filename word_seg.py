import pkuseg
from utils import sen_parse
import numpy as np
import os
import pickle

fileSegWordDonePath ='corpusSegDone.txt'
with open('../holes_github_dict.pkl','rb') as f:
    holes = pickle.load(f)
    
fileTrainRead = []
seg = pkuseg.pkuseg(model_name='web')
a=" "
fileTrainRead = [a.join(sen_parse(holes[d]['dz_text'], seg))+"\n" for d in holes]

with open(fileSegWordDonePath,'w',encoding='utf-8') as fW:
    fW.writelines(fileTrainRead)
