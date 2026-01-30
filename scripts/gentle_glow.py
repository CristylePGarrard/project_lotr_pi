#!/usr/bin/env python3

from PIL import Image, ImageEnhance

img = '~/lotr/shire/tower_eyeball.bmp'

frames = []
for i in range(20):
    enhancer = ImageEnhance.Brightness(img)
    frame = enhancer.enhance(0.8 + i * 0.02)
    frames.append(frame)

for i in range(20):
    enhancer = ImageEnhance.Brightness(img)
    frame = enhancer.enhance(1.2 - i * 0.02)
    frames.append(frame)

frames[0].save(
        "shire_gif",
        save_all=True,
        append_images= frames[1:],
        duration=80,
        loop=0
        )
