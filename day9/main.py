import os

# find input file
dirpath = os.path.split(os.path.realpath(__file__))[0]
fpath = os.path.join(dirpath, "input.txt")
fh = open(fpath)

def convert_int(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr
#parse 
heightmap = []
risk = 0
while True:
    line = fh.readline().strip()
    if line == '':
        fh.close()
        del fh
        del fpath
        del dirpath
        break
    heightmap.append(list(line))
heightmap = convert_int(heightmap)
low_points = 0
#do checks per number
for i,x in enumerate(heightmap):
    for index,val in enumerate(x):
        #for top left corners
        if index == 0 and i == 0:
            if heightmap[i][1] > val and heightmap[i+1][0] > val:
                low_points += 1
                risk += 1+val
        #for top right corners
        elif i == 0 and index == len(x)-1:
            if heightmap[i][index-1] > val and heightmap[i+1][index] > val:
                low_points += 1
                risk += 1+val
        #for rights
        elif index == len(x)-1 and i != 0 and i != len(heightmap):
            if heightmap[i][index-1] > val and heightmap[i+1][len(heightmap[i+1])-1] > val and heightmap[i-1][len(heightmap[i-1])-1] > val:
                low_points += 1
                risk += 1+val
        # for lefts
        elif index == 0 and i != 0 and i != len(heightmap):
            if heightmap[i][index+1] > val and heightmap[i-1][0] > val and heightmap[i+1][0] > val:
                low_points += 1
                risk += 1+val
        # for bottom lefts
        elif i == len(heightmap)-1 and index == 0:
            if heightmap[index+1] > val and heightmap[i-1][0] > val:
                low_points += 1
                risk += 1+val
        #for bottom middle
        elif i == len(heightmap)-1 and index != len(heightmap[i])-1 and index != 0:
            if heightmap[i][index-1] > val and heightmap[i][index+1] > val and heightmap[i-1][index] > val:
                low_points += 1
                risk += 1+val
        #for others
        else:
            if heightmap[i-1][index] > val and heightmap[i][index-1] > val and heightmap[i][index+1] > val and heightmap[i+1][index] > val:
                low_points += 1
                risk += 1+val
print(f"number of low points is {low_points} and risk level is {risk}")