import torch
from transformers import GPTNeoXForCausalLM, AutoTokenizer
import time
import pickle as pkl
import os
from time import time

import numpy as np

from pythia import pythia_variants, pythia_output_size, pythia

from utils import DIR

import importlib

import sys

if len(sys.argv)<3:
    print('usage: python run_experiments_pythia.py pythia_variant module_name')
    print('module_name.py contains definition of queries')
    print('pythia_variant is one of the variants defined in pythia.py')
    quit()

pythia_variant = sys.argv[1]
module_name = sys.argv[2]
assert pythia_variant in pythia_variants
print('pythia-{} + {}'.format(pythia_variant, module_name))
print()


queries = getattr(importlib.import_module(module_name), 'queries')

model = GPTNeoXForCausalLM.from_pretrained('EleutherAI/pythia-{}-v0'.format(pythia_variant))
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/pythia-{}-v0'.format(pythia_variant))
if pythia_variant not in ['12B']:
    model.cuda()

def run_query(query):
    input_ids = tokenizer(query, return_tensors='pt').input_ids
    with torch.no_grad():
        output = model(input_ids.to(model.device))
    ps = torch.softmax(output.logits[0], 1).cpu().numpy()
    token_probablities = ps[-2] # we are predicting the last token in query
    return token_probablities


if __name__ == "__main__":

    savepath = DIR #'/storage_0/romuald/PRACA/MEMORY/results'
    os.makedirs(savepath, exist_ok=True)

    output_size = pythia_output_size(pythia_variant)

    t0 = time()
    for prefix, lst in queries:
        fname = f"{savepath}/{prefix}_pythiav0-{pythia_variant}.npz"
        if os.path.exists(fname):
            print('{} | file exists, skipping...'.format(prefix))
            continue

        n = len(lst)
        out = np.zeros((n, output_size), dtype = np.float32)
        answers = np.zeros(n, dtype=int)
        sumprob = 0
        for i in range(n):
            query, answer = lst[i]
            probs = run_query(query)
            out[i, :] = probs
            answers[i] = answer
            sumprob += probs[pythia[answer]]
        print('{} | {:.4f}'.format(prefix, sumprob/n))
        np.savez_compressed(fname, probs=out, answers=answers)

    print('--------- {:.2f}s'.format(time()-t0))

    print("Finished processing!")



