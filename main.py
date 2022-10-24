from hashlib import sha256
import string
from itertools import combinations_with_replacement

id = "veryuniqueid"
hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
l_and_n = string.ascii_lowercase+string.digits
number_of_zeroes = 6

def isCorrect(hex):
    for j in range(number_of_zeroes):
        if hex[j] != '0':
            return False
    return True


if __name__ == '__main__':
    i = 0
    for length in range(1, 1000):
        print("length = " + str(length) + "\n")
        c_w_r = combinations_with_replacement(l_and_n,length)
        for tuple in c_w_r:
            i+=1
            if(i % 1e6 == 0):
                print("Reached " + str(i) + " iterations \n")
            coin_blob = ''.join(tuple)
            sha = sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id).encode('utf-8'))
            if isCorrect(sha.hexdigest()):
                print(coin_blob, sha.hexdigest())
                exit()

