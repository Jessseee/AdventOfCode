from helpers import *
from datetime import datetime
import requests
import shutil
import config

now = datetime.utcnow()
date = now.date()
time = now.time()

# Check if it is actually December
if date.month < 12:
    print('It is not December yet :(')
    exit()

# Check if it is after midnight EST/UTC-5
if time.hour < 5:
    print(color_text('There is no new puzzles yet! you have to wait until midnight EST/UTC-5.', 33))
    exit()

# Check if directory and file already exists
filename = f'{date.year}/day_{str(date.day).zfill(2)}.py'
if not os.path.exists(str(date.year)):
    os.mkdir(str(date.year))
elif os.path.exists(filename):
    print(color_text(f'Your solution file has already been created and can be found at ./{filename}', 33))
    exit()

# Everything is in order to set up today's puzzle solution
print(f'Let\'s get started on day {date.day}. {25 - date.day} days to go until christmas!')
shutil.copy('day_template.py', filename)

done = False
error_count = 0
while not done:
    try:
        with requests.get(
            url=f'{config.URL}/{str(date.year)}/day/{str(date.day)}/input',
            cookies={"session": config.SESSION_ID},
            headers={"User-Agent": config.USER_AGENT}
        ) as response:
            if response.ok:
                data = response.text
                input = open(f'{str(date.year)}/input/input_day_{str(date.day).zfill(2)}.txt', "w+")
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
print(color_text(f'Successfully initialized AdventOfCode working directories for day {date.day} of this years challenge!', 32))
