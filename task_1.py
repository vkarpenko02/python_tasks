#!/usr/bin/env python3
''' this  is about cheching does the file has extension '''

import mimetypes


class NotAnExtension(Exception):
    ''' Exception if there is no such extension '''

class InvalidInput(Exception):
    ''' This input is invalid '''

def get_file_extension(fname):
    ''' 
    function for checking file extension
    '''
    extensions = mimetypes.types_map.keys() # all extensions
    ext = fname.split('.')

    #  checking if the input is correct
    try:
        if fname[0] == '.' or len(ext) < 2:
            raise InvalidInput('Invalid Input')
    except InvalidInput as err:
        return err
    
    # checking if there is such extension
    try:
        if f'.{ext[-1]}' in extensions:
            return f'The file extension is: {ext[-1]}'
        raise NotAnExtension('There is no such extension')
    except NotAnExtension as err:
        return err


if __name__ == "__main__":
    filename = input("Enter the file name: ")
    if len(filename) > 0:
        print(get_file_extension(filename))
    else:
        print('Empty input')
