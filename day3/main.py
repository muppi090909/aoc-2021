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
# my code
# most ocurring bit
inputs = file.readlines()
gamma = ""
column_gamma = 0
column_epsilon = 0
digit_len = inputs[0]
# remove newline char
digit_len = digit_len[0:len(digit_len)-1]
digit_len = len(digit_len)
# gamma loop
for j in range(0, digit_len):
    # number of zero`s
    noz = 0
    # number of one`s
    noo = 0
    for d in range(0, len(inputs)):
        line = inputs[d]
        if d != len(inputs)-1:
            line = line[0:len(line)-1]
        if line[column_gamma:column_gamma+1] == "1":
            noo += 1
        else:
            noz += 1
    column_gamma += 1
    if noo < noz:
        gamma = gamma + "0"
    else:
        gamma = gamma + "1"
# epsilon loop
epsilon = ""
file.seek(0)
for g in range(0, digit_len):
    # number of zero`s
    noz = 0
    # number of one`s
    noo = 0
    for m in range(0, len(inputs)):
        line = inputs[m]
        if m != len(inputs)-1:
            line = line[0:len(line)-1]
        if line[column_epsilon:column_epsilon+1] == "1":
            noo += 1
        else:
            noz += 1
    column_epsilon += 1
    if noz < noo:
        epsilon = epsilon + "0"
    else:
        epsilon = epsilon + "1"
gamma = b2d(gamma)
epsilon = b2d(epsilon)
print(gamma*epsilon)
file.close()