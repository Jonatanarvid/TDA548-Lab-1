import sys
import wordfreq
import urllib.request

eng_stop_words_file = open(sys.argv[1], encoding="utf-8")
stop_words = [word.strip() for word in eng_stop_words_file]
eng_stop_words_file.close()

if "http://" in sys.argv[2] or "https://" in sys.argv[2]:
    response = urllib.request.urlopen(sys.argv[2])
    lines_of_words = response.read().decode("utf8").splitlines()
else:
    word_file = open(sys.argv[2], encoding="utf-8")
    lines_of_words = [line.strip() for line in word_file]
    word_file.close()

n = int(sys.argv[3])

def main(stop_words: list, lines_of_words: list, n: int) -> None:
    tokenized_list = wordfreq.tokenize(lines_of_words)
    count = wordfreq.countWords(tokenized_list, stop_words)
    wordfreq.printTopMost(count, n)

main(stop_words, lines_of_words, n)