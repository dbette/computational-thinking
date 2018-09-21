import random
import time
import matplotlib.pyplot as plt

def create_cards(num_cards):
    cards = list(range(1,num_cards))
    random.shuffle(cards)
    return(cards)

def sorting(cards):
    for j in range(1, len(cards)):
        key = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > key:
            cards[i+1] = cards[i]
            i -= 1
        cards[i+1]=key
    return(cards)
    
def iteration(number_iteration, number_cards):
    measure_time = []
    for i in range(0, number_iteration):
        cards = create_cards(number_cards)
        start = time.time()
        sorting(cards)
        measure_time.append(time.time()-start)
    average_time = sum(measure_time)/len(measure_time)
    print("Average time: " + "{0:.9f}".format(average_time) + " seconds")
    return(average_time)

time_cards = []
print("Please wait some time... It's worth it!")
for number_cards in range(10, 1000, 100):
    time_in_sec = iteration(1000, number_cards)
    time_cards.append(time_in_sec)
    
plt.plot([10, 110, 210, 310, 410, 510, 610, 710, 810, 910], time_cards)
plt.xlabel("Number cards")
plt.ylabel("Average runtime in seconds")
plt.title("Insertion sort algorithm runtime")
plt.show()
