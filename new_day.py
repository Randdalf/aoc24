#!/usr/bin/env python

"""
Generates Advent of Code skeleton solution and input.
"""

import aocd
import argparse
import datetime
import pathlib

template = '''import aoc

export fn part1(input):
    pass

export fn part2(input):
    pass

if is_main():
    aoc.solve({day}, part1, part2)
'''


def write_file(filename, contents):
    if not pathlib.Path(filename).exists():
        with open(filename, 'wt') as file:
            file.write(contents)
            print(f'Created {filename}')
    else:
        print(f'{filename} already exists')


def write_solution(day, year):
    skeleton = template.format(day=day, year=year)
    write_file(f'd{day:02d}.gum', skeleton)


def write_input(day, year):
    input = aocd.get_data(day=day, year=year)
    write_file(f'd{day:02d}.txt', input)


def main(args):
    now = datetime.datetime.now()
    year = args.year or now.year
    day = args.day or now.day
    write_solution(day, year)
    write_input(day, year)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generates Advent of Code skeleton solution and input.')
    parser.add_argument('-y', '--year', type=int, default=None,
                        help='manual year override')
    parser.add_argument('-d', '--day', type=int, default=None,
                        help='manual day override')
    main(parser.parse_args())
