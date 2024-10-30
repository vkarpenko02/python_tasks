#!/usr/bin/env python3

stroka = list(input())

amount_of_chars = {}
for char in stroka:
    amount_of_chars[char] = amount_of_chars.get(char, 0) + 1

result = []
for key in amount_of_chars:
    result.append(f'{key}: {amount_of_chars[key]}')

print(', '.join(result))