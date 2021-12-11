import os

# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "input.txt")
fh = open(fpath)

# parse
fish = []
while True:
    line = fh.readline().strip()
    if line == '':
        del dirpath
        del fpath
        del fh
        break
    fish = fish + line.split(",")

# process
for l in range(0, len(fish)):
    fish[l] = int(fish[l])
generations = int(input("enter the number of generations to simulate: "))
breedTargets = []
bredTargets = []
range_gen = range(0, generations-1)
del generations
for i in range_gen:
    print(i)
    for j in range(0, len(fish)):
        if j in breedTargets:
            fish[j] = 6
            continue
        elif j in bredTargets:
            continue
        else:
            fish[j] -= 1
    breedTargets = []
    bredTargets = []
    for m in range(0, len(fish)):
        if fish[m] == 0:
            breedTargets.append(m)
            fish.append(8)
            bredTargets.append(len(fish)-1)
print(len(fish))
