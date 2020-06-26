import sys
import re
import pandas as pd 
import fileinput

def delete_extra_commas(file_name):
    for line in fileinput.input(file_name, inplace=True):
        character_count = 0
        for character in line:
            if character == ',': character_count = character_count + 1
            if character == ',' and character_count > 5:
                continue
            else:
                print('{}'.format(character), end='')

def remove_null_values(file_name):
    for line in fileinput.input(file_name, inplace=True):
        previous_character_is_comma = False
        for character in line:
            if character == ',' and previous_character_is_comma:
                print('{}'.format('UNKNOWN'), end='')
            previous_character_is_comma = False
            print('{}'.format(character), end='')
            if character == ',': previous_character_is_comma = True     

if len(sys.argv) == 1:
    print("Usage: sanitize.py {file}")
    exit()

for file_name in sys.argv[1:]:
    print("Processing ", file_name)
    delete_extra_commas(file_name)
    remove_null_values(file_name)
    # delete_invalid_entries(file_name)

