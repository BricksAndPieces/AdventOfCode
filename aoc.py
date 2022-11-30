from urllib.request import urlopen
import urllib.request
import os
from os import path
from functools import reduce
import ssl
import sys

# Avoid certificate issues (OK because only accessing AOC)
ssl._create_default_https_context = ssl._create_unverified_context
project_path = path.dirname(path.abspath(__file__))


def create_day_file(day, year):
    # generate any missing directories
    if not path.exists(project_path + '/' + year):
        print('\u2705 Created missing directory: "' + project_path + '/' + year + '"')
        os.mkdir(project_path + '/' + year)
    for dir in ['days', 'inputs', 'samples']:
        if not path.exists(project_path + '/' + year + '/' + dir):
            print('\u2705 Created missing directory: "' + project_path + '/' + year + '/' + dir + '"')
            os.mkdir(project_path + '/' + year + '/' + dir)

    with open(project_path + '/template.txt', 'r') as file:
        template = file.read()

    template = template.replace('DAY', f'{day}').replace('YEAR', f'{year}')
    with open(project_path + f'/{year}/days/day{day:02d}.py', 'w') as file:
        file.write(template)
        print('\u2705 Created day file from template')

    # Create Empty Sample File
    sample_file = open(project_path + f'/{year}/samples/day{day:02d}.txt', 'w')
    sample_file.close()
    print('\u2705 Created empty sample file')


def puzzle_input(day, year='2020', sample=False):
    file_path = f'{project_path}/{year}/{"samples" if sample else "inputs"}/day{day:02d}.txt'
    if not sample and (not path.exists(file_path) or path.getsize(file_path) == 0):
        print('Downloading Input...')
        opener = urllib.request.build_opener()
        opener.addheaders.append(('Cookie', f'session={__get_cookie()}'))
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        print(url)
        page = opener.open(url)

        with open(file_path, 'w') as file:
            file.write(page.read().decode('utf-8').strip())

    with open(file_path, 'r') as file:
        return file.read()


def __get_cookie(file='/cookie.txt'):
    with open(project_path + file, 'r') as file:
        return file.read()


" ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- "


def timeit(some_function):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        x = some_function(*args, **kwargs)
        t2 = time.time()
        print(f'Time Taken: {t2 - t1} sec')
        return x

    return wrapper


def ints(str_array, split='\n'):
    return [int(s) for s in str_array.split(split)]


def iterate_char(c: str):
    return chr(ord(c) + 1) if c.lower() != 'z' else 'a' if c.islower() else 'A'


def mult(*args):
    return reduce(lambda x, y: x * y, *args, 1)


" ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- "

"""
Allows the user to create a python file for a puzzle based of the day and year
This is run if aoc.py is called from the command line to speed up creation of day files

Ex. python3 aoc.py 05 2021
"""
if __name__ == '__main__':
    create_day_file(int(sys.argv[1]), sys.argv[2])
