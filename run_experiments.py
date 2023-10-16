import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import pickle as pkl
import os
from time import time

import numpy as np

from utils import DIR

import importlib

import sys

if len(sys.argv)<2:
    print('usage: python run_experiments.py module_name')
    print('module_name.py contains definition of queries')
    quit()

module_name = sys.argv[1]
print('original network +', module_name)
print()

queries = getattr(importlib.import_module(module_name), 'queries')

model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model.cuda()

def run_query(query):
    input_ids = tokenizer(query, return_tensors="pt").input_ids
    with torch.no_grad():
        output = model(input_ids.to(model.device))
    ps = torch.softmax(output.logits[0], 1).cpu().numpy()
    token_probablities = ps[-2] # we are predicting the last token in query
    return token_probablities


if __name__ == "__main__":

    savepath = DIR #'/storage_0/romuald/PRACA/MEMORY/results'
    os.makedirs(savepath, exist_ok=True)
    
    t0 = time()
    for prefix, lst in queries:
        fname = f"{savepath}/{prefix}_original.npz"
        if os.path.exists(fname):
            print('{} | file exists, skipping...'.format(prefix))
            continue

        n = len(lst)
        out = np.zeros((n, 50400), dtype = np.float32)
        answers = np.zeros(n, dtype=int)
        sumprob = 0
        for i in range(n):
            query, answer = lst[i]
            probs = run_query(query)
            out[i, :] = probs
            answers[i] = answer
            sumprob += probs[answer]
        print('{} | {:.4f}'.format(prefix, sumprob/n))
        np.savez_compressed(fname, probs=out, answers=answers)

    print('--------- {:.2f}s'.format(time()-t0))

    print("Finished processing!")



