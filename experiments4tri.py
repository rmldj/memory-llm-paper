from memory import prepare_complex_test

# experiment with intervening second task
# additional cases for L=10,
# changes distractors to Humpty Dumpty *10


task1 = 'has-a'
task2 = 'is-a'
length = 10

queries = []
ntot = 0

seeds = [555, 666, 1621, 137, 0]

for seed in seeds:

    # reference (as in experiments4.py) 

    identifier = 'memory_complex2_{}_{}_l{}_seed{}'.format(task1, 'fillall', length, seed)
    test = prepare_complex_test(task1, 'fillall', length, 110, 110, adjacent=False, permute=False, seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

    # permuted task2 (as in experiments4.py)

    identifier = 'memory_complex2_{}_{}_l{}_seed{}'.format(task1, task2, length, seed)
    test = prepare_complex_test(task1, task2, length, 110, 110, adjacent=False, permute=True, seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

    # task2 with complementary names

    identifier = 'memory_complex2_complementary_{}_{}_l{}_seed{}'.format(task1, task2, length, seed)
    test = prepare_complex_test(task1, task2, length, 110, 110, adjacent=False, permute=True, complementary=True, seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)


    # task2 involving completely different facts

    identifier = 'memory_complex2_{}_{}_l{}_seed{}'.format(task1, 'independent', length, seed)
    test = prepare_complex_test(task1, 'independent', length, 110, 110, adjacent=False, permute=True, seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)


print('total number of queries', ntot)
print()
