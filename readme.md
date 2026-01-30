# Hello!

I hope you enjoy this little pi! :D I had fun making it! 
I know you love Lord of the Rings so I did my best to make a LOTR themed pi. 
Most of what i've done is in the console. 

Here is some info if you want to make changes. 

#### Alias's

To add or remove alias's use the following command and edit the file

```bash
vim ~/.bashrc
```

vimtutor is a great tool to learn vim. You can use nano too if you prefer that editor. 
Just type vimtutor into the console for the tutorial on how to use vim

At the bottom of the .bashrc file you'll find my lotr modifications. Alias's are short hand ways to perform commands. 

For example:
The command 'gandalf' if typed in the console will output a quote by gandalf into the console. 

To set your own aliases you add a line like this

```bash
alias gandalf='shuf -n 1 /home/samwise/lotr/quotes/gandalf_quotes.txt | pv -qL 20'
```

Now if you type gandalf in the console it will read the file it's directed to, shuffle the lines and select one. 
Then it uses pv to type the quote out at a speed of 20

The file has a quote for gandalf on each line. You can add or remove any lines you like. 
There are several other characters with quotes as well :)
You can find these files at ~/lotr/quotes

#### Console customization

Part of the console is updated in the .bashrc file where the PS1 variable is exported and the small .motd_lotr script.
The .motd_lotr script is what does the middle earth part and quote down to Imladris Terminal part

The other way is through the preferences in the LXTerminal app under the edit tab. I customized the colors with a lotr theme.  

#### Background changer
--------------------------------------------------------------------------------------------------------------------------------------
------ The gui and console aren't communicating well. I'll figure it out. But for now just use the alias to manually call the script.-
Type ahime- in the console and it will run the bash script. --------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------

The script that changes the background is random_wallpaper.sh

```bash
#!/bin/bash

# ------------------------------------------------- #
# Script randomly chooses an image from a directory
# and then updates the background with the image
# ------------------------------------------------- #

# config
WALLPAPER_DIR="/home/samwise/lotr/wallpapers"

IMAGE=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" \) | shuf -n 1)

pcmanfm --set-wallpaper=$IMAGE
```

This script sets two variables. One is the directory where the images are saved, the other is the image that is selected from the directory
It looks for files with a .jpg or .png ext, makes a list, shuffles and chooses one. Then pcmanfm sets the image as the wallpaper

I also wrote a python script to randomly run the shell script

```python
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
```

the random_number function needs two variables an min integar and a max integar. in the script it's set from 0-3, but can be modified if the chance of a change needs to go up or down

#### music

I tried to make a cute little musical experience but it's not working. there are a few scripts that aren't running. But if you want to hear the melody the shire_music.js is the code just copy and paste into https://strudel.cc and press play :) 

#### Shire Clock

shire_clock.py creates a little app that has a clock with mealtimes in the shire. 
if you type 'mealtime' in the console it will activate it. To close it click the x on the window that pops up.

#### pygame
i wanted to make a cute game or graphic that could play but it's still in development. You can see a little eyeball tower with flames if you run the eyeball_tower.py script in the scripts directory. The sample_game.py files is just a smaple pygame where you use the asdw keys to move a red circle around the screen. I left it cause it's kind of fun. But it serves no purpose beyond that.

#### Other Aliases
| Alias | Information |
|-------|-------------|
|fellowship|Activates htop which gives an overview of the computer.  f10 or ctrl + c will close htop|
|lembas|Updates all the dependencies and libraries. runs ``` sudo apt update && sudo apt upgrade ```|
|shire| Moves to your home directory ``` cd ~ ```|
|mordor|Moves to your root directory ``` cd /```|
|ahime-|Changes the wallpaper - runs random_wallpaper.sh|
|mealtime|Activates the mealtimes in the shire clock - runs the shire_clock.py script|



