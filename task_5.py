#!/usr/bin/env python3
''' System information '''

import argparse
import platform
import os
import http.client
import re
import psutil


parser = argparse.ArgumentParser(description="System Information Fetcher")
parser.add_argument('-d', '--distro', action='store_true', help='Get distribution information')
parser.add_argument('-m', '--memory', action='store_true', help='Get memory information')
parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU information')
parser.add_argument('-u', '--user', action='store_true', help='Get current user information')
parser.add_argument('-l', '--load', action='store_true', help='Get system load average')
parser.add_argument('-i', '--ip', action='store_true', help='Get IP address')

args = parser.parse_args()

if args.distro:
    print(f'Distro info: {platform.system()}, release {platform.release()}')

if args.memory:
    sys_mem = psutil.virtual_memory()
    print(f'Total memory: {sys_mem.total / (1024**3):>8.2f} GB, '
          f'used memory: {sys_mem.used / (1024**3):>8.2f} GB, '
          f'free memory: {sys_mem.free / (1024**3):>8.2f} GB')

if args.cpu:
    print(f'Model: {platform.processor()}')
    print(f'Cores: {psutil.cpu_count(logical=False)}')
    print(f'Logical cores: {psutil.cpu_count(logical=True)}')
    print(f'Frequency: {psutil.cpu_freq().current}')

if args.user:
    print(f'User: {os.getlogin()}')

if args.load:
    loads = os.getloadavg()
    print(f'The load average over the last:\n'
          f'  1 minute: {round(loads[0], 3)}\n'
          f'  5 minutes: {round(loads[1], 3)}\n'
          f' 15 minutes: {round(loads[2], 3)}')

if args.ip:
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    print('IP-address:', re.search(r'(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', \
                                   str(conn.getresponse().read())).group(1))
