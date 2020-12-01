from urllib.request import urlopen
import urllib.request
from os import path
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def puzzle_input(day, year='2020'):
    file_path = f'../inputs/day{day:02d}.txt'
    if not path.exists(file_path) or path.getsize(file_path) == 0:
        print('Downloading Input...')
        opener = urllib.request.build_opener()
        opener.addheaders.append(('Cookie', f'session={get_cookie()}'))
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        page = opener.open(url)

        with open(file_path, 'w') as file:
            file.write(page.read().decode('utf-8').strip())

    with open(file_path, 'r') as file:
        return file.read()


def get_cookie(file='../cookie.txt'):
    with open(file, 'r') as file:
        return file.read()


def ints(str_array, split='\n'):
    return [int(s) for s in str_array.split(split)]
