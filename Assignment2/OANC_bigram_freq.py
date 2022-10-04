import os
import re
from contextlib import redirect_stdout
fdir = "C:/Users/vesbr/Downloads/OANC-1.0.1-UTF8/OANC/data"

n_freq = 3
separator = "\n"+"#"*15+"\n"

if __name__ == '__main__':

    print("Generating " +str(n_freq)+ "grams")
    freq = {}
    sum = 0
    for path, subdirs, files in os.walk(fdir):
        for name in files:
            if(name.endswith(".txt")):
                ff = os.path.join(path, name)
                with open(ff, encoding='utf-8') as f :
                    raw=f.read().lower()
                    data = re.sub(r'[^a-zA-Z]', '', raw)
                    data = re.sub(r'[j]', 'i', data)
                    partials_dict = [(data[i:i + 2],i) for i in range(0, len(data), 2)]
                    for t in partials_dict:
                        k = t[0]
                        v = t[1]
                        if k[0] == [1]:
                            data = data[:v]+'x'+data[v:]
                    if len(data)%2 == 1 :
                        data += 'x'
                    # `data` now contains the string parsed as it would be if used for input to playfair cipher
                    # we can extract partials's frequencies now --> get n_grams
                    partials = [data[i:i + n_freq] for i in range(0, len(data), n_freq)]
                    for i in partials:
                        if i in freq:
                            freq[i] += 1
                        else:
                            freq[i] = 1
                        sum+=1
                #print("Finished with file" + ff+"\n")

    sortfreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    normalized = [(t[0],(t[1]/sum)*100) for t in sortfreq]
    non_tuple = [t[0] for t in sortfreq]
    with open("OANC"+str(n_freq)+"gram_out.txt","w") as f:
        with redirect_stdout(f):
            print("Sorted, raw:\n")
            print(sortfreq)
            print(separator)
            print("Sorted, normalized:\n")
            print(normalized)
            print(separator)
            print("Sorted, non-tuple:\n")
            print(non_tuple)

