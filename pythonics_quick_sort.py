
import random


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