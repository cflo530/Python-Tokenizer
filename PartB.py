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

def commonFreqs(freq1, freq2):
    result = {}
    inCommon = set(freq1.keys() & set(freq2.keys()))

    for word in inCommon:
        result[word] = freq1[word] + freq2[word]
    
    return result

def printCommon(dict):
    for word in dict:
        print(word)
    print(str(len(dict)))

if __name__ == '__main__':
    file1 = tokenize(sys.argv[1])
    file2 = tokenize(sys.argv[2])

    file1_freqs = computeWordFrequencies(file1)
    file2_freqs = computeWordFrequencies(file2)

    fileFreqs = commonFreqs(file1_freqs, file2_freqs)
    printCommon(fileFreqs)