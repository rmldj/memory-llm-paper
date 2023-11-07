# Memory characteristics of Large Language Models

This repository contains code which can be used to perform the experiments reported in the paper and generate figures

Romuald A. Janik, *Aspects of human memory and Large Language Models*, arXiv:2311.XXXXX


## Code organization
 
`memory.py` contains the key definitions and functions for setting up all the experiments. The files with names like `experiments1default.py` contain definitions of all queries necessary for performing a given experiment. The outputs of all experiments are saved in the directory `DIR` defined in `utils.py` (default `../results`).

The experiments are ran on GPT-J writing e.g.
```
python run_experiments.py experiments1default
```
and on a model from the pythia family
```
python run_experiments_pythia.py 6.9B experiments1default
```
If the output file already exists, the subexperiment is skipped.

`summarize.py` and `errors.py` are diagnostic scripts which we describe at the very end, together with some more information.

In the following we describe the code necessary for reproducing figures from the paper.

## Run all experiments

```
./RUN_ALL
```
This takes about 5 hours on an NVIDIA V100 GPU. Requires 32Gb GPU memory.


## Figures 1, 3 and 4

Run experiments (if necessary):
```
python run_experiments.py experiments1bis
./RUN_PYTHIA
```
Generate figures:
```
python plot_glanzer_cunitz.py  # Fig. 1
python plot_overall23bis.py    # Fig. 3
python plot_pythia2.py         # Fig. 4
```
The Fig. S1 in the Supplementary information shows the prior `v0` versions of the Pythia models, which exhibit a much more stable recency effect than the updated versions.
```
./RUN_PYTHIAv0
python plot_pythia2v0.py         # Fig. S1
```


## Figure 5

`experiments2bis` and
```
python plot_elaborations.py
```

## Figure 6

`experiments3tri` and
```
python plot_humpty_dumpty.py
```

## Figure 7

`experiments4tri` and
```
python plot_interference2.py
```

## Figure 8

`experiments6bis` and
```
python plot_repetitions2.py
```

## Further information

Each experiment file like `experiments1default.py` contains a series of subexperiments denoted by identifiers. One can see the identifiers by writing
```
memory-llm-paper $ python experiments1default.py 
memory_has-a_l20_d1_direct_seed555
memory_has-a_l20_d1_direct_seed666
memory_has-a_l20_d1_direct_seed1621
memory_has-a_l20_d1_direct_seed137
memory_has-a_l20_d1_direct_seed0
total number of queries 3000

```
The outputs are written as arrays with names like `memory_has-a_l20_d1_direct_seed555_SUFFIX.npz`, where the `SUFFIX` stands for `original` (meaning GPT-J) or e.g. `pythia-6.9B` or `pythiav0-6.9B`.

The arrays contain for each query in the subexperiment the probabilities of each token. One can see the accuracies for each position on the list by writing
```
python summarize.py ../results/memory_has-a_l20_d1_direct_seed555_original.npz 
memory_has-a_l20_d1_direct_seed555_original.npz

mean accuracy 0.342+-0.075
number of correct words 6.83+-1.51

accuracy at position 1: 1.000
accuracy at position 2: 0.933
accuracy at position 3: 0.600
accuracy at position 4: 0.500
accuracy at position 5: 0.233
accuracy at position 6: 0.300
accuracy at position 7: 0.167
accuracy at position 8: 0.167
accuracy at position 9: 0.167
accuracy at position 10: 0.100
accuracy at position 11: 0.133
accuracy at position 12: 0.133
accuracy at position 13: 0.233
accuracy at position 14: 0.200
accuracy at position 15: 0.133
accuracy at position 16: 0.167
accuracy at position 17: 0.133
accuracy at position 18: 0.367
accuracy at position 19: 0.567
accuracy at position 20: 0.600
```
The errors made e.g. at position 3 (for each of the 30 repetitions appearing in that experiment) can be read off using
```
python errors.py ../results/memory_has-a_l20_d1_direct_seed555_original.npz 3
memory_has-a_l20_d1_direct_seed555_original.npz
position 3

      2  bike | bike
ERROR 22  Ford | bicycle car bike cat dog house camera brother Ford
ERROR 42  laptop | boat car laptop
      62  house | house
      82  sister | sister
ERROR 102  bike | sister cat brother dog bike
ERROR 122  Ford | boat sister car cat brother dog friend ______ lot Ford
      142  sister | sister
      162  sister | sister
      182  cat | cat
ERROR 202  Porsche | Mercedes sister brother car dog Porsche
ERROR 222  keyboard | cat guitar car dog trumpet brother piano sister bicycle bike
      242  sister | sister
      262  Porsche | Porsche
ERROR 282  laptop | dog bike laptop
      302  boat | boat
      322  trumpet | trumpet
      342  cat | cat
      362  piano | piano
ERROR 382  Toyota | car violin dog Toyota
      402  sister | sister
      422  camera | camera
      442  camera | camera
      462  brother | brother
ERROR 482  Porsche | dog camera car Porsche
ERROR 502  trumpet | cat dog trumpet
      522  Mercedes | Mercedes
ERROR 542  guitar | dog guitar
ERROR 562  Porsche | cat piano car Porsche
      582  dog | dog

```
where the top ranking nouns (at most 10) are listed up to the correct answer. The repetitions are obtained by permuting independently all names and objects and restricting the number of facts to the desired length of the list.

