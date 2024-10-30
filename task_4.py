#!/usr/bin/env python3
''' Count occurrences of all characters within a string '''

try:
    line = list(input("Enter a string: "))
    if not line:
        raise ValueError('The string is empty')
    
    # create a dictionary where key - char and value - amount of this char in string
    amount_of_chars = {}
    for char in line:
        if char != ' ':
            char = char.lower()
            amount_of_chars[char] = amount_of_chars.get(char, 0) + 1

    # create a list with strings in format 'char': 'amount of this char'
    result = []
    for key in amount_of_chars:
        result.append(f'{key}: {amount_of_chars[key]}')

    print(', '.join(result))
    
except ValueError as err:
    print(err)