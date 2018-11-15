import os
import re
from glob import glob
from tqdm import tqdm
import numpy as np
import pandas as pd
import ast
import matplotlib.pyplot as plt
fnames = glob('/Users/erictang/Desktop/Github/DoogleDrawing/train_simplified/*.csv')
cnames = ['countrycode', 'drawing', 'key_id', 'recognized', 'timestamp','word']
drawlist = []
firstFive = pd.read_csv(fnames[0],nrows = 1) 
firstOne = firstFive[firstFive.recognized==True].head(1)
print(firstFive)
print(firstOne)