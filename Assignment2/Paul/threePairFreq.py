import CpenAssignmentTwo


if __name__ == '__main__':
    text = CpenAssignmentTwo.ciphertext
    most_common_three_groups = {}
    for i in range(0, len(text) - 5, 2):
        three_group = text[i:i+6]
        if (three_group in most_common_three_groups):
            most_common_three_groups[three_group] += 1
        else:
            most_common_three_groups[three_group] = 1

    sortfreq=sorted(most_common_three_groups.items(), key=lambda t: t[1], reverse=True)
    print(sortfreq)

    MIN_TIMES = 3
    TARGET_WORD = "COMXMA"

    all_pot_encrypt_maps = []
    for item in sortfreq:
        if item[1] < MIN_TIMES:
            break
        mapping = {
            item[0][:2] : TARGET_WORD[:2],
            item[0][2:4] : TARGET_WORD[2:4],
            item[0][4:] : TARGET_WORD[4:]
        }
        all_pot_encrypt_maps.append(mapping)


    with open("out.txt",'w') as f:
         for dict in all_pot_encrypt_maps:
            plaintext = ""
            replaced = 0
            flag = False
            two_in_a_row = 0
            for i in range(0,len(text),2):
                alreadyReplaced = False
                for k,v in dict.items():
                    ct = text[i]+text[i+1]
                    if ct == k:
                        plaintext+=v
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                    elif ct == k[::-1]:
                        plaintext += v[::-1]
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                if(two_in_a_row >= 2) :
                    flag = True
                if not alreadyReplaced:
                    plaintext+=".."
                    two_in_a_row = 0
            tern = " HAVETWO!!!" if flag else " NOPAIR:("
            o = plaintext+'\n'+ "Replaced: " + str(replaced)  + ", using mapping: " + str(dict) +tern +'\n\n\n'
            #print(o)
            f.write(o)