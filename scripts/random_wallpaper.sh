#!/bin/bash

# ------------------------------------------------- #
# Script randomly chooses an image from a directory
# and then updates the background with the image
# ------------------------------------------------- #

# config
WALLPAPER_DIR="/home/samwise/lotr/wallpapers"

IMAGE=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" \) | shuf -n 1)

pcmanfm --set-wallpaper=$IMAGE
