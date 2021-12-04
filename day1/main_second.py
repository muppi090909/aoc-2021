import os
from linkedlist import LinkedList, Node
# find input file
file = os.path.split(os.path.realpath(__file__))[0]
file = os.path.join(file, 'input.txt')
file = open(file)
counter = 0
for d in file:
    if counter == 0:
        depths = LinkedList(Node(int(d)))
    else:
        depths.insert_end(Node(int(d)))
    counter += 1
del counter
#my code
compares = []
swA = 0
swB = 0
for i in range(0, len(depths)-2):
    #sliding window A
    swA = depths.get(i).dataval + depths.get(i+1).dataval + depths.get(i+2).dataval
    #sliding window A
    swB = depths.get(i+1).dataval + depths.get(i+2).dataval + depths.get(i+3).dataval
    if swA < swB:
        compares.append(True)
    else: 
        compares.append(False)
increases = 0
for j in compares:
    if j == True:
        increases += 1
    else:
        continue
print(increases)