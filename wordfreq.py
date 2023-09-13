import sys
import urllib.request

def tokenize(lines: list) -> list:
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            # Skipping blankspace characters
            while start < len(line) and line[start].isspace():
                start += 1
            
            end = start
            while end < len(line) and line[end].isdigit():
                end += 1

            # If the above while loop has not been run, then end = start. We check this because i.e "15th" should be split into 2 words
            if end == start:
                while end < len(line) and line[end].isalpha():
                    end += 1
          
            # If the word is not an empty string, append it to the list in lowercase
            if start != end:
                words.append(line[start:end].lower())

            # Makes sure symbols are added aswell
            if end < len(line) and not (line[end].isalpha() or line[end].isdigit() or line[end].isspace()):
                words.append(line[end])
                end += 1

            start = end

    return words

def countWords(words: list, stopWords: list) -> dict:
    count = {}
    for word in words:
        if word not in stopWords:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count

def printTopMost(frequencies: dict, n: int) -> None:
    # Convert the dictionary to a list of tuples
    value_pairs = list(frequencies.items())

    # Sort the tuples in descending order
    sorted_value_pairs = sorted(value_pairs, key=lambda x: -x[1])

    # print the n number of highest word frequencies
    if not n > len(value_pairs):
        for i in range(n):
            print(sorted_value_pairs[i][0].ljust(20) + str(sorted_value_pairs[i][1]).rjust(5))
