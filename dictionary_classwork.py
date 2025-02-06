"""Wordcount exercise
Google's Python class
"""

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

import sys

def readfile(filename):
  wordcount = {}
  with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        words = line.lower().split()
    for word in words:
      wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount

def print_words():
  wordcount = readfile()
  for word in sorted(wordcount):
    print(word, wordcount[word])

def get_count(word_count_tuple):
  return word_count_tuple[1] 

def print_top():
  wordcount = wordcount_dict (filename)
  items = sorted(wordcount.items(), key=get_count, reverse=True)
  for item in items[:20]:
    print(item[0], item[1])

def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
