import os
import numpy as np

def max(arr):
    max = 0
    for i in arr:
        if int(i) > max:
            max = int(i)
    return max


# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "input.txt")
fh = open(fpath)

# parse
pos = []
while True:
    line = fh.readline().strip()
    if line == '':
        del dirpath
        del fpath
        del fh
        break
    pos += line.split(",")

# process
# find largest number which will be used as maximum but with +5
maximum = max(pos)
# find horizontal value but by spendin minimum fuel
minfuel = 0
# optimum position
optipos = 0
for l in range(0, len(pos)):
    pos[l] = int(pos[l])
pos = np.array(pos)
for i in range(0, maximum+1):
    fuel = 0
    for j in pos:
        fuelrate = 1
        for m in range(0, abs(j-i)):
            fuel += fuelrate
            fuelrate += 1
    if fuel < minfuel:
        minfuel = fuel
        optipos = i
    if i == 0:
        minfuel = fuel
print(f"optimum position:{optipos}, minimum fuel:{minfuel}")
