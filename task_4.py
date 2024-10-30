#!/usr/bin/env python3
''' Count occurrences of all characters within a string '''

line = list(input("Enter a string: "))

# create a dictionary where key - char and value - amount of this char in string
amount_of_chars = {}
for char in line:
    amount_of_chars[char] = amount_of_chars.get(char, 0) + 1

# create a list with strings in format 'char': 'amount of this char'
result = []
for key in amount_of_chars:
    result.append(f'{key}: {amount_of_chars[key]}')

print(', '.join(result))