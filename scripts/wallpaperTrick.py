#!/usr/bin/env python3

# ----------------------------------------------------------------- #
# This script selects a random number witin a specified range
# if the number == 1 then a shell script is ran
# The shell script changes the background to a random img from a dir
# ------------------------------------------------------------------ #

import os
import random
import subprocess

# path to shell script
script_path = "/home/samwise/lotr/scripts/random_wallpaper.sh"

# function to choose random number within a range
def random_number(min_num, max_num):
    num_array=range(min_num, max_num)
    rand_value = random.choice(num_array)
    return rand_value

rand_num = random_number(0,3)

if rand_num == 1:
    try:
        result = subprocess.run(script_path, capture_output=True, text=True, shell=False)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Exit Code:", result.returncode)
    except subprocess.CalledProcessError as e:
        print(f"Script failed with exit code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print(f"Error: The script file was not found at {script_path}")
else:
    print(f"Number is {str(rand_num)}")

