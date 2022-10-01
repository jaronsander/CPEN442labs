import os
import re
fdir = "C:/Users/vesbr/Downloads/OANC-1.0.1-UTF8/OANC/data"

if __name__ == '__main__':

    freq = {}
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
                    partials = [data[i:i + 2] for i in range(0, len(data), 2)]
                    for i in partials:
                        if i in freq:
                            freq[i] += 1
                        else:
                            freq[i] = 1
                #print("Finished with file" + ff+"\n")
    sortfreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(sortfreq)
    non_tuple = [t[0] for t in sortfreq]
    print(non_tuple)

