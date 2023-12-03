from dataclasses import dataclass
from datetime import datetime
from os import PathLike
from time import sleep

import click
import requests
import yaml

from .helpers import *

christmas = rf"""
            .-----_
           /  /  /\|
         / /  |  \ {c('*', Color.ORANGE)}
        /  /    \ \      {c(' A D V E N T ', Highlight.ORANGE)}
       / /  /   \  \     {c(' O F ', Highlight.GREEN)}{c('C O D E ', Highlight.RED)}
     ./~~~~~~~~~~~~~\.
    ( .", ^. ~".  '.~ )
     '~~~~~~~~~~~~~~~'

"""


@dataclass
class Config:
    SESSION_ID: str
    URL: str = "https://adventofcode.com"
    MAX_RECONNECT_ATTEMPT: int = 3

    @staticmethod
    def parse(path: str):
        """
        Parses a config.yaml file to an object.

        :param path: Path to config.yaml file.
        """
        with open(path, "r") as file:
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
            print("Getting input...")
            with requests.get(
                url=f"{config.URL}/{year}/day/{day}/input",
                cookies={"session": config.SESSION_ID},
            ) as response:
                if response.ok:
                    data = response.text
                    with open(f"{year}/input/input_day_{day:02d}.txt", "w+") as f:
                        f.write(data.rstrip("\n"))
                    with open(f"{year}/input/example_input_day_{day:02d}.txt", "w+") as f:
                        pass
                else:
                    print(f"Server:\t" + c(f"Error {response.status_code}", 31))
            done = True
        except requests.exceptions.RequestException:
            if error_count > config.MAX_RECONNECT_ATTEMPT:
                print(f"Server:\tTried {error_count} time. Giving up!")
                done = True
            elif error_count == 0:
                print(
                    "Server:\t"
                    + c(
                        f"Error while requesting input. Request probably timed out. Trying again. "
                        f"(Max {config.MAX_RECONNECT_ATTEMPT} times)",
                        33,
                    )
                )
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
    os.makedirs(f"{year}/input", exist_ok=True)

    input_file = f"{year}/input/input_day_{day:02d}.txt"
    if os.path.exists(input_file):
        print(c(f"Input file already at " f"./{year}/input/{input_file}", Color.ORANGE))
    else:
        download_input(year, day, config)

    puzzle_file = f"{year}/day_{day:02d}.py"
    if os.path.exists(puzzle_file):
        print(c(f"Solution file already at " f"./{year}/{puzzle_file}", Color.ORANGE))
    else:
        with open("day_template.py", "r") as file:
            data = file.read().replace("<YEAR>", str(year)).replace("<DAY>", str(day))
        with open(puzzle_file, "w") as file:
            file.write(data)

    print(c(f"Let's get started on day {day} of AdventofCode {year}!", Color.GREEN))


@click.group()
def cli():
    pass


@cli.command(help="Download input and initialize solution file for AdventOfCode puzzle.")
@click.option("--date", type=click.DateTime(), default=datetime.today())
@click.option("--watch", is_flag=True, default=False)
@click.option("--config", default="config.yaml")
def init(date: datetime, watch: bool, config: PathLike):
    """
    Initialize an Advent of Code puzzle and download the input file.

    :param date: Date of AoC puzzle to initialize.
    :param watch: Whether to wait for today's puzzle to come online.
    :param config: Config file to use for initialisation.
    """
    config = Config.parse(config)

    # Print fun graphic
    for line in christmas:
        print(line, end="")

    # Initialise puzzle from a previous year
    if date is not None:
        if int(date.year) < 2015:
            print(c("There was no AdventOfCode before 2015 :(", Color.RED))
        elif not 1 <= date.day <= 25:
            print(c("Advent of code runs from 1 Dec until 25 Dec.", Color.RED))
        else:
            init_day(date.year, date.day, config)

    # Initialise today's puzzle
    else:
        # Get current time in UTC
        init_time = datetime.utcnow()
        release_time = datetime.utcnow().replace(hour=5, minute=0, second=0)
        year, day = str(init_time.year), str(init_time.day)

        # Check if it is December yet
        if init_time.month != 12:
            print(c("It is not December! If you want to initiate a previous year please provide a date.", Color.ORANGE))
            exit()

        # Check if it is after midnight EST/UTC-5 (=05:00 UTC)
        if init_time.hour > 5:
            init_day(year, day, config)
        elif watch:
            while datetime.utcnow().hour < 5:
                sleep(1)
                until = release_time - datetime.utcnow()
                print(f"\rWaiting for day {init_time.day} puzzle to release: {str(until).split('.')[0]}", end="")
            print("\n")
            init_day(year, day, config)
        else:
            print(c("There is no new puzzle yet! you have to wait until midnight EST/UTC-5.", Color.ORANGE))
