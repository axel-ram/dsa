

def naivePatternFinding(string, pattern):
    n = len(string)
    k = len(pattern)
    if n<k:
        return index
    for i in range(n+k-1):
        j = 0
        while(j<k):
            if pattern[j] != string[i+j]:
                break
            j += 1
        if j==k:
            return i
    return -1
    

text = 'this is a test string'
pattern = 'test'
print(naivePatternFinding(text, pattern))