from CpenAssignmentTwo import decrypt_ciphertext_from_keyword

tests = [('subaltern', 121), ('misgovern', 99), ('cpen', 98), ('KERN', 98), ('HERN', 96), ('ERN', 94), ('NORTHERN', 94), ('SOUTHERN', 93), ('SLATTERN', 92), ('LEATHERN', 92), ('QUARTERN', 92), ('SUBALTERN', 92), ('UNCONCERN', 92), ('PREMODERN', 90), ('MISGOVERN', 90)]
for item in tests:
    print("Keyword: ", item[0])
    print("Plaintext: ", decrypt_ciphertext_from_keyword(item[0]))
    print("Score: ", item[1])