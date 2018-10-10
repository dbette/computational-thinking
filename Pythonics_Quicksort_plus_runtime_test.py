import random
import time
import matplotlib.pyplot as plt

def start_sort(myList):
    """Starts the quicksort by evaluating starting and 
       ending index of the list.
    
    Args:
        myList: List that is to be sorted.
    Returns:
        quicksort(myList, start, end): Calls the quicksort function.
        myList: List that is to be sorted.
        start: The starting index of the input list.
        end: The ending index of the list.
    """
    start = 0
    end = len(myList) - 1
    return quicksort(myList, start, end)

def quicksort(myList, start, end):
    """Regulates the pivot selection by calling the partition function
       and calls for further quicksorts of the halved lists.
    
    Args:
        myList: List that is to be sorted.
        start: The starting index of the list/partition.
        end: The ending index of the list/partition.
    Returns:
        Returns the sorted list.
    """
    if start < end:
        pivot = partition(myList, start, end)
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    """Moves the right and left pointer and changes the numbers
       within the list according to the Quicksort principle until 
       the pointers cross. The index for selecting the new pivot 
       is returned.
    
    Args:
        myList: List that is to be sorted.
        start: The starting index of the partition.
        end: The ending index of the partition.
    Returns:
        Returns index of the right pointer.
    """
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            myList[left], myList[right] = myList[right], myList[left]
    myList[start], myList[right] = myList[right], myList[start]
    return right   
    
# These functions are testing the runtime of the quicksort algorythm.

def create_cards(n, method):
    """Creats a list of cards and shuffles it.
    
    Args:
        n: The number of integers that should be in the list.
        method: The method the integers should be ordered in the
        list (shuffle, increasing, decreasing).
    Returns:
        A list of n integers.
    """
    if type(n) != int:
        print('Please use an integer for n!')
        return 
    if n <= 1:
        print('Please use a positive integer for n!')
        return
    if method not in ['inc', 'dec', 'shuffle']:
        print('Please use a valid method!')
        return
    if method == 'inc':
        cards = list(range(1, n+1))
    if method == 'dec':
        cards = list(range(n+1, 1, -1))
    if method == 'shuffle':
        cards = list(range(1, n+1))
        random.shuffle(cards) 
    return(cards)

def avg_time(n_iteration, n_cards, method):        
    """Returns the runtime of the quicksort algorythm.
    
    Args:
        n_iterations: The number of iterations.
        n_cards: The number of cards.
        method: the method the integers should be ordered in the
        list (shuffle, increasing, decreasing).
    Returns:
        average_time: The average runtime in seconds.
    """
    measure_time = []
    for i in range(0, n_iteration):
        cards = create_cards(n_cards, method)
        start = time.time()
        start_sort(cards)
        measure_time.append(time.time()-start)
    average_time = sum(measure_time)/len(measure_time)
    return(average_time)

# A sorting test is executed.

unordered_test_list = [214234, -3, 0, 0, 13, 3, 1000, 5, 133, 3, 5, 777, 1, 1000]
print(unordered_test_list)
print(start_sort(unordered_test_list))

# A runtime test with shuffled cards is executed.

print("Please wait some seconds for the runtime test... It's worth it!")
time_cards_rnd = []
number_cards_rnd = []
for n_cards in range(10, 3000, 100):
    time_in_sec = avg_time(30, n_cards, 'shuffle')
    time_cards_rnd.append(time_in_sec)
    number_cards_rnd.append(n_cards)
    
# A runtime test with increasingly ordered sets is executed.
    
time_cards_worst = []
number_cards_worst = []
for n_cards in range(10, 1000, 100):
    time_in_sec = avg_time(1, n_cards, 'inc')
    time_cards_worst.append(time_in_sec)
    number_cards_worst.append(n_cards)
    
# The results of the tests will be plotted in the following. 
    
plt.plot(number_cards_rnd, time_cards_rnd, label = 'Randomized order')
plt.plot(number_cards_worst, time_cards_worst, label = 'Increasingly ordered')
plt.xlabel("Number of cards")
plt.ylabel("Runtime in seconds")
plt.title("Quicksort algorithm runtime")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()