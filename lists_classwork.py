# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0 #intializes the count 
    for word in words: #checks each word
        if len(word) >= 2 and word[0] == word[-1]: #if the word is longer than 2 letters and the first and last letter are the same
            count = count + 1 #increase the count
    print (count)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    xlist = [] #words that start with x
    list2 = [] #all other words
    for w in words:
        if w.startswith('x'):
            xlist.append(w) #adds words that start with x to first list
        else:
            list2.append(w) #adds all other words to second list 
    print (sorted(xlist) + sorted(list2)) #places first list of x words at the beginning before the list of other words


# D. Given a list of numbers, return a list where 
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    finallist = [] #initializes a list
    for num in nums: #for each number in the given list
        if not finallist or num != finallist[-1]: #if list does not contain the current number
            finallist.append(num) #add the number to the list 
    print (finallist) #prints final list


def main():
    match_ends (['racecar', 'bab', 'far', 'abba'])
    front_x (['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    remove_adjacent ([1, 1, 2, 2, 3, 3, 4])

if __name__ == '__main__':
  main()
