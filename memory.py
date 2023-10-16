import numpy as np


token = dict()

token['Dublin'] = 18220
token['Copenhagen'] = 31104
token['Budapest'] = 40959
token['Warsaw'] = 32955
token['Madrid'] = 14708
token['Stockholm'] = 29679
token['Tokyo'] = 11790   
token['Sydney'] = 11852   
token['Delhi'] = 12517   
token['Seattle'] = 7312    
token['Havana'] = 40274   
token['Cairo'] = 23732   

token['Melbourne'] = 14819  
token['Chicago'] = 4842  
token['Lisbon'] = 41898  
token['Honolulu'] = 43296  
token['Seoul'] = 22372  
token['Rome'] = 10598  
token['Athens'] = 21891  
token['Manila'] = 31721  



lives_in = np.array(['Dublin', 'Copenhagen', 'Budapest', 'Warsaw', 'Madrid', 'Stockholm',
                   'Tokyo', 'Sydney', 'Delhi', 'Seattle', 'Havana', 'Cairo',
                   'Melbourne', 'Chicago', 'Lisbon', 'Honolulu',
                   'Seoul', 'Rome', 'Athens', 'Manila']) 

#token['car'] = 1097
token['bike'] = 7161
token['cat'] = 3797
token['dog'] = 3290
token['guitar'] = 10047
token['piano'] = 19132
token['camera'] = 4676    
token['laptop'] = 13224   
token['motorcycle'] = 18757   
token['house'] = 2156    
token['sister'] = 6621    
token['brother'] = 3956    


token['trumpet'] = 40334  
token['keyboard'] = 10586  
token['violin'] = 38283  
token['Toyota'] = 20182  
token['Porsche'] = 28367  
token['Ford'] = 8092  
token['Mercedes'] = 21279  
token['horse'] = 8223  
token['boat'] = 8848  


has_a = np.array(['bike', 'cat', 'dog', 'guitar', 'piano',
                'camera', 'laptop', 'motorcycle', 'house', 'sister', 'brother',
                'trumpet', 'keyboard', 'violin', 'Toyota', 'Porsche',
                'Ford', 'Mercedes', 'horse', 'boat'])

elaborations = dict()
elaborations['bike'] = ', on which {} drives to work each day. '
elaborations['cat'] = ', which passionately likes to play with a ball. '
elaborations['dog'] = ', called Fido who just adores catching his rope toy. '
elaborations['guitar'] = ', an electric one, on which {} plays in a local garage band. '
elaborations['piano'] = ', which unfortunately is a bit out of tune. '
elaborations['camera'] = ', a quite heavy full-frame digital SLR with a couple of lenses. '
elaborations['laptop'] = ', which is covered with all kinds of stickers. '
elaborations['motorcycle'] = ', not a Harley-Davidson but rather an unasuming model which easily blends in. '
elaborations['house'] = ', situated in large garden in a nice quiet part of the town. '
elaborations['sister'] = ', who is much younger, so they did not overlap at high school. '
elaborations['brother'] = ', who went to school one year earlier, so school was a familiar ground. '
elaborations['trumpet'] = ', on which {} regularly plays each weekend in the local jazz club. '
elaborations['keyboard'] = ', on which {} tries to practice reading notes and playing standards. '
elaborations['violin'] = ', on which {} tries to practice every morning to the dismay of neighbors. '
elaborations['Toyota'] = ', an old model bought quite cheaply at a second-hand outlet. '
elaborations['Porsche'] = ', painted red, almost matching the stereotypical image. '
elaborations['Ford'] = ', a sturdy pickup truck, very useful for the gardening business. '
elaborations['Mercedes'] = ', which so far has been very reliable, but now some minor problems start to surface. '
elaborations['horse'] = ', which is kept on a farm just a few miles north of the city. '
elaborations['boat'] = ', really a small dinghy, used for fishing on the lake. '


