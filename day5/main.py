import re
import os

# Globals
# regex pattern to parse input coordinates
# (x1, y1) and (x2, y2)
pattern = r"(\d+),(\d+)\s*->\s*(\d+),(\d+)\s*"
plot = []
print(plot)
maxrow = 0
maxcol = 0

# functions
def hilo(n1: int, n2: int):
    if n1 > n2:
        return (n1, n2)
    else:
        return (n2, n1)

def extend(rows: int, cols: int):

    global maxrow, maxcol, plot

    if maxrow < rows:
        for i in range(maxrow, rows):
            plot.append([])
            for j in range(0, maxcol):
                plot[i].append(0)
        maxrow = rows

    if maxcol < cols:
        for i in range(0, maxrow):
            for j in range(len(plot[i]), cols):
                plot[i].append(0)
        maxcol = cols
    return

def plotVertical(x1: int, y1: int, x2: int, y2: int):
    # sort the start and end coordinates
    (hi, lo) = hilo(y1, y2)
    # exted the plot size, if required
    # plot size is +1 of the coordinates
    # i.e. (0, 0) has size of (1, 1)
    extend(x1 + 1, hi + 1)
    # increment count for this line's plot
    for i in range(lo, hi + 1):
        plot[x1][i] += 1

def plotHorizontal(x1: int, y1: int, x2: int, y2: int):
    # sort the start and end coordinates
    (hi, lo) = hilo(x1, x2)
    # exted the plot size, if required
    # plot size is +1 of the coordinates
    # i.e. (0, 0) has size of (1, 1)
    extend(hi + 1, y1 + 1)
    # increment count for this line's plot
    for i in range(lo, hi + 1):
        plot[i][y1] += 1
def plotDiagonal(x1, y1, x2, y2):
    extend(x1+1, y1+1)
    extend(x2+1, y2+1)
    if x1 < x2:
        while x1 != x2 or y1 != y2:
            if x1 != x2:
                x1 += 1
            if y1 != y2:
                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
            extend(x1+2, y1+1)
            extend(x2+1, y2+1)
            plot[x1+1][y1-1] += 1
    elif x1 > x2:
        while x1 != x2 or y1 != y2:
            if x1 != x2:
                x1 -= 1
            if y1 != y2:
                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
            plot[x1+1][y1-1] += 1
# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "input.txt")
fh = open(fpath)

while True:
    line = fh.readline()

    # if EOF
    if line == '':
        fh.close()
        del fh
        del fpath
        del dirpath
        break

    # else, match pattern
    m = re.match(pattern, line)
    (x1, y1, x2, y2) = m.groups()
    
    print(m.groups())
    if x1 == x2:
        plotVertical(int(x1), int(y1), int(x2), int(y2))
        print("Vertical")
    elif y1 == y2:
        plotHorizontal(int(x1), int(y1), int(x2), int(y2))
        print("Horizontal")
    else:
        plotDiagonal(int(x1), int(y1), int(x2), int(y2))
        print("Diagonal")
        continue
# number of intersects
noi = 0
for i in plot:
    for j in i:
        if j > 1:
            noi += 1
print(noi)
