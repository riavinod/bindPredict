from pandas import DataFrame
import torch
import os
import numpy
import h5py
import random
from collections import defaultdict
import sys

embeddings = dict()
file = sys.argv[1]
with h5py.File(file, 'r') as f:
    for key, embedding in f.items():
        embeddings[key] = numpy.array(embedding, dtype=numpy.float32)
        print(embedding)
print(embeddings.keys())