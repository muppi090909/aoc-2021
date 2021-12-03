import os
increased = 0
pre_i = 0
file = os.path.split(os.path.realpath(__file__))[0]
file = os.path.join(file, 'input.txt')
file = open(file)
for i in file:
    if int(i) > int(pre_i):
        increased += 1
    pre_i = i
file.close()
print(f"the depth increased {increased-1} times")
