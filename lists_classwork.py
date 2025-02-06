"""
A, B, and D completed for 2/5 Homework
C and E completed for 2/9 Homework
"""

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
    return count

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
    return sorted(xlist) + sorted(list2) #places first list of x words at the beginning before the list of other words


# D. Given a list of numbers, return a list where 
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    finallist = [] #initializes a list
    for num in nums: #for each number in the given list
        if not finallist or num != finallist[-1]: #if list does not contain the current number
            finallist.append(num) #add the number to the list 
    return finallist #returns final list

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def last(z): #helper function to define the last element of the tuples 
    return z[-1] 
def sort_last(tuples):
    return sorted (tuples, key=last) #helper function makes the sort start from the back of the tuple


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    list1.sort()
    list2.sort()
    merged = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0)) #moves the first element of the list to the merged list and removes it   
        else:
            merged.append(list2.pop(0)) #adds element to list if it is less than the current first element in list1 
    merged.extend(list1)
    merged.extend(list2)
    return merged

def main():
#2/5 homework tests
    print (match_ends (['racecar', 'bab', 'far', 'abba']))
    print (front_x (['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
    print (remove_adjacent ([1, 1, 2, 2, 3, 3, 4])) 
#2/9 homework tests
    print (sort_last ([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
    print (linear_merge ([1, 4, 3], [2, 5, 6]))

if __name__ == '__main__':
  main()
