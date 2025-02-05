#A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  if count >= 10: #checks for the amount of donuts
    print ("Number of Donuts: Many") #More than 10 donuts is many
  else:
    print (f"Number of Donuts: {count}") #less than 10 donuts prints amount of donuts



# MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    print (b[:2] + a[2:] + " " + a[:2] + b[2:]) #changes the first letter of each word to the other word by changing the letter in the slot

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) >= 3: #checks of the string is longer than 3 letters
        if s[-3:] != 'ing': #if it does not already contain 'ing'
            s = s + 'ing' #add 'ing'
        else: #if it contains 'ing'
            s = s + 'ly' #add 'ly'
    print (s)

def main():
  donuts(5)
  donuts(25)
  mix_up('mix', 'pod')
  mix_up('dog', 'dinner')  
  verbing('love')
  verbing('loving')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
