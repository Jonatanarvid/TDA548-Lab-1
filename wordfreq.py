def tokenize(lines: list) -> list:
    words = []
    for line in lines:
        start = 0 
        while start < len(line):
            while line[start].isspace(): # Skipping blankspace characters
                start += 1
            print(line[start])
            start += 1
    return words
tokenize(['    sweet  apple  tart'])
#"The next step is to recognize what kind of word you have..."