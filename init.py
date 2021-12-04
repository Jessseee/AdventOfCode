import argparse
import config
import requests
import shutil

from datetime import datetime
from time import sleep
from helpers import *


parser = argparse.ArgumentParser(description='Download input and initialize solution files for AdventOfCode puzzles.')
parser.add_argument('--watch', type=bool)
args = parser.parse_args()

# Get current time in UTC
now = datetime.utcnow()

# Check if it is after midnight EST/UTC-5 (=05:00 UTC)
if args.watch:
    while now.hour < 5:
        sleep(1)  # Poll every 15 seconds
        now = datetime.utcnow()
        print('\r'+str(now.time()).split('.')[0], end='')
else:
    if now.hour < 5:
        print(color_text('There is no new puzzles yet! you have to wait until midnight EST/UTC-5.', 33))
        exit()
print('\n')

# Check if directory and file already exists
filename = f'{now.year}/day_{str(now.day).zfill(2)}.py'
if not os.path.exists(str(now.year)):
    os.mkdir(str(now.year))
elif os.path.exists(filename):
    print(color_text(f'Your solution file has already been created and can be found at ./{filename}', 33))
    exit()

# Everything is in order to set up today's puzzle solution
print(f'Let\'s get started on day {now.day}. {25 - now.day} days to go until christmas!')
shutil.copy('day_template.py', filename)

done = False
error_count = 0
while not done:
    try:
        with requests.get(
            url=f'{config.URL}/{str(now.year)}/day/{str(now.day)}/input',
            cookies={"session": config.SESSION_ID},
            headers={"User-Agent": config.USER_AGENT}
        ) as response:
            if response.ok:
                data = response.text
                input = open(f'{str(now.year)}/input/input_day_{str(now.day).zfill(2)}.txt', "w+")
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
print(color_text(f'Successfully initialized AdventOfCode working directories for day {now.day} of this years challenge!', 32))
