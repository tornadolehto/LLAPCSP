with open('Pseudo English/training-data.txt') as file:
    data = file.read()
characters = set(char for char in data)

def substrings(s,depth):
    res = []
    for length in range(2,depth+1):
        for charindex in range(length,len(s)):
            cur = s[charindex:charindex+length]
            res.append(cur)
            print(cur)
    return res
substringsdata = substrings(data,3)

