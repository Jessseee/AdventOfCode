<div align="center">
    <img src="adventofcode.jpg"/>
    <h1>Advent of Code</h1>
    <h2>Helper library</h2>
    <p>This small library helps set up a Python file for the Advent of Code puzzles and contains helper functions to load and parse inputs, and help handle common data structures.</p>
</div>



### Setup
1. Install the package using `uv`, by running `uv venv` to initialize the project with a virtual environment.
2. Next, to allow the library to fetch data from the official AoC website, retrieve your session id:
   - Login to https://adventofcode.com.
   - Open browser dev tools (F12).
   - Go to `Application -> Cookies`
   - Copy the value of the `session` cookie.
   - Paste the value into a `config.yaml` file at the root of your project:
       ```yaml 
       # <project_dir>/config.yaml
       SESSION_ID: <session_id>
       ```
3. Finally, you are all set up to start coding!

### Commands
Here are a couple of useful commands to help you get started.

- `aoc init`: Initializes a code file and downloads the puzzle input.
- `uv run <year>/day_xx.py`: Run your code on the puzzle input.
- `uv run pytest <year>/day_xx.py`: Run the tests in your code using the example inputs.
