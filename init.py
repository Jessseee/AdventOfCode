import argparse
import config
import requests
import shutil

from datetime import datetime
from time import sleep
from helpers import *


def download_input(year, day):
    """
    :param str year: The year to download input for
    :param str day: The day to download input for
    """
    done = False
    error_count = 0
    while not done:
        try:
            with requests.get(
                    url=f'{config.URL}/{year}/day/{day}/input',
                    cookies={"session": config.SESSION_ID},
                    headers={"User-Agent": config.USER_AGENT}
            ) as response:
                if response.ok:
                    data = response.text
                    input = open(f'{year}/input/input_day_{day.zfill(2)}.txt', "w+")
                    input.write(data.rstrip("\n"))
                    input.close()
                else:
                    print("        Server response for input is not valid.")
            done = True
        except requests.exceptions.RequestException:
            error_count += 1
            if error_count > config.MAX_RECONNECT_ATTEMPT:
                print("        Giving up.")
                done = True
            elif error_count == 0:
                print("        Error while requesting input from server. Request probably timed out. Trying again.")
            else:
                print("        Trying again.")
        except Exception as e:
            print("        Non handled error while requesting input from server. " + str(e))
            done = True


def init_day(year, day):
    # Check if directory and file already exists
    filename = f'{year}/day_{day.zfill(2)}.py'

    if not os.path.exists(year):
        os.mkdir(year)
    if not os.path.exists(f'{year}/input'):
        os.mkdir(f'{year}/input')

    if os.path.exists(f'{year}/input/input_day_{day.zfill(2)}.txt'):
        print(color_text(f'Your input file was already downloaded and can be found at ./{year}/input/', 33))
    else:
        download_input(year, day)

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
    parser.add_argument('--watch', default=True, action=argparse.BooleanOptionalAction)
    parser.add_argument('--date', default=None, nargs='?')
    args = parser.parse_args()

    # Initialise specific date
    if args.date is not None:
        year, day = args.date[:4], args.date[4:]
        if int(year) < 2015:
            print('There was no AdventOfCode before 2015 :(')
        elif not 1 <= int(day) <= 25:
            print('Advent of code runs from 1 Dec until 25 Dec.')
        else:
            init_day(year, day)

    # Initialise today
    else:
        # Get current time in UTC
        now = datetime.utcnow()

        # Check if it is after midnight EST/UTC-5 (=05:00 UTC)
        if args.watch:
            print('Waiting for puzzle to release:')
            while now.hour < 5:
                sleep(1)
                now = datetime.utcnow()
                print('\r'+str(now.time()).split('.')[0], end='')
        else:
            if now.hour < 5:
                print(color_text('There is no new puzzles yet! you have to wait until midnight EST/UTC-5.', 33))
                exit()
        print('\n')

        init_day(str(now.year), str(now.day))
