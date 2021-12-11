import os
import re

# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "input.txt")
fh = open(fpath)

pattern = r".* \| (.*)"
# number of 1s, 4s, 7s, 8s
count1 = 0
count4 = 0
count7 = 0
count8 = 0
while True:
    line = fh.readline().strip()
    if line == '':
        fh.close()
        del dirpath
        del fpath
        del fh
        break
    m = re.match(pattern, line)
    output = m.groups()[0].split()
    for i in output:
        match len(i):
            case 2:
                count1 += 1
            case 4:
                count4 += 1
            case 3:
                count7 += 1
            case 7:
                count8 += 1
            case _:
                continue
print(count1 + count4 + count7 + count8)