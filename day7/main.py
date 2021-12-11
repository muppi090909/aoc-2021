import os

def max(arr):
    max = 0
    for i in arr:
        if int(i) > max:
            max = int(i)
    return max
# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "exm_input.txt")
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
    pos = pos + line.split(",")

# process
# find largest number which will be used as maximum but with +5
maximum = max(pos)
# find horizontal value but by spendin minimum fuel
minfuel = 0
#optimum position
optipos = 0
for l in range(0, len(pos)):
    pos[l] = int(pos[l])
for i in range(0, maximum+1):
    fuel = 0
    for j in pos:
        fuel += abs(j-i)
    if i == 0:
        minfuel = fuel
    if fuel < minfuel:
        minfuel = fuel
        optipos = i
print(f"optimum position:{optipos}, minimum fuel:{minfuel}")