token['biologist'] = 35261   
token['driver'] = 4639    
token['farmer'] = 18739   
token['mathematician'] = 48251   
token['physicist'] = 33013   
token['programmer'] = 24292   
token['journalist'] = 10099   
token['lawyer'] = 6853    
token['doctor'] = 6253    
token['surgeon'] = 23923   
token['psychologist'] = 23540   
token['politician'] = 14971   

token['nurse'] = 15849  
token['teacher'] = 4701  
token['writer'] = 6260  
token['soldier'] = 10686  
token['pilot'] = 8022  
token['baker'] = 46412  
token['painter'] = 34537  
token['musician'] = 21623  


is_a = np.array(['biologist', 'driver', 'farmer', 'mathematician', 'physicist', 'programmer',
                'journalist', 'lawyer', 'doctor', 'surgeon', 'psychologist', 'politician',
                'nurse', 'teacher', 'writer', 'soldier', 
                'pilot', 'baker', 'painter', 'musician'])

token['Paul'] = 3362    
token['Helen'] = 22695   
token['Ann'] = 5506    
token['Mary'] = 5335    
token['David'] = 3271    
token['Mark'] = 2940    
token['Michael'] = 3899    
token['Susan'] = 14919   
token['Robert'] = 5199    
token['Peter'] = 5613    
token['Christine'] = 26088   
token['Sarah'] = 10490   

token['Ivan'] = 21798  
token['Charlotte'] = 14685  
token['Pierre'] = 21204  
token['Catherine'] = 22578  
token['Audrey'] = 48498  
token['John'] = 1757  
token['Amanda'] = 23040  
token['Kevin'] = 7939  


persons = np.array(['Paul', 'Helen', 'Ann', 'Mary', 'David', 'Mark',
                'Michael', 'Susan', 'Robert', 'Peter', 'Christine', 'Sarah',
                'Ivan', 'Charlotte', 'Pierre', 'Catherine',
                'Audrey', 'John', 'Amanda', 'Kevin'])

pronoun = dict()
pronoun['Paul'] = 'he'
pronoun['Helen'] = 'she'
pronoun['Ann'] = 'she'
pronoun['Mary'] = 'she'
pronoun['David'] = 'he'
pronoun['Mark'] = 'he'
pronoun['Michael'] = 'he'
pronoun['Susan'] = 'she'
pronoun['Robert'] = 'he'
pronoun['Peter'] = 'he'
pronoun['Christine'] = 'she'
pronoun['Sarah'] = 'she'
pronoun['Ivan'] = 'he'
pronoun['Charlotte'] = 'she'
pronoun['Pierre'] = 'he'
pronoun['Catherine'] = 'she'
pronoun['Audrey'] = 'she'
pronoun['John'] = 'he'
pronoun['Amanda'] = 'she'
pronoun['Kevin'] = 'he'

distractor = dict()
distractor[0] = ''
distractor[1] = ('Now, after you received all this information, try to concentrate, drink a cup of coffee, ' + 
                'go for a walk. Then please complete the following sentence. ')

# the following are sentences from the introduction in "Machine Learning. A Probabilistic Perspective" by Kevin P. Murphy
distractor[2] = ('With the ever increasing amounts of data in electronic form, the need for automated ' +
                'methods for data analysis continues to grow. ')
distractor[3] = ('With the ever increasing amounts of data in electronic form, the need for automated ' +
                'methods for data analysis continues to grow. ' + 
                'The goal of machine learning is to develop methods that can automatically detect patterns ' + 
                'in data, and then to use the uncovered patterns to predict future data or other outcomes of interest. ')
distractor[4] = ('With the ever increasing amounts of data in electronic form, the need for automated ' +
                'methods for data analysis continues to grow. ' + 
                'The goal of machine learning is to develop methods that can automatically detect patterns ' + 
                'in data, and then to use the uncovered patterns to predict future data or other outcomes of interest. ' + 
                'Machine Learning is thus closely related to the fields of statistics and data mining, but differs ' + 
                'slightly in terms of its emphasis and terminology. ')
distractor[5] = ('With the ever increasing amounts of data in electronic form, the need for automated ' +
                'methods for data analysis continues to grow. ' + 
                'The goal of machine learning is to develop methods that can automatically detect patterns ' + 
                'in data, and then to use the uncovered patterns to predict future data or other outcomes of interest. ' + 
                'Machine Learning is thus closely related to the fields of statistics and data mining, but differs ' + 
                'slightly in terms of its emphasis and terminology. ' + 
                'This book provides a detailed introduction to the field, and includes worked examples drawn from ' + 
                'application domains such as molecular biology, text processing, computer vision, and robotics. ')

# alternative to #3
distractor[6] = ('Syntax and semantics certainly interact in the generation of errors and the recovery from ' +
                'them in the language development of children. ')

# alternative to 3-5 from "The Geometry of Schemes" D. Eisenbud, J. Harris
distractor[7] = ('The theory of schemes is the foundation for algebraic geometry formulated by Alexandre ' +
                'Grothendieck and his many coworkers. ')

distractor[8] = ('The theory of schemes is the foundation for algebraic geometry formulated by Alexandre ' +
                'Grothendieck and his many coworkers. ' + 
                'It is the basis for a grand unification of number theory and algebraic geometry, dreamt ' +
                'of by number theorists and geometers for over a century. ')

distractor[9] = ('The theory of schemes is the foundation for algebraic geometry formulated by Alexandre ' +
                'Grothendieck and his many coworkers. ' + 
                'It is the basis for a grand unification of number theory and algebraic geometry, dreamt ' +
                'of by number theorists and geometers for over a century. ' +
                'It has strengthened classical algebraic geometry by allowing flexible geometric arguments ' +
                'about infinitesimals and limits in a way that the classic theory could not handle. ')

distractor[10] = ('The theory of schemes is the foundation for algebraic geometry formulated by Alexandre ' +
                'Grothendieck and his many coworkers. ' + 
                'It is the basis for a grand unification of number theory and algebraic geometry, dreamt ' +
                'of by number theorists and geometers for over a century. ' +
                'It has strengthened classical algebraic geometry by allowing flexible geometric arguments ' +
                'about infinitesimals and limits in a way that the classic theory could not handle. ' +
                'In both these ways it has made possible astonishing solutions of many concrete problems. ' +
                'On the number-theoretic side one may cite the proof of the Weil conjectures. ')

# repetitions of #6

distractor[11] = distractor[6] + distractor[6]
distractor[12] = distractor[6] + distractor[6] + distractor[6]
distractor[13] = distractor[6] + distractor[6] + distractor[6] + distractor[6]
distractor[14] = distractor[6] + distractor[6] + distractor[6] + distractor[6] + distractor[6]
distractor[15] = distractor[6] + distractor[6] + distractor[6] + distractor[6] + distractor[6] + distractor[6]

# 10 independent facts not involving people
distractor[99] = ('The color of France on the map is blue. ' + 
                'The color of Finland on the map is white. ' +
                'The color of Spain on the map is yellow. ' +
                'The color of Japan on the map is purple. ' +
                'The color of Italy on the map is green. ' +
                'The color of India on the map is brown. ' +
                'The color of Greece on the map is violet. ' +
                'The color of Brazil on the map is orange. ' +
                'The color of Denmark on the map is gray. ' +
                'The color of Mexico on the map is red. ')


def get_distractor(n):
    if n<100:
        return distractor[n]
    else:
        return 'Humpty Dumpty. '*(n-100)





