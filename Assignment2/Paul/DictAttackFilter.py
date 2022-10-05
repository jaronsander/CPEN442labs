# -*- coding: utf-8 -*-

deciphers = {}
with open("442-assignment-3-ordered.txt", "r") as file:
    for line in file.readlines():
        line = line.split(":")
        deciphers[line[0].strip()] = line[1].strip()

def count_words(plaintext, word_list):
    count = 0
    for word in word_list:
        count += plaintext.count(word) * len(word)
    return count
    

word_list = []

MAX_NUM = 10

num = 0


user_input = input("search word: ")
while len(user_input) > 1:
    num = 0
    for item in sorted(deciphers.items(), key = lambda t: count_words(t[1],[user_input]), reverse=True):
        print("Keyword: ", item[0])
        print("Plaintext: ", item[1])
        num += 1
        if num > MAX_NUM:
            break
    user_input = input("search word: ")