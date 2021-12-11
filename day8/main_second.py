import os
import re

class digit:
    def __init__(self):
        self.a = False
        self.b = False
        self.c = False
        self.d = False
# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "exm2_input.txt")
fh = open(fpath)

pattern = r".* \| (.*)"
total_sum = 0
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
    sum_line = ""
    for i in output:
        match len(i):
            case 2:
                sum_line += "1"
                continue
            case 4:
                sum_line += "4"
                continue
            case 3:
                sum_line += "7"
                continue
            case 7:
                sum_line += "8"
                continue
        if sorted(i.strip()) == sorted('cagedb'):
            sum_line += "0"
        elif sorted(i.strip()) == sorted('cdfgeb'):
            sum_line += "6"
        elif sorted(i.strip()) == sorted('cefabd'):
            sum_line += "9"
        elif sorted(i.strip()) == sorted('fcadb'):
            sum_line += "3"
        elif sorted(i.strip()) == sorted('gcdfa'):
            sum_line += "2"
        elif sorted(i.strip()) == sorted('cdfeb'):
            sum_line += "5"
    total_sum += int(sum_line)
print(total_sum)