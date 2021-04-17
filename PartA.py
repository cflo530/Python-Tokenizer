import sys
import re

# Each function runs in O(n) time

def tokenize(filepath):
    result = []
    regex = re.compile("[a-z0-9_]*")
    
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            result.extend(regex.findall(line.lower()))
    
    return result

def computeWordFrequencies(words):
    result = {}

    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    
    return result

def printFreqs(frequencies):
    for i, j in sorted(frequencies.items(), key = lambda ij: ij[1], reverse=True):
        print(i + " => " + str(j))

if __name__ == '__main__':
    #print(len(sys.argv))
    file = tokenize(sys.argv[1])
    freqs = computeWordFrequencies(file)
    printFreqs(freqs)
    