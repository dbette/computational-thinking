liste = [3, 4, 1, 2, 3, 10, 6, 7, 9, 17]
number = 8

def number_check(liste, number):
    solution = []
    for i in range(0, len(liste)):
        for j in range(i, len(liste)):
            if liste[i] + liste[j] == number:
                if liste[i] != liste[j]:
                    solution.append([liste[i], liste[j]])
    return solution

print(number_check(liste, number))