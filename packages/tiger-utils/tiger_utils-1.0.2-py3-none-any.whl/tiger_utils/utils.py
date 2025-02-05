import pickle
import json
from collections import OrderedDict
from itertools import chain
import torch

def dedup_list(ls):
  return list(OrderedDict.fromkeys(ls))

def concat(ls):
  return list(chain.from_iterable(ls))

def read_json(fn):
  with open(fn) as f:
    return json.load(f)

def write_json(obj, fn):
  with open(fn, 'w') as f:
    json.dump(obj, f, indent=2)

def read_pickle(fn):
  with open(fn, 'rb') as f:
    return pickle.load(f)

def write_pickle(r, fn):
  with open(fn, 'wb') as f:
    pickle.dump(r, f)

def cosine_sim(A, B):
  # Normalize A and B row-wise
  A_norm = A / A.norm(dim=1, keepdim=True)
  B_norm = B / B.norm(dim=1, keepdim=True)

  # Compute cosine similarity: A_norm @ B_norm.T
  cosine_sim = torch.mm(A_norm, B_norm.T)

  return cosine_sim