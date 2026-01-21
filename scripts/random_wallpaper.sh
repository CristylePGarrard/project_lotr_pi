#!/bin/bash

# -------------------------------------------------- #
# Script randomly chooses and image from a directory
# and then updates the background with the img. 
# -------------------------------------------------- #

# --- config ---
WALLPAPER_DIR="/path/to/directory"

IMAGE=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" \) | shuf -n 1)

pcmanfm --set-wallpaper="$IMAGE"

