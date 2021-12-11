import os

# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "exm_input.txt")
fh = open(fpath)

#parse
file = []
while True:
    line = fh.readline().strip()
    if line == '':
        fh.close()
        del dirpath
        del fpath
        del fh
        break
    file.append([])
    file[len(file)-1].append(list(line))

# process
risk_level = 0
for i,x in enumerate(file):
    for index,val in enumerate(x):
        char = x[index]
        if char == '[':
            correct = False
            for j in x:
                if j == char:
                    correct = True
                    break
            if correct == False:
                risk_level += 57
        elif char == '(':
            correct = False
            pass
        elif char == '{':
            correct = False
            pass
        elif char == '<':
            correct = False
            pass
        else:
            continue