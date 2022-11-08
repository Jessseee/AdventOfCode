import argparse
import requests
import shutil
import yaml
from dataclasses import dataclass
from datetime import datetime
from time import sleep

from helpers import *


@dataclass
class Config:
    SESSION_ID: str
    URL: str = 'https://adventofcode.com'
    MAX_RECONNECT_ATTEMPT: int = 3

    @staticmethod
    def parse(path: str):
        """
        Parses a config.yaml file to an object.

        :param path: Path to config.yaml file.
        """
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return Config(**config)


def download_input(year: str, day: str, config: Config):
    """
    Downloads the puzzle input for a specific year and day.

    :param year: The year to download input for.
    :param day: The day to download input for.
    :param config: A Config object.
    """
    done = False
    error_count = 0
    while not done:
        try:
            print("Getting input:")
            with requests.get(
                    url=f'{config.URL}/{year}/day/{day}/input',
                    cookies={"session": config.SESSION_ID},
            ) as response:
                if response.ok:
                    data = response.text
                    with open(f'{year}/input/input_day_{day.zfill(2)}.txt', "w+") as f:
                        f.write(data.rstrip("\n"))
                else:
                    print(f"Server:\t"+color_text(f"Error {response.status_code}", 31))
            done = True
        except requests.exceptions.RequestException:
            if error_count > config.MAX_RECONNECT_ATTEMPT:
                print(f"Server:\tTried {error_count} time. Giving up!")
                done = True
            elif error_count == 0:
                print("Server:\t"+color_text(f"Error while requesting input. Request probably timed out. Trying again. (Max {config.MAX_RECONNECT_ATTEMPT} times)", 33))
            else:
                print(f"Server:\tTrying again. ({error_count})")
            error_count += 1
        except Exception as e:
            print("Server:\tNon handled error while requesting input from server. \n" + str(e))
            done = True


def init_day(year: str, day: str, config: Config):
    """
    Initializes the puzzle files for a specific year and day.

    :param year: The year to initialize puzzle for.
    :param day: The day to initialize puzzle for.
    :param config: A Config object.
    """
    filename = f'{year}/day_{day.zfill(2)}.py'

    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(f'{year}/input'):
        os.mkdir(f'{year}/input')

    if os.path.exists(f'{year}/input/input_day_{day.zfill(2)}.txt'):
        print(color_text(f'Your input file was already downloaded and can be found at ./{year}/input/', 33))
    else:
        download_input(year, day, config)

    if os.path.exists(filename):
        print(color_text(f'Your solution file was already been created and can be found at ./{year}/', 33))
    else:
        shutil.copy('day_template.py', filename)

    with open('christmas.txt', 'r') as f:
        for line in f:
            print(line, end='')
    print(color_text(f'Let\'s get started on day {day} of AdventofCode {year}!', 32))


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Download input and initialize solution file for AdventOfCode puzzle.')
    parser.add_argument('--watch', default=True, action=argparse.BooleanOptionalAction,
                        help="Whether the script should watch until the start time.")
    parser.add_argument('--config', default="config.yaml",
                        help="Path to config.yaml file to define session id.")
    parser.add_argument('--date', default=None, nargs='?',
                        help="Date in format 'YYYYDD'. Current date if not specified.")
    args = parser.parse_args()

    # Parse config file
    config = Config.parse(args.config)

    # Initialise previous date
    if args.date is not None:
        day = args.date[4:] if len(args.date) > 4 else None
        year = args.date[:4]

        if int(year) < 2015:  # No AdventOfCode yet :(
            print('There was no AdventOfCode before 2015 :(')

        if day is None:  # Initialize entire year
            for day in range(1, 26):
                init_day(args.date, day, config)

        else:  # Initialize specific day from year
            if not 1 <= int(day) <= 25:
                print('Advent of code runs from 1 Dec until 25 Dec.')
            else:
                init_day(year, day, config)

    # Initialise current day
    else:
        # Get current time in UTC
        init_time = datetime.utcnow()
        release_time = datetime.utcnow().replace(hour=5, minute=0, second=0)
        year, day = str(init_time.year), str(init_time.day)

        # Check if it is December yet
        if init_time.month != 12:
            print(color_text('It is not December! If you want to initiate a previous year please provide a date.', 33))
            exit()

        # Check if it is after midnight EST/UTC-5 (=05:00 UTC)
        if init_time.hour > 5:
            init_day(year, day, config)
        elif args.watch:
            while datetime.utcnow().hour < 5:
                sleep(1)
                until = release_time - datetime.utcnow()
                print(f"\rWaiting for day {init_time.day} puzzle to release: {str(until).split('.')[0]}", end='')
            print('\n')
            init_day(year, day, config)
        else:
            print(color_text('There is no new puzzle yet! you have to wait until midnight EST/UTC-5.', 33))
