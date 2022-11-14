from cryptography.hazmat.primitives import hashes

if __name__ == '__main__':
    bytes = bytes(input("input what to hash\n"), 'utf-8')
    digest = hashes.Hash(hashes.SHA1())
    digest.update(bytes)
    hash = digest.finalize()
    print(hash.hex())
    
    f = open("Group9.program2.exe", "r+b")
    f.seek(0x1d3f6)
    f.write(hash)
    f.close()