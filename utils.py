import pickle
import os
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch import Dataset

class hole_dataset(Dataset):
	def __init__(self, all_dict, good_pids, bad_pids, batch_size)