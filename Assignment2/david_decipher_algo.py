
import random
import math
from quadgramvar import quad_gram_freqs
key = "IDCULTAMYOWQFSVGBXHPERNKZ"

# didnt use this idea in the end
# general idea was scoring how good a text is based on quadgram frequencies and trying to find local maxima of how "good" a text is

def quadgramFreqScore(text):
    score = 0.0 #score of a text
    temp = ["","","",""]
    for i in range(0, len(text)-3):
        temp[0] = ord(text[i]) - ord('A')
        temp[1] = ord(text[i+1]) - ord('A')
        temp[2] = ord(text[i+2]) - ord('A')
        temp[3] = ord(text[i+3]) - ord('A')
        
        #17k possible trigrams, 676 possible digrams, 26 possible letters, last letter is known 
        score += quad_gram_freqs[17576*temp[0] + 676*temp[1] + 26*temp[2] + temp[3]]
    return score


# function for deciphering playfair cipher text
def decipher(key, inText):
    outText = [""]*len(inText)
    for i in range(0, len(inText), 2):
        # a represents first letter, b second letter
        a = inText[i]
        b = inText[i+1]
        # indexes of each letter relative to the key
        ind_a = key.find(a) 
        ind_b = key.find(b) 

        row_a = ind_a // 5
        row_b = ind_b // 5
        col_a = ind_a % 5
        col_b = ind_b % 5

        ## same row rule
        if(row_a == row_b):
            # rotate a to the end of the row
            if(col_a == 0):
                outText[i] = key[ind_a + 4] # move 4 col to the right
                outText[i+1] = key[ind_b - 1] # move  1 col to the left
            # rotate b to the end of the row
            elif(col_b == 0):
                outText[i] = key[ind_a-1]
                outText[i+1] = key[ind_b + 4]
            else:
                outText[i] = key[ind_a-1]
                outText[i+1] = key[ind_b -1]
        # same col rule
        elif(col_a == col_b):
            if(row_a == 0):
                outText[i] = key[ind_a + 20] # move 4 rows down
                outText[i+1] = key[ind_b - 5]  # move 1 
            elif(row_b == 0):
                outText[i] = key[ind_a - 5]
                outText[i+1] = key[ind_b + 20]
            else:
                outText[i] = key[ind_a - 5]
                outText[i+1] = key[ind_b - 5]
        else:
            outText[i] = key[5*row_a + col_b]
            outText[i+1] = key[5*row_b + col_a]
    return ''.join(outText)

# swap 2 specific indices in any string
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

# swap 2 random indices in key
def swap2randLetters(key):
    i = random.randint(0,24)
    j = random.randint(0,24)
    return swap(key, i, j)

# swap 2 random rows of the key
def swap2RandRows(key):
    out = key
    i = random.randint(0,4)
    j = random.randint(0,4)
    for k in range(5):
        out = swap(out, i*5 + k, j*5 + k)
    return out

# swap 2 random columns of the key
def swap2RandCols(key):
    out = key
    i = random.randint(0,4)
    j = random.randint(0,4)
    for k in range(5):
        out = swap(out, k*5 + i, k*5 + j)
    return out

# modify the key 
def changeKey(oldKey):
    newList = list(oldKey)
    oldList = list(oldKey)
    k = random.randint(0,49)
    j = random.randint(0,49)
    i = random.randint(0,49)
    if i == 0:
        return swap2RandRows(oldKey)
    elif i == 1:
        return swap2RandCols(oldKey)
    elif i == 2:
        for k in range(25):
            newList[k] = oldList[24-k]
        return ''.join(newList)
    elif i == 3:
        for k in range(5):
            for j in range(5):
                newList[k*5 + j] = oldList[(4-k)*5 + j]
        return ''.join(newList)
    elif i == 4:
        for k in range(5):
            for j in range(5):
                newList[j*5 + k] = oldList[(4-j)*5 + k]
        return ''.join(newList)
    else: 
        return swap2randLetters(oldKey)


