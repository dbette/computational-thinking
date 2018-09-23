
import random
import time
import matplotlib.pyplot as plt


def create_cards(n, method):
    """
    Returns an list of integers.
    
    Args:
        n: the number of integers.
        method: the method the integers are ordered in the list (random, worst, best)
    Returns:
        list of n integers.
    """
    
    if type(n) != int:
        print('Please use an integer for n!')
        return 
    
    if n <= 1:
        print('Please use a positive integer for n!')
        return
    
    if type(method) != str:
        print('Please use a string for method!')
        return
    
    if method.lower() not in ['random', 'worst', 'best']:
        print('Please use a valid method!')
        return
    
    cards = list(range(1,n+1))
    
    if method.lower()=='random':
        random.shuffle(cards)   
    elif method.lower()=='worst':
        cards = cards[::-1]
        
    return(cards)


def quicksort(input_array):
    """
    Implementation of the quicksort algorithm.
    
    Args:
        input_array: list consisting of integers.
    Return:
        sorted list.
    """
    
    left = []
    right = []
    pivot = []
    
    if len(input_array) <= 1:
        return input_array
    else:
        pivot_number = input_array[-1]
        for card in input_array:
            if card < pivot_number:
                left.append(card)
            elif card == pivot_number:
                pivot.append(card)
            else:
                right.append(card)
                
        #print("Pivot: " + str(pivot))
        #print("Left: " + str(left))
        #print("Right: " + str(right))

        left = quicksort(left)
        right = quicksort(right)
        
        return left + pivot + right


cards = create_cards(n=10, method='random')
print(quicksort(cards))


#def iteration(n_iteration, n_cards, method):
#    measure_time = []
#    for i in range(0, n_iteration):
#        cards = create_cards(n_cards, method)
#        start = time.time()
#        quicksort(cards)
#        measure_time.append(time.time()-start)
#    average_time = sum(measure_time)/len(measure_time)
#    print("Average time: " + "{0:.9f}".format(average_time) + " seconds")
#    return(average_time)
#
#time_cards = []
#number_cards = []
#print("Please wait some time... It's worth it!")
#for n_cards in range(10, 10000, 100):
#    time_in_sec = iteration(10, n_cards, method='random')
#    time_cards.append(time_in_sec)
#    number_cards.append(n_cards)
#    
#    
#plt.plot(number_cards, time_cards)
#plt.xlabel("Number cards")
#plt.ylabel("Average runtime in seconds")
#plt.title("Quicksort algorithm runtime")
#plt.show()