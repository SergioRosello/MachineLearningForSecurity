import fileinput

for line in fileinput.input("./sorted_network_traffic.csv", inplace=True):
    character_count = 0
    for character in line:
        modified_line = line
        if character == ',': character_count = character_count + 1
        if character == ',' and character_count > 5:
            continue
        else:
            print('{}'.format(character), end='') # for Python 3
