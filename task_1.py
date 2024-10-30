#!/usr/bin/env python3
''' this is about cheching does the file has extension '''


def get_file_extension(fname):
    ''' 
    function for checking file extension
    '''
    ext = fname.split('.')
    try:
        if len(ext) == 2:
            return f'The file extension is: {ext[-1]}'
        raise ValueError()
    except ValueError:
        return 'No such extension'


if __name__ == "__main__":
    filename = input("Enter the file name: ")
    print(get_file_extension(filename))
