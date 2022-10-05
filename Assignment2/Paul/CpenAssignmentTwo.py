# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:11:18 2022

@author: Paul
"""
import re
from collections import OrderedDict

keyword = "route"

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
ciphertext = "MQWIDQWNSGYLKQYGRNTMARIEMRATGRZAIHXUTYYMMRIAGKQTUZCEBHBEIGVYCDXNWCULIOYGMAYGKWDMNRDNTVMVWIKFYIAXIZLAWZEAGKTKCPOVQGEDUNFUTYYMSGDUGSRNKGRNZWRNSYKRWZRCTAVYTNWTTNFUTYYMCEIRRILMFNYMYGKTGINRRDYZRKAZTCFHWUEXODATEIYGRNLMFNYMIZOQCEBPVOKWYGMAATATDLOXRIMDZAFHQYRCLAZAYGTSODZRAQZACKCBLAAMVSAZYGKWDMNRDNTVLMFNYMBYWLEXZMRDTDKFLMFNYMGKQTUZRIWYDQTEGYYBRTCUTYYMMRUQYVWIGHGZCDEMTAGKPYIZQYRCWNCPDOMWLICPIZEXYGMZYGKGQDAREDUNQUTATWKRWZKBDKYGCTLMFNYMPYGIWZNDTYYMMRCBLAZAYGTSYLICGLUNGUYCBORCWKYGCTLHMZGUVSNGIWTBTDCMTYYMSGDIKGITTLKRUBRNCEDOIHGUEXTNNBEDUOMAGUVYFETCHKOBLAMGYGNWQDYFGINRZMMERTZDSHTVZIIUQDRIVMKBRNRTWYGKTSRNNWQDYGRNRQUNLAMGYGRNIGRNNWIGRNPYYHKWMRCQIGRNQNLDMGAENGKWLMFNYMMRIAGKQMEAGKEAGKTSRKMGYGNTAZRIUWYMDORCOVKRVYTNYGNIYLEMKAGRDMTNLAAMMEMPMZYGKTQYAITVRXOAGKZAQAWUIRLMFNYMKRQDODTWOIRGZAYZLMFNYMMRCBLAZAYGOTGZKRUBRNRQHUIWMRIBTAYLYWTYRGNRQALAYWGKMVWNNRAQGLNIIWTAGKFUQDNIZAFITYYMHDYGRNNWYHRILAWTMYKRWZKBCKBEMUTYYMGKQYDCLMFNYMMRCDWTQYILUNOAGUEXDTFCTALMFNYMVMNAOYYLYGUWMZUOBOCEWICUTYYMMRCDWCHKYLICULAMPYIZCETWVYDUYLICRTMITYYMYGKWAETQDTYFYIXNWNIQTWGSYLICLMTNYLMITYYMMRIABYWGYLICVHTLIOGKHKOBZTXFSKRTCBLAAIAZTAKSQYQTATCMIWBYMGYGUWQTWYKDNITYYMVYHKZTZCMKALIRAQRCGIEMMZRTWTEXGKDRNRQALAMGWICPCOKWTYIWGUEXQRYLAOYLKQZIQMRCYGNIYLEMKAOTLUMYNWZAFMTYYMQYDCYGKWDMNRDNTVLMFNYMSGRKHKKGQAWCECHKRIGKDACEKRDATAVYHKIWVOUBCTODDOPAIYRYKFYQLMFNYMMRUBTVBEMOZWRNOAGUEXQTWYGKNRLMFNYMMRUBTVYGNIMUOVKRBYCUQDEDRIGKEATAGUVFIKRNDORCMVVLLAMGYGKWDMNRDNTVIDWYRKRIDMNRSCCPUOLMFNYMMRUQTDCUTYYMDUMRZMYIRCRNWYMRIQKSOTYHPYLIIQUWGYVORTWZYGUWGRYDWTSCIUYLEMKAMRIBAPMDEYTAGKADMUTYYMBEMOZOMDKTYLDMCPUZMRQYQUTAYGMAUWGRDMYHKTYLBYWZZMRDTDKFMRVQRNRIYGIEDEICTAZMYMMGWIKBTVADRTKAMRIBDQOTDKPYTNQYNRLMFNYMGIGZVZIZMVVCKWBYRCPDMPALVTLIADMAGKZDLWIWGKNRYGMRCEMROTYGRNLMCKAEMUTYYMGRTWZWRNVYGRYDWTSCICTAYGRNITFKVZDOINIDZRPYTNLAMGYGKWDMNRDNTVWUBPRILAATXMYLKQITDMCNZMYIRCRNWYMRCDMITYYMGKQYDCLAWTSMYLKBRTUQGINRWYCSWNIQTWKHAETQLMFNYMIDZRTCKRLMFNYMOTISYLICBZAPQRUOODCPIDWZCEYGRGRTIYCWLIZOMDKWLMFNYMMRIAGKKZMRQYVQYLICBYWZZMGZVZIZMAODICTATWUWVMEACKMANWAZRYKFYQYGMAOTYKOQRGDQCEQUTAVTEMOTIYZICORTWYAZMUTYYMSGDIIGRTNRNRWYCEBTHURIYGNIGUICLAMGYGKWDMNRDNTVOVYZRIMAGKNBNRBZTMUXSCCPUOLMFNYMMRAQKFGINRCAOUCWKGYQGRRKVYHKAZMGYGMADERTCPUOZKTVZMYGCEEGBYWIWZDATATGYQMZUOYMIRAQAHNWAZKTKWWIDAMOLAWGBYYGOBGZKRCDEMGKVTZDARNWAZIWBYMGWTTNUWODILKZZMFEATTNLAOILUEUUOLMFNYMSGRKYGNWQDTNNAQANTSKRTCUTYYMMZZTWMGKWCKQMGYGCEHWGKCDIQYQATBOCEAYTKQDFUTYYMVYYGMAUGRTDASGMAQTWHTLEXMZLAMGYGRNIGYQMRTAGKNACKUXEUEFTWPHGUFMTYYMMRIAGKWCKQMGYGCEETGKQDIQYQYGNWQDTNKQMOCEXITYYMPYQITOYLIDZRYGYVNGRTKQYGKTQDRKYWAETDBPMITYYMMRVQRNRIYGZTYGRNLAMEZWRNTCRCLMFNYMQYDCYGNWQDTNDATAYGKTQDNGRTKQDLWYYGKWMYNITYYMSGDUGSYQAEIKRKYLBPLAMETVDICOYRIWGKKTKWLMFNYMQYDCYGNWQDTNNB"

class BraindeadBoundedPriorityQueue:
    def __init__(self, size = 10, kick_highest_first = False):
        self._queue = []
        self._size = size
        self._kick_highest_first = kick_highest_first
        
    def __getitem__(self, key):
        return self._queue[key][0]
        
    def __len__(self):
        return len(self._queue)
        
    def __iter__(self):
        return map(lambda t: t[0], self._queue).__iter__()
    
    def __str__(self):
        return self._queue.__str__()
    
    def insert(self, item, priority):
        if len(self._queue) == 0 or priority <= self._queue[len(self._queue)-1][1]:
            self._queue.append((item, priority))
        elif priority >= self._queue[0][1]:
            self._queue.insert(0, (item, priority))
        else: 
            for i in range(len(self._queue) - 2, 0, -1):
                if priority < self._queue[i][1]:
                    self._queue.insert(i + 1, (item, priority))
                    break
        if len(self._queue) > self._size:
             self._queue.pop(0 if self._kick_highest_first else -1)

    
    def get_lowest(self):
        return self._queue.pop()[0]
    
    def get_highest(self):
        return self._queue.pop(0)[0]

    def peek_lowest(self):
        return self[-1]
    
    def peek_highest(self):
        return self[0]
        

def get_keygrid_from_keyword(keyword):
    keyword = "".join(OrderedDict.fromkeys(keyword.strip().upper().replace("J", "I")))

    keygrid = []
    for row in range(5):
        keygrid.append([".", ".", ".", ".", "."])
    
    for i in range(len(keyword)):
        keygrid[i//5][i % 5] = keyword[i]
    
    position = len(keyword)
    for letter in alphabet:
        if letter not in keyword:
            if position//5 >= 5:
                print(keygrid)
                print(keyword)
            keygrid[position//5][position % 5] = letter
            position += 1

    return keygrid


def decrypt(two_letter_substring, keygrid, position_map):
    if two_letter_substring[0] not in position_map or two_letter_substring[1] not in position_map:
        return ".."
    first = position_map[two_letter_substring[0]]
    second = position_map[two_letter_substring[1]]
    
    if first[0] == second[0]: #same row
        return keygrid[first[0]][(first[1] - 1) % 5] + keygrid[second[0]][(second[1] - 1) % 5]
        
    elif first[1] == second[1]: #same column
        return keygrid[(first[0] - 1) % 5][first[1]] + keygrid[(second[0] - 1) % 5][second[1]]
    
    else: #rectangle
        return keygrid[first[0]][second[1]] + keygrid[second[0]][first[1]]
        

def generate_position_map(keygrid):
    position_map = {}
    for row in keygrid:
        for letter in row: 
            position_map[letter] = (keygrid.index(row), row.index(letter))
    return position_map
    
def decrypt_ciphertext_from_keyword(keyword):
    keygrid = get_keygrid_from_keyword(keyword)
    return decrypt_ciphertext_from_keygrid(keygrid)

def decrypt_ciphertext_from_keygrid(keygrid):
    position_map = generate_position_map(keygrid)

    plaintext = ""
    
    for i in range(len(ciphertext)//2):
        plaintext += decrypt(ciphertext[i * 2: i * 2 + 2], keygrid, position_map)
    
    return plaintext


if __name__ == "__main__":
    
    MOST_COMMON_WORDS = []

    with open("most-common-english-words.txt", "r") as file:
        for line in file.readlines():
            word = line.strip().upper()
            if len(word) > 2:
                MOST_COMMON_WORDS.append(word)

    def get_score(plaintext, most_common_words):
        count = 0
        if len(re.split("[^AEIOUY]{6,}", plaintext)) > 1:
            return 0
        for word in most_common_words:
            count += plaintext.count(word)
        return count

    with open("Collins-Scrabble-Words.txt", "r") as file:
        words = file.read()

    possible_keywords = []
    for word in words.split("\n"):
        possible_word = "".join(OrderedDict.fromkeys(word.strip().replace("J", "I")))
        if len(possible_word) > 2:
            possible_keywords.append(possible_word)

    old_word = "Z"
    priority_queue = BraindeadBoundedPriorityQueue(25)
    for word in possible_keywords:
        if word[0] != old_word[0]:
            print("Reached: ", word[0])
            print("Queue: ", priority_queue)
        plaintext = decrypt_ciphertext_from_keyword(word)
        priority_queue.insert(word, get_score(plaintext, MOST_COMMON_WORDS))
        old_word = word

    with open("442-cpen-best-matches.txt", "w") as file:
        for keyword in priority_queue:
            plaintext = decrypt_ciphertext_from_keyword(keyword)
            print("Keyword: ", keyword)
            file.write("Keyword: " + keyword)
            file.write("Plaintext: " + plaintext)
            file.write("Score: " + str(get_score(plaintext, MOST_COMMON_WORDS)))