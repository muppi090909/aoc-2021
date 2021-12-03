import os
#init variables
increased = 0
pre_i = 0
#find input file
file = os.path.split(os.path.realpath(__file__))[0]
file = os.path.join(file, 'input.txt')
file = open(file)
#loop and compare
for i in file:
    if int(i) > int(pre_i):
        increased += 1
    pre_i = i
#shut down and show output
file.close()
print(f"the depth increased {increased-1} times")
