from memory import prepare_test

# for quickly testing other models

query_type = 'direct'

queries = []
ntot = 0

seeds = [555, 666, 1621, 137, 0]

for seed in seeds:

    for variant in ['has-a']:
        for length in [20]:
            identifier = 'memory_{}_l{}_d1_{}_seed{}'.format(variant, length, query_type, seed)
            test = prepare_test(variant, length, 1, query_type, seed=seed)
            queries.append( (identifier, test) )
            print(identifier)
            ntot += len(test)


print('total number of queries', ntot)
print()

