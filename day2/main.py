def i_int(i):
    try:
        i_int = int(i)
        return True
    except:
        return False


# init variables
depth = 0
horizontal = 0
raw_commands = input()
commands = raw_commands.split()
for i in commands:
    i_can_be_int = i_int(i)
    if i_can_be_int == True:
        match command:
            case "forward":
                horizontal += int(i)
            case "up":
                depth -= int(i)
            case "down":
                depth += int(i)
            case _:
                print("invalid")
                exit(1)
    else:
        command = i
print(depth*horizontal)