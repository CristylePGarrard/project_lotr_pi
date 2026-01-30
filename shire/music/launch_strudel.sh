#!/bin/bash

ENCODED_CODE=$(cat ~/lotr/shire/music/shire_music_encoded.txt)

chromium \
	--new-window \
	"https://strudel.cc/?code=$ENCODED_CODE"
