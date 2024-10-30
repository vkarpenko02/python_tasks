#!/usr/bin/env python3
''' A script that reads the access log from a file. An output is 
the amount of user agents and the amount of requests from each of them '''


import gzip # import library to work with .gz extension


def read_file(fname):
    ''' Function to read a file content '''
    with gzip.open(fname, 'r') as file:

        agents = {}

        for line in file:
            stroka = str(line)
            if stroka.find('Mozilla') != -1 and stroka.find('GET'):
                agent = stroka[stroka.find('Mozilla'):-4]
                agents[agent] = agents.get(agent, 0) + 1

        for i, key in enumerate(agents):
            print(f'{i+1}. Agent: {key} has {agents[key]} request(s)')


if __name__ == "__main__":
    try:
        log_filename = input()
        read_file(log_filename)
    except FileNotFoundError:
        print('There is no such file')
