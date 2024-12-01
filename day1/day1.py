from itertools import count
from pathlib import Path
import numpy as np
import pandas as pd

def parse(filename: str) -> pd.DataFrame:
    data = pd.read_csv(filename, sep="   ", names=["left", "right"], engine="python")

    return data

def part1(locations_df: pd.DataFrame) -> int:
    """This does part1 of day1

    Sort lists in ascending order
    Calc difference between smallest numbers, return to new column
    Sum total differences
    """
    sorted_df = pd.DataFrame()

    sorted_df["left"] = locations_df["left"].sort_values(ignore_index=True)
    sorted_df["right"] = locations_df["right"].sort_values(ignore_index=True)

    sorted_df["difference"] = np.abs(sorted_df["left"] - sorted_df["right"])
    
    total = sorted_df["difference"].sum()

    return total

def part2(locations_df: pd.DataFrame) -> int:
    """This does part2 of day1

    Count number of times left number is in right list
    Add similarity score to new column
    Sum total differences
    """

    right_freq = locations_df["right"].value_counts()

    total = 0

    for number in locations_df["left"]:

        total += number * right_freq.get(number, default=0)

    return total

if __name__ == "__main__":
    locations_df = parse("day1_input.txt")
    print(f"Part 1 Solution: {part1(locations_df)}")
    print(f"Part 2 Solution: {part2(locations_df)}")