def get_objects_verb_reverse(task):
    if task=='lives-in':
        objects = lives_in.copy()
        verb = 'lives in'
        reverse_query = 'The name of the person who lives in'
    if task=='has-a':
        objects = has_a.copy()
        verb = 'has a'
        reverse_query = 'The name of the person who has a'
    if task=='is-a':
        objects = is_a.copy()
        verb = 'is a'
        reverse_query = 'The name of the'

    return objects, verb, reverse_query

def prepare_test(task, length, distractor_id, query_type, repetitions=30, seed=555, elaborate=[]):

    objects, verb, reverse_query = get_objects_verb_reverse(task)

    names = persons.copy()

    rng = np.random.default_rng(seed)

    test = []
    for i in range(repetitions):
        rng.shuffle(names)
        rng.shuffle(objects)

        prompt_common = ''
        for j in range(length):
            if j+1 in elaborate:
                elaboration = elaborations[objects[j]].format(pronoun[names[j]])
                prompt_common += '{} {} {}{} '.format(names[j], verb, objects[j], elaboration)            
            else:
                prompt_common += '{} {} {}. '.format(names[j], verb, objects[j])
        for j in range(length):
            prompt = prompt_common + get_distractor(distractor_id) 
            if query_type=='direct':
                prompt += '{} {} X'.format(names[j], verb)
                answer = token[objects[j]]
            if query_type=='reverse':
                prompt += '{} {} is X'.format(reverse_query, objects[j])
                answer = token[names[j]]
            test.append( (prompt, answer) )

    return test

# prepare tests of the form iv) and v) in my notes
#
# task 1 - distractor 1 - task 2 - distractor 2 - evaluate task 1 (adjacent=False)
# task 1 - task 2 - distractor 1 - distractor 2 - evaluate task 1 (adjacent=True)
# 
# task 2 can be any task variant or `mid` (picks middle fact from task 1) or `fillall` or `fillsingle` (for comparison)
# `fillall` repeats "Humpty Dumpty. " as many times as the length of the task instead of task 2
# `fillsingle` puts a single "Humpty Dumpty" - for comparing with `mid`
# `independent` provides a completely independent set of facts not involving people
# 
# permute=True additionally permutes task 2 (so the names do not appear in the same order as in task 1)
# complementary=True makes the names of task2 complementary to task1 (assumes length=10)

def prepare_complex_test(task1, task2, length, distractor_id1, distractor_id2, adjacent=False, permute=True, complementary=False, repetitions=30, seed=555):

    task2_is_real = task2 in ['lives-in', 'has-a', 'is-a']

    objects1, verb1, _ = get_objects_verb_reverse(task1)
    names1 = persons.copy()
    rng1 = np.random.default_rng(seed)

    if task2_is_real:
        objects2, verb2, _ = get_objects_verb_reverse(task2)
        names2 = persons.copy()
        rng2 = np.random.default_rng(seed)

    if complementary:
        assert length==10 and task2_is_real

    rngperm = np.random.default_rng(1621)
    
    distractor1 = get_distractor(distractor_id1)
    distractor2 = get_distractor(distractor_id2)

    test = []
    for i in range(repetitions):
        rng1.shuffle(names1)
        rng1.shuffle(objects1)

        task1_text = ''
        for j in range(length):
            task1_text += '{} {} {}. '.format(names1[j], verb1, objects1[j])

        if task2_is_real:
            if complementary:
                names2 = np.setdiff1d(persons, names1[:length])
            else:
                rng2.shuffle(names2)
            rng2.shuffle(objects2)
            task2_text = ''
            for j in range(length):
                task2_text += '{} {} {}. '.format(names2[j], verb2, objects2[j])

        if task2=='mid':
            jmid = (length - 1)//2
            task2_text = '{} {} {}. '.format(names1[jmid], verb1, objects1[jmid])

        if task2=='fillsingle':
            task2_text = 'Humpty Dumpty. '

        if task2=='fillall':
            task2_text = 'Humpty Dumpty. '*length

        if task2=='independent':
            task2_text = get_distractor(99)

        if permute:
            lst = task2_text.split('. ')[:-1]
            rngperm.shuffle(lst)
            task2_text = '. '.join(lst) + '. '

        for j in range(length):
            query = '{} {} X'.format(names1[j], verb1)
            answer = token[objects1[j]]

            if adjacent:
                prompt = task1_text + task2_text + distractor1 + distractor2 + query
            else:
                prompt = task1_text + distractor1 + task2_text + distractor2 + query

            test.append( (prompt, answer) )

    return test


