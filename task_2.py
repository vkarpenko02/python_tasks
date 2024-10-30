#!/usr/bin/env python3
''' Removing duplicates and creating a tuple. Finding min and max number '''

class Task:
    ''' Class Task that has properties for getting minimum, maximum and converting list to tuple '''
    def __init__(self, list_of_integers) -> None:
        self.list_of_integers = set(list_of_integers)

    @property
    def get_minimum(self):
        ''' Function returns the minimum '''
        return f'Min value: {min(self.list_of_integers)}'

    @property
    def get_maximum(self):
        ''' Function returns the maximum '''
        return f'Max value: {max(self.list_of_integers)}'

    @property
    def get_tuple(self):
        ''' Function returns tuple'''
        return tuple(self.list_of_integers)


if __name__ == "__main__":
    try:
        # make a list from inputed numbers
        # if user inputed not a number, ValueError will occur
        lst = [int(x) for x in input('Enter numbers separated by spaces: ').split()]

        # if list is not empty next code will be executed
        if lst:
            obj = Task(lst)
            print(obj.get_tuple)
            print(obj.get_minimum)
            print(obj.get_maximum)
        else:
            print('No numbers provided')

    except ValueError:
        print('Invalid input')
