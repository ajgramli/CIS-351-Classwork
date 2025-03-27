"""
CIS 351 Midterm Exam
Arthur Gramlich
"""

"""Write a Python function that takes a string and returns the string reversed."""

def reverse():
    string = input("Please enter a word or phrase to be reversed. ") 
    reversed_string = string[::-1] #reverses from the back of the string
    return reversed_string

print(reverse()) 

"""Write a Python script that reads a text file and counts the frequency of each word in the file. The script should print the word frequencies in descending order."""

import os

os.chdir(r"C:\Users\GRAMLICH\Desktop\VsCode")  

def readfile(filename):
    count = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.lower().strip().split()
                for word in words:
                    count[word] = count.get(word, 0) + 1  #Increments the word count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    
    return count

def CountWords(count):
    if count is None:
        return
    sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)  #Sorts by frequency
    
    for word, freq in sorted_counts:
        print(f"{word}: {freq}") 

filename = "Midterm.txt"  
word_count = readfile(filename)  
CountWords(word_count)

"""Write a Python function that takes two arguments, a list and a number, and returns a new list with the number added to each element of the original list."""

def adding(lst, num):
    numbers = []
    for x in lst:
        numbers.append(x + num) 
    return numbers

print(adding([1, 2, 3, 4], 1)) #expecting [2, 3, 4, 5] 