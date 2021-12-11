import os

# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "exm_input.txt")
fh = open(fpath)

#parse
octu = []
while True:
    line = fh.readline().strip()
    if line == '':
        fh.close()
        del dirpath
        del fpath
        del fh
        break
    octu.append([])
    octu[len(octu)-1].append(list(line))
