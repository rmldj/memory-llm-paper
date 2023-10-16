from memory import prepare_test

# experiment with Humpty Dumpty repeated variable number of times
# list of length 10, for comparison with interference experiments


variant = 'has-a'
query_type = 'direct'
length = 10

queries = []
ntot = 0
    
for distractor_length in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]:

    distractor_type = 100 + distractor_length 
    identifier = 'memory_{}_l{}_d{}_{}'.format(variant, length, distractor_type, query_type)
    test = prepare_test(variant, length, distractor_type, query_type)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

print('total number of queries', ntot)
print()
