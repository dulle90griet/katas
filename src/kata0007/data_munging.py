import pandas as pd
import re

""" CodeKata.com Kata 04: Data Munging
Available here: http://codekata.com/kata/kata04-data-munging/

Part One: Weather Data

In weather.dat you'll find daily weather data for Morristown, NJ for June 2002. Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).
"""

def find_smallest_spread():
    weather_df = pd.read_csv(
        'src/kata0007/data/weather.dat',
        sep=r"[\s*]+"
    )

    weather_df = weather_df[weather_df["Dy"] != "mo"] \
                    .convert_dtypes()
    
    weather_df["T_spread"] = weather_df["MxT"] - weather_df["MnT"]

    min_spread = weather_df["T_spread"].min()
    day = weather_df.loc[
        weather_df["T_spread"].idxmin(),
        "Dy"
    ]

    print(f"Day {day} saw the smallest temperature spread, at {min_spread} degrees.")


""" Part Two: Soccer League Table

The file football.dat contains the results from the English Premier League for 2001/2. The columns labeled 'F' and 'A' contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in 'for' and 'against' goals."""


def find_smallest_goal_difference():
    football_df = pd.read_csv(
        'src/kata0007/data/football.dat',
        sep=r"[\s-]+"
    )

    football_df = football_df.dropna(thresh=football_df.shape[1]) \
                    .convert_dtypes()
    
    football_df["goal_diff"] = abs(football_df["F"] - football_df["A"])

    min_diff = football_df["goal_diff"].min()
    team = football_df.loc[
        football_df["goal_diff"].idxmin(),
        "Team"
    ]

    print(f"{team} had the smallest difference ({min_diff}) between 'for' and 'against' goals.")


""" Part Three: DRY Fusion

Take the two programs written previously and factor out as much common code as possible, leaving you with two smaller programs and some kind of shared functionality.
"""


if(__name__ == "__main__"):
    find_smallest_spread()
    find_smallest_goal_difference()
