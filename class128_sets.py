#Sets
s1 = {3, 1, 9, 7, 6}
s2 = {2, 4, 5, 6, 8}
print (s1) 
print (s2)
union = s1.union(s2)
intersection = s1.intersection(s2)
diff1 = s1.difference(s2)
diff2 = s2.difference(s1)
print(union)
print(intersection)
print(diff1)
print(diff2)
s1.add(4)
print (s1) #prints s1 with 4
s2.remove (4)
print(s2) #prints with 4 removed