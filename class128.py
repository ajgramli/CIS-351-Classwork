def checkdays():
    days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") #list of days
    print (days[0], days[6]) #print the first and last days of the week
    if "Wednesday" in days: #check for Wednesday
        print ("Wednesday is a day of the week. ")
    else: 
        print ("Wednesday is not in the list of days. ")  
checkdays() 

def sorting():
    numbers = (2, 1, 3) #tuple of numbers
    numberlist = list(numbers) #convert to a list
    numberlist.sort() #sort the converted list
    numbers = tuple (numberlist) #convert back to a tuple
    print (numbers) 
sorting()
