#Dictionaries
dicti = {'Matt': 20, 'Sally': 30, 'Billy': 20, 'Ben': 80, 'Alex': 50}
def add(key, value):
    dicti[key] = value
def remove(name):
    del dicti[name]
def average(dicti):
    print(sum(dicti.values()) / len(dicti))
def highest(dicti):
    print(max(dicti, key = dicti.get))
def score80(dicti):
    above = [name for name, score in dicti.items() if score > 80]
    print (above)
print (dicti)
add('Bill', 45)
print(dicti)
remove('Matt')
average(dicti)
