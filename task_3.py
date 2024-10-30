#!/usr/bin/env python3
''' A script that reads the access log from a file. An output is 
the amount of user agents and the amount of requests from each of them '''


import gzip # import library to work with .gz extension


def read_file(fname):
    ''' Function to read a file content and write the amount of agents (and their requests) 
    into the file statistics.txt'''

    with gzip.open(fname, 'r') as file, open('statistics.txt', 'w', encoding='utf-8') as otpt:

        http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD",
                        "OPTIONS", "PATCH", "CONNECT", "TRACE"]

        agents = {}

        for line in file:
            stroka = str(line)
            if stroka.find('Mozilla') != -1:
                for el in http_methods:
                    if stroka.find(el) != -1:
                        agent = stroka[stroka.find('Mozilla'):-4]
                        agents[agent] = agents.get(agent, 0) + 1
                        break

        for i, key in enumerate(agents):
            otpt.write(f'{i+1}. Agent: {key} has {agents[key]} request(s)\n')


if __name__ == "__main__":
    try:
        log_filename = input()
        read_file(log_filename)
    except FileNotFoundError:
        print('There is no such file')
