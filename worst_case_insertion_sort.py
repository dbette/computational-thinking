import random
import time

def create_cards_worst(num_cards):
    cards = list(range(1, num_cards))
    return(cards[::-1])

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
    for _ in range(0, number_iteration):
        cards = create_cards_worst(number_cards)
        start = time.time()
        sorting(cards)
        measure_time.append(time.time()-start)
    average_time = sum(measure_time)/len(measure_time)
    print("Time for " + str(number_cards) + " cards: " + "{0:.9f}".format(average_time) + " seconds")
    return(average_time)

time_cards = []

for number_cards in [10, 100, 1000, 10000, 100000]:
    time_in_sec = iteration(1, number_cards)
    time_cards.append(time_in_sec)