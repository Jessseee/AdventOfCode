import os
import re
import webbrowser
from dataclasses import dataclass
from datetime import datetime, UTC
from importlib.resources import as_file, files
from os import PathLike
from time import sleep

import click
import requests
import yaml

from .helpers import Color, c, Highlight

christmas = [
    c("            .-----_", Color.RED),
    c("           /  /  /\\|", Color.RED),
    c("         / /  |  \\ ", Color.RED) + c("*", Color.ORANGE),
    c("        /  /    \\ \\    ", Color.RED) + c(" A D V E N T ", Highlight.ORANGE),
    c("       / /  /   \\  \\   ", Color.RED) + c(" O F ", Highlight.GREEN) + c("C O D E ", Highlight.RED),
    c("     ./~~~~~~~~~~~~~\\.", Color.WHITE),
    c('    ( .", ^. ~".  \'.~ )', Color.WHITE),
    c("     '~~~~~~~~~~~~~~~'", Color.WHITE),
]


@dataclass
class Config:
    SESSION_ID: str
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
    error_count = 0
    while True:
        try:
            print("Getting input...")
            with requests.get(
                url=f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": config.SESSION_ID},
            ) as response:
                response.raise_for_status()
                data = response.text
                with open(f"{year}/input/input_day_{day:02d}.txt", "w+") as f:
                    f.write(data.rstrip("\n"))
                with open(f"{year}/input/example_input_day_{day:02d}.txt", "w+") as f:
                    f.write(" ")
            break
        except requests.ConnectTimeout:
            if error_count > config.MAX_RECONNECT_ATTEMPT:
                print(f"Server:\tTried {error_count} time. Giving up!")
                break
            elif error_count == 0:
                print(
                    "Server:\t"
                    + c(f"Request timed out. Trying again. (Max {config.MAX_RECONNECT_ATTEMPT} times)", 33)
                )
            else:
                sleep(2)
                print(f"Server:\tTrying again. ({error_count})")
            error_count += 1
        except requests.exceptions.HTTPError as e:
            response = e.response
            if response.status_code == 400 and "log in" in response.text:
                print("Server:\t" + c("Provide correct credentials in config.yaml.", 31))
            else:
                print("Server:\t" + c(f"{response.status_code}: {response.text}.", 31))
            break
        except Exception as e:
            print("Server:\t" + c("Unhandled error while requesting input from server:\n", 31) + str(e))
            break


def get_puzzle_title(year, day):
    with requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}"
    ) as response:
        if response.ok and (match := re.search(r"-- Day \d+: (.*) --", response.text)):
            return match.group(1)


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
        print(c(f"Input file already at {input_file}", Color.ORANGE))
    else:
        download_input(year, day, config)

    puzzle_file = f"{year}/day_{day:02d}.py"
    if os.path.exists(puzzle_file):
        print(c(f"Solution file already at {puzzle_file}", Color.ORANGE))
    else:
        puzzle_title = get_puzzle_title(year, day) or "<PUZZLE TITLE>"
        template_file = files("aoc").joinpath("day_template.py.txt")
        with (as_file(template_file) as file):
            data = file.open("r").read() \
                .replace("<YEAR>", str(year)) \
                .replace("<DAY>", f"{day:02d}") \
                .replace("<PUZZLE TITLE>", puzzle_title)
        with open(puzzle_file, "w") as file:
            file.write(data)
    os.system(f"pycharm {puzzle_file}")
    print(c(f"Let's get started on day {day} of Advent of Code {year}!", Color.GREEN))


@click.group()
def cli():
    pass


@cli.command(help="Download input and initialize solution file for Advent of Code puzzle.")
@click.argument("date", type=click.DateTime(formats=["%Y-%d", "%Y%d"]), default=datetime.today())
@click.option("--watch", is_flag=True, default=False)
@click.option("--config", default="config.yaml")
@click.option("--browser", is_flag=True, default=False)
def init(date: datetime, watch: bool, config: PathLike, browser: bool) -> None:
    """
    Initialize an Advent of Code puzzle and download the input file.

    :param date: Date of AoC puzzle to initialize.
    :param watch: Whether to wait for today's puzzle to come online.
    :param config: Config file to use for initialisation.
    :param browser: Whether to open browser on init.
    """
    config = Config.parse(config)

    # Print fun graphic
    for line in christmas:
        print(line)

    # Initialise puzzle from a previous year
    if date is not None:
        if int(date.year) < 2015:
            print(c("There was no Advent of Code before 2015 :(", Color.RED))
        elif not 1 <= date.day <= 25:
            print(c("Advent of code runs from 1 Dec. until 25 Dec.", Color.RED))
        else:
            init_day(date.year, date.day, config)
            if browser:
                webbrowser.open(f"https://adventofcode.com/{date.year}/day/{date.day}")

    # Initialise today's puzzle
    else:
        # Get current time in UTC
        init_time = datetime.now(UTC)
        release_time = datetime.now(UTC).replace(hour=5, minute=0, second=0)
        year, day = str(init_time.year), str(init_time.day)

        # Check if it is December yet
        if init_time.month != 12:
            print(c("It is not December! If you want to initiate a previous year please provide a date.", Color.ORANGE))
            exit()

        # Check if it is after midnight EST/UTC-5 (=05:00 UTC)
        if init_time.hour > 5:
            init_day(year, day, config)
        elif watch:
            while datetime.now(UTC).hour < 5:
                sleep(1)
                until = release_time - datetime.now(UTC)
                print(f"\rWaiting for day {init_time.day} puzzle to release: {str(until).split('.')[0]}", end="")
            print("\n")
            init_day(year, day, config)
        else:
            print(c("There is no new puzzle yet! you have to wait until midnight EST/UTC-5.", Color.ORANGE))
