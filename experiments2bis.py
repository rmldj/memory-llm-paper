from memory import prepare_test

# experiment with adding elaborations in three places in the list of length 19
# in order to gather statistics, we repeat the experiment with 5 random seeds


variant = 'has-a'
query_type = 'direct'
length = 19

queries = []
ntot = 0

seeds = [555, 666, 1621, 137, 0]

for seed in seeds:
    
    identifier = 'memory_{}_l{}_d1_{}_seed{}'.format(variant, length, query_type, seed)
    test = prepare_test(variant, length, 1, query_type, seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

    identifier = 'memory_{}_l{}_d1_{}_seed{}_elaborate5-10-15'.format(variant, length, query_type, seed)
    test = prepare_test(variant, length, 1, query_type, elaborate=[5, 10, 15], seed=seed)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

print('total number of queries', ntot)
print()