if __name__=='__main__':

    def print_test(test):
        for p, t in test:
            print(p, '|', t)
        print()


    test = prepare_test('lives-in', 2, 0, 'direct', repetitions=3)
    print_test(test)

    test = prepare_test('lives-in', 2, 0, 'reverse', repetitions=3)
    print_test(test)

    test = prepare_test('has-a', 2, 0, 'direct', repetitions=3)
    print_test(test)

    test = prepare_test('has-a', 2, 0, 'reverse', repetitions=3)
    print_test(test)

    test = prepare_test('is-a', 2, 0, 'direct', repetitions=3)
    print_test(test)

    test = prepare_test('is-a', 2, 0, 'reverse', repetitions=3)
    print_test(test)

    test = prepare_test('is-a', 2, 1, 'reverse', repetitions=3)
    print_test(test)

    test = prepare_test('has-a', 2, 0, 'direct', repetitions=3, elaborate=[1])
    print_test(test)

    print()
    print('----------- COMPLEX TASKS ------------')
    print()

    nrep = 1

    print('iv) INTERVENING SECOND TASK')
    test = prepare_complex_test('has-a', 'is-a', 3, 6, 1, adjacent=False, permute=True, repetitions=nrep)
    print_test(test)

    print('iv) INTERVENING SECOND TASK reference')
    test = prepare_complex_test('has-a', 'fillall', 3, 6, 1, adjacent=False, permute=True, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS')
    test = prepare_complex_test('has-a', 'has-a', 3, 6, 1, adjacent=False, permute=False, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS permute')
    test = prepare_complex_test('has-a', 'has-a', 3, 6, 1, adjacent=False, permute=True, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS adjacent')
    test = prepare_complex_test('has-a', 'has-a', 3, 6, 1, adjacent=True, permute=False, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS adjacent permute')
    test = prepare_complex_test('has-a', 'has-a', 3, 6, 1, adjacent=True, permute=True, repetitions=nrep)
    print_test(test)


    print('v) REPETITIONS mid')
    test = prepare_complex_test('has-a', 'mid', 3, 6, 1, adjacent=False, permute=False, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS mid reference')
    test = prepare_complex_test('has-a', 'fillsingle', 3, 6, 1, adjacent=False, permute=False, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS mid adjacent')
    test = prepare_complex_test('has-a', 'mid', 3, 6, 1, adjacent=True, permute=False, repetitions=nrep)
    print_test(test)

    print('v) REPETITIONS mid adjacent reference')
    test = prepare_complex_test('has-a', 'fillsingle', 3, 6, 1, adjacent=True, permute=False, repetitions=nrep)
    print_test(test)



    print()
    print('----------- OTHER ------------')
    print()

    print('VARIABLE LENGTH')
    test = prepare_test('has-a', 2, 105, 'direct', repetitions=1)
    print_test(test)

    print('iv) INTERVENING SECOND TASK complementary names')
    test = prepare_complex_test('has-a', 'is-a', 10, 101, 101, adjacent=False, permute=True, complementary=True, repetitions=1)
    print(test[0][0], '|', test[0][1])
    print()

    print('iv) INTERVENING SECOND TASK independent')
    test = prepare_complex_test('has-a', 'independent', 10, 101, 101, adjacent=False, permute=True, repetitions=2)
    print()
    print(test[0][0], '|', test[0][1])
    print()
    print(test[10][0], '|', test[10][1])
    print()
    
