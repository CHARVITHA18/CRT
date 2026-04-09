#here we use set and dict for searching in Python
#FREQuency counting   aabbcc

def frequency_count(s):
    d={}
    for ch in s:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
    return d
print(frequency_count("aabbccfjenjkdsfhkuegkf")) 