def crackPlayfair(text, bestKey):
    maxKey = bestKey
    deciphered = decipher(maxKey, text)
    maxScore = quadgramFreqScore(deciphered)
    bestScore = maxScore
    for T in range(2,-1, -1):
        for count in range(10000):
            testKey = changeKey(maxKey)
            deciphered = decipher(testKey, text)
            score = quadgramFreqScore(deciphered)
            dF = score - maxScore
            if dF >= 0:
                maxScore = score
                maxKey = testKey
            elif T/5 > 0:
                prob = math.exp(dF/(T/5))
                flt = random.uniform(0,1)
                if prob > flt:
                    maxScore = score
                    maxKey = testKey
            if maxScore > bestScore:
                bestScore = maxScore
                bestKey = maxKey
    return (bestScore, bestKey)

#main function
if __name__ == '__main__':
    cipher = "MQWIDQWNSGYLKQYGRNTMARIEMRATGRZAIHXUTYYMMRIAGKQTUZCEBHBEIGVYCDXNWCULIOYGMAYGKWDMNRDNTVMVWIKFYIAXIZLAWZEAGKTKCPOVQGEDUNFUTYYMSGDUGSRNKGRNZWRNSYKRWZRCTAVYTNWTTNFUTYYMCEIRRILMFNYMYGKTGINRRDYZRKAZTCFHWUEXODATEIYGRNLMFNYMIZOQCEBPVOKWYGMAATATDLOXRIMDZAFHQYRCLAZAYGTSODZRAQZACKCBLAAMVSAZYGKWDMNRDNTVLMFNYMBYWLEXZMRDTDKFLMFNYMGKQTUZRIWYDQTEGYYBRTCUTYYMMRUQYVWIGHGZCDEMTAGKPYIZQYRCWNCPDOMWLICPIZEXYGMZYGKGQDAREDUNQUTATWKRWZKBDKYGCTLMFNYMPYGIWZNDTYYMMRCBLAZAYGTSYLICGLUNGUYCBORCWKYGCTLHMZGUVSNGIWTBTDCMTYYMSGDIKGITTLKRUBRNCEDOIHGUEXTNNBEDUOMAGUVYFETCHKOBLAMGYGNWQDYFGINRZMMERTZDSHTVZIIUQDRIVMKBRNRTWYGKTSRNNWQDYGRNRQUNLAMGYGRNIGRNNWIGRNPYYHKWMRCQIGRNQNLDMGAENGKWLMFNYMMRIAGKQMEAGKEAGKTSRKMGYGNTAZRIUWYMDORCOVKRVYTNYGNIYLEMKAGRDMTNLAAMMEMPMZYGKTQYAITVRXOAGKZAQAWUIRLMFNYMKRQDODTWOIRGZAYZLMFNYMMRCBLAZAYGOTGZKRUBRNRQHUIWMRIBTAYLYWTYRGNRQALAYWGKMVWNNRAQGLNIIWTAGKFUQDNIZAFITYYMHDYGRNNWYHRILAWTMYKRWZKBCKBEMUTYYMGKQYDCLMFNYMMRCDWTQYILUNOAGUEXDTFCTALMFNYMVMNAOYYLYGUWMZUOBOCEWICUTYYMMRCDWCHKYLICULAMPYIZCETWVYDUYLICRTMITYYMYGKWAETQDTYFYIXNWNIQTWGSYLICLMTNYLMITYYMMRIABYWGYLICVHTLIOGKHKOBZTXFSKRTCBLAAIAZTAKSQYQTATCMIWBYMGYGUWQTWYKDNITYYMVYHKZTZCMKALIRAQRCGIEMMZRTWTEXGKDRNRQALAMGWICPCOKWTYIWGUEXQRYLAOYLKQZIQMRCYGNIYLEMKAOTLUMYNWZAFMTYYMQYDCYGKWDMNRDNTVLMFNYMSGRKHKKGQAWCECHKRIGKDACEKRDATAVYHKIWVOUBCTODDOPAIYRYKFYQLMFNYMMRUBTVBEMOZWRNOAGUEXQTWYGKNRLMFNYMMRUBTVYGNIMUOVKRBYCUQDEDRIGKEATAGUVFIKRNDORCMVVLLAMGYGKWDMNRDNTVIDWYRKRIDMNRSCCPUOLMFNYMMRUQTDCUTYYMDUMRZMYIRCRNWYMRIQKSOTYHPYLIIQUWGYVORTWZYGUWGRYDWTSCIUYLEMKAMRIBAPMDEYTAGKADMUTYYMBEMOZOMDKTYLDMCPUZMRQYQUTAYGMAUWGRDMYHKTYLBYWZZMRDTDKFMRVQRNRIYGIEDEICTAZMYMMGWIKBTVADRTKAMRIBDQOTDKPYTNQYNRLMFNYMGIGZVZIZMVVCKWBYRCPDMPALVTLIADMAGKZDLWIWGKNRYGMRCEMROTYGRNLMCKAEMUTYYMGRTWZWRNVYGRYDWTSCICTAYGRNITFKVZDOINIDZRPYTNLAMGYGKWDMNRDNTVWUBPRILAATXMYLKQITDMCNZMYIRCRNWYMRCDMITYYMGKQYDCLAWTSMYLKBRTUQGINRWYCSWNIQTWKHAETQLMFNYMIDZRTCKRLMFNYMOTISYLICBZAPQRUOODCPIDWZCEYGRGRTIYCWLIZOMDKWLMFNYMMRIAGKKZMRQYVQYLICBYWZZMGZVZIZMAODICTATWUWVMEACKMANWAZRYKFYQYGMAOTYKOQRGDQCEQUTAVTEMOTIYZICORTWYAZMUTYYMSGDIIGRTNRNRWYCEBTHURIYGNIGUICLAMGYGKWDMNRDNTVOVYZRIMAGKNBNRBZTMUXSCCPUOLMFNYMMRAQKFGINRCAOUCWKGYQGRRKVYHKAZMGYGMADERTCPUOZKTVZMYGCEEGBYWIWZDATATGYQMZUOYMIRAQAHNWAZKTKWWIDAMOLAWGBYYGOBGZKRCDEMGKVTZDARNWAZIWBYMGWTTNUWODILKZZMFEATTNLAOILUEUUOLMFNYMSGRKYGNWQDTNNAQANTSKRTCUTYYMMZZTWMGKWCKQMGYGCEHWGKCDIQYQATBOCEAYTKQDFUTYYMVYYGMAUGRTDASGMAQTWHTLEXMZLAMGYGRNIGYQMRTAGKNACKUXEUEFTWPHGUFMTYYMMRIAGKWCKQMGYGCEETGKQDIQYQYGNWQDTNKQMOCEXITYYMPYQITOYLIDZRYGYVNGRTKQYGKTQDRKYWAETDBPMITYYMMRVQRNRIYGZTYGRNLAMEZWRNTCRCLMFNYMQYDCYGNWQDTNDATAYGKTQDNGRTKQDLWYYGKWMYNITYYMSGDUGSYQAEIKRKYLBPLAMETVDICOYRIWGKKTKWLMFNYMQYDCYGNWQDTNNB"

    print("this may take several minutes")
    key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    score = -99e99
    maxScore = -99e99
    i = 0
    while(1):
        i += 1
        (score, key) = crackPlayfair(cipher, key)
        if(score > maxScore):
            maxScore = score
            print("best score so far: ", maxScore, "on iteration: ", i)
            print("Key: ", key)
            deciphered = decipher(key, cipher)
            print(" plaintext: ", deciphered)
