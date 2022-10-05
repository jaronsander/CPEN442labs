import CpenAssignmentTwo
import random
import ngram_score_1
import math
from copy import copy



quadgram_scorer = ngram_score_1.ngram_score("english_quadgrams.txt")

def swap_columns(tempword, keyword, col1, col2):
    tempword = list(tempword)
    for row in range(5):
        tempword[5 * row + col1] = keyword[5 * row + col2]
        tempword[5 * row + col2] = keyword[5 * row + col1]

    return "".join(tempword)

def get_swapped_columns_key(keyword):
    col1 = random.randrange(0, 5)
    col2 = random.randrange(0, 5)

    return swap_columns(copy(keyword), keyword, col1, col2)


def swap_rows(tempword, keyword, row1, row2):
    tempword = list(tempword)
    tempword[5 * row1: 5 * row1 + 5] = keyword[5 * row2: 5 * row2 + 5]
    tempword[5 * row2: 5 * row2 + 5] = keyword[5 * row1: 5 * row1 + 5]

    return "".join(tempword)

def get_swapped_rows_key(keyword):
    row1 = random.randrange(0, 5)
    row2 = random.randrange(0, 5)

    return swap_rows(copy(keyword), keyword, row1, row2)

def get_reflect_rows_key(keyword):
    tempword = copy(keyword)
    
    tempword = swap_rows(tempword, keyword, 0, 4)

    return swap_rows(tempword, keyword, 1, 3)

def get_reflected_columns_key(keyword):
    tempword = copy(keyword)
    tempword = swap_columns(tempword, keyword, 0, 4)

    return swap_columns(tempword, keyword, 1, 3)

def get_reflected_diagonal_key(keyword):
    tempword = list(copy(keyword))

    for row in range(5):
        for column in range(5):
            tempword[5 * row + column] = keyword[5 * column + row]

    return "".join(tempword)

def get_reversed_key(keyword):
    return keyword[::-1]

def get_single_swap_key(keyword):
    tempword = list(copy(keyword))
    positions = [
        random.randrange(0,5),
        random.randrange(0,5),
        random.randrange(0,5),
        random.randrange(0,5)
    ]

    tempword[5 * positions[0] + positions[1]] = keyword[5 * positions[2] + positions[3]]
    tempword[5 * positions[2] + positions[3]] = keyword[5 * positions[0] + positions[1]]
    return "".join(tempword)

OPTIONS = [
    get_swapped_columns_key, 
    get_swapped_rows_key,
    get_reflect_rows_key,
    get_reflected_columns_key,
    get_reflected_diagonal_key,
    get_reversed_key,
    get_single_swap_key
    ]

def get_random_key(keyword):
    random_value = random.randrange(0, 20)
    if random_value > 6:
        random_value = 6
    return OPTIONS[random_value](keyword)


def score_by_quadgrams(plaintext):
    return quadgram_scorer.score(plaintext)

def do_anyway(dE, T):
    if T == 0:
        return False
    return random.random() < math.exp(dE/T)

if __name__ == "__main__":
    TESTS = 20
    ROUNDS = 20000
    SUBROUND = 3
    best_key = "".join(random.sample(CpenAssignmentTwo.alphabet, len(CpenAssignmentTwo.alphabet)))
    plaintext = CpenAssignmentTwo.decrypt_ciphertext_from_keyword(best_key)
    best_score = score_by_quadgrams(plaintext) + plaintext.count("COMXMA") * 500
    for test in range(TESTS):
        for round in range(ROUNDS):
            best_key_old = best_key
            for subround in range(SUBROUND):
                test_key = get_random_key(best_key_old)
                plaintext = CpenAssignmentTwo.decrypt_ciphertext_from_keyword(test_key)
                test_score = score_by_quadgrams(plaintext) + plaintext.count("COMXMA") * 500
                delta_E = test_score - best_score
                if  delta_E > 0:
                    best_score = test_score
                    best_key = test_key
                elif do_anyway(delta_E, (TESTS - test) * 5):
                    best_score = test_score
                    best_key = test_key
            #Bonus Subround!
            test_key = "".join(random.sample(best_key_old, len(best_key_old)))
            plaintext = CpenAssignmentTwo.decrypt_ciphertext_from_keyword(test_key)
            test_score = score_by_quadgrams(plaintext) + plaintext.count("COMXMA") * 500
            delta_E = test_score - best_score
            if  delta_E > 0:
                best_score = test_score
                best_key = test_key
            elif do_anyway(delta_E, (TESTS - test)):
                best_score = test_score
                best_key = test_key

        print("Best Key after Test ", test)
        print("Key: ", best_key)
        print("Plaintext: ", CpenAssignmentTwo.decrypt_ciphertext_from_keyword(best_key))
        print("Score: ", best_score)
