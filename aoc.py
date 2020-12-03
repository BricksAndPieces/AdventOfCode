from urllib.request import urlopen
import urllib.request
from os import path
import ssl

# Avoid certificate issues (OK because only accessing AOC)
ssl._create_default_https_context = ssl._create_unverified_context


def puzzle_input(day, year='2020'):
    project_path = path.dirname(path.abspath(__file__))
    file_path = f'{project_path}/{year}/inputs/day{day:02d}.txt'
    if not path.exists(file_path) or path.getsize(file_path) == 0:
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
    project_path = path.dirname(path.abspath(__file__))
    with open(project_path + file, 'r') as file:
        return file.read()


def ints(str_array, split='\n'):
    return [int(s) for s in str_array.split(split)]
