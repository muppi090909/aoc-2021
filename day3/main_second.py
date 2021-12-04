import os

def b2d(binary):
    binary = int(binary)
    length = len(str(binary))
    dv = 0
    for i in range(0, length, +1):
        fv = binary % 10
        dv = fv*2**i+dv
        binary = binary//10
        if binary == 0:
            break
    return dv

# find input file
file = os.path.split(os.path.realpath(__file__))[0]
file = os.path.join(file, 'input.txt')
file = open(file)

#my code
column_o2 = 0
column_co2 = 0
arr_co2 = file.readlines()
file.seek(0)
arr_o2 = file.readlines()
digit_len = arr_o2[0]
# remove newline char
digit_len = digit_len[0:len(digit_len)-1]
digit_len = len(digit_len)
o2 = 0
co2 = 0
#o2 loop
for i, x in enumerate(arr_o2):
    if x[len(x)-1:len(x)] == "\n":
        arr_o2[i] = x[0:len(x)-1]
del i
del x
for i, x in enumerate(arr_co2):
    if x[len(x)-1:len(x)] == "\n":
        arr_co2[i] = x[0:len(x)-1]
for a in range(0, digit_len):
    # number of zero`s
    noz = 0
    # number of one`s
    noo = 0
    for b in range(0, len(arr_o2)):
        line = arr_o2[b]
        if line[column_o2:column_o2+1] == "1":
            noo += 1
        else:
            noz += 1
    if noo > noz:
        watch = 0
        for c in range(0, len(arr_o2)):
            if arr_o2[watch][column_o2:column_o2+1] == "0":
                arr_o2.pop(watch)
            else:
                watch += 1
    elif noz > noo:
        watch = 0 
        for d in range(0, len(arr_o2)):
            if arr_o2[watch][column_o2:column_o2+1] == "1":
                arr_o2.pop(watch)
            else:
                watch += 1
    elif noz == noo:
        watch = 0
        for e in range(0, len(arr_o2)):
            if arr_o2[watch][column_o2:column_o2+1] == "0":
                arr_o2.pop(watch)
            else:
                watch += 1
    column_o2 += 1
    if len(arr_o2) == 1:
        o2 = arr_o2[0]
        o2 = (b2d(o2))
        break
for f in range(0, digit_len):
    noz = 0
    noo = 0
    for g in range(0, len(arr_co2)):
        line = arr_co2[g]
        if line[column_co2:column_co2+1] == "1":
            noo += 1
        else:
            noz += 1
    if noo > noz:
        watch = 0
        for h in range(0, len(arr_co2)):
            if arr_co2[watch][column_co2:column_co2+1] == "1":
                arr_co2.pop(watch)
            else:
                watch += 1
    elif noz > noo:
        watch = 0 
        for k in range(0, len(arr_co2)):
            if arr_co2[watch][column_co2:column_co2+1] == "0":
                arr_co2.pop(watch)
            else:
                watch += 1
    elif noz == noo:
        watch = 0
        for l in range(0, len(arr_co2)):
            if arr_co2[watch][column_co2:column_co2+1] == "1":
                arr_co2.pop(watch)
            else:
                watch += 1
    column_co2 += 1
    if len(arr_co2) == 1:
        co2 = arr_co2[0]
        co2 = (b2d(co2))
        break
print(co2*o2)