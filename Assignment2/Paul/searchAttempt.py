import CpenAssignmentTwo
from copy import deepcopy
import random

MAX_ROUNDS = 50000

english_frequencies = {
"A":0.08167,
"B":0.01492,
"C":0.02782,
"D":0.04253,
"E":0.12702,
"F":0.02288,
"G":0.02015,
"H":0.06094,
"I":0.06966,
"J":0.00153,
"K":0.00772,
"L":0.04025,
"M":0.02406,
"N":0.06749,
"O":0.07507,
"P":0.01929,
"Q":0.00095,
"R":0.05987,
"S":0.06327,
"T":0.09056,
"U":0.02758,
"V":0.00978,
"W":0.0236,
"X":0.0015,
"Y":0.01974,
"Z":0.00074
}


def get_frequency_distance_from_keygrid(keygrid):
    return get_frequency_distance(CpenAssignmentTwo.decrypt_ciphertext_from_keygrid(keygrid))

def get_frequency_distance(plaintext):
    frequencies = get_frequencies(plaintext)
    distance = 0
    for letter in frequencies:
        distance += (frequencies[letter] - english_frequencies[letter])**2
    return distance


def get_frequencies(plaintext):
    freq = {}
    for letter in plaintext:
        letter = letter.upper()
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    for key in freq:
        freq[key] = freq[key]/len(plaintext)
    return freq

initial_keygrid = CpenAssignmentTwo.get_keygrid_from_keyword("ADJOURN")

keygrid = initial_keygrid
best_grid = keygrid
MAX_ROUNDS = 50000

search_queue = CpenAssignmentTwo.BraindeadBoundedPriorityQueue(50, True)
search_queue.insert(keygrid, get_frequency_distance_from_keygrid(keygrid))

for round in range(MAX_ROUNDS):
    keygrid = search_queue[random.randrange(0, 4) - 4]

    if (round % 1000) == 0:
        print("Round ", round)
        print("Best: ")
        print("Keygrid: ", keygrid)
        print("Plaintext: ", CpenAssignmentTwo.decrypt_ciphertext_from_keygrid(keygrid))

    #row 0-2
    for i in range(3):
        test_grid = keygrid[:i] + [keygrid[i+1]] + [keygrid[i]] + keygrid[i + 2:]
        search_queue.insert(test_grid, get_frequency_distance_from_keygrid(test_grid))
    #row 3
    test_grid = keygrid[:3]
    test_grid += [keygrid[4]]
    test_grid += [keygrid[3]]
    search_queue.insert(test_grid, get_frequency_distance_from_keygrid(test_grid))

    #row 4
    test_grid = keygrid[4:]
    test_grid += keygrid[:4]
    search_queue.insert(test_grid, get_frequency_distance_from_keygrid(test_grid))

    #columns
    for i in range(5):
        test_grid = deepcopy(keygrid)
        for j in range(5):
            saved_value = test_grid[j][i]
            test_grid[j][i] = test_grid[j][(i+1) % 5]
            test_grid[j][(i+1) % 5] = saved_value
        search_queue.insert(test_grid, get_frequency_distance_from_keygrid(test_grid))

with open("442-cpen-best-matches.txt", "w") as file:
    for keygrid in search_queue:
        plaintext = CpenAssignmentTwo.decrypt_ciphertext_from_keygrid(keygrid)
        print("Keygrid: ", keygrid)
        file.write("Keygrid: " + str(keygrid))
        file.write("Plaintext: " + plaintext)
        file.write("Score: " + str(get_frequency_distance(plaintext)))