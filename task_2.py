#!/usr/bin/env python3
''' Removing duplicates and creating a tuple. Finding min and max number '''

class Task:
    def __init__(self, list_of_integers) -> None:
        self.list_of_integers = set(list_of_integers)

    @property
    def get_minimum(self):
        return f'Min value: {min(self.list_of_integers)}'
    
    @property
    def get_maximum(self):
        return f'Max value: {max(self.list_of_integers)}'
    
    @property
    def get_tuple(self):
        return tuple(self.list_of_integers)
    

if __name__ == "__main__":
    try:
        lst = [int(x) for x in input('Enter numbers separated by spaces: ').split()]

        if lst:
            obj = Task(lst)
            print(obj.get_tuple)
            print(obj.get_minimum)
            print(obj.get_maximum)
        else:
            print('No numbers provided')

    except ValueError:
        print('Invalid input')
