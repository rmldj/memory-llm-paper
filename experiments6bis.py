from memory import prepare_complex_test

# experiment with repeated task in various configurations
# modified so to use 10x Humpty Dumpty

task1 = 'has-a'



queries = []
ntot = 0

# for completeness - should be already computed in experiments4.py
for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_{}_{}_l{}'.format(task1, 'fillall', length)
    test = prepare_complex_test(task1, 'fillall', length, 110, 1, adjacent=False, permute=False)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_adjacent_{}_{}_l{}'.format(task1, 'fillall', length)
    test = prepare_complex_test(task1, 'fillall', length, 110, 1, adjacent=True, permute=False)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

# repeated task

for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_{}_{}_l{}'.format(task1, 'repeated', length)
    test = prepare_complex_test(task1, task1, length, 110, 1, adjacent=False, permute=False)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_{}_{}_l{}'.format(task1, 'permuted', length)
    test = prepare_complex_test(task1, task1, length, 110, 1, adjacent=False, permute=True)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)


for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_adjacent_{}_{}_l{}'.format(task1, 'repeated', length)
    test = prepare_complex_test(task1, task1, length, 110, 1, adjacent=True, permute=False)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

for length in range(7, 21, 2):
    
    identifier = 'memory_complex2_adjacent_{}_{}_l{}'.format(task1, 'permuted', length)
    test = prepare_complex_test(task1, task1, length, 110, 1, adjacent=True, permute=True)
    queries.append( (identifier, test) )
    print(identifier)
    ntot += len(test)

print('total number of queries', ntot)
print()
