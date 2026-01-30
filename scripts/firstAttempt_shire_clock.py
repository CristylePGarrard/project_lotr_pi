#!/usr/bin/env python3

import curses
import time
from datetime import datetime
import math

MEALS = [
        (7, 0, "Breakfast", "Mereth Amanie"),
        (9, 0, "Second Breakfast", "Mereth Attea"),
        (11, 0, "Elevenses", "Lomie Melme"),
        (13, 0, "Luncheon", "Mereth Andune"),
        (16, 0, "Afternoon Tea", "Sura Lomie"),
        (18, 0, "Dinner", "Mereth Nura"),
        (21, 0, "Supper", "Lomelindi")
        ]
def current_meal(now):
    minutes = now.hour * 60 + now.minute
    last = MEALS[0]
    for h, m, name, elvish in MEALS:
        if minutes >= h * 60 + m:
            last = (h, m, name, elvish)
    return last

def draw_clock(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        cy, cx = h // 2, w // 2
        radius = min(h, w) // 4

        now = datetime.now()
        meal = current_meal(now)

        # angle based on day progress
        total_minutes = now.hour * 60 + now.minute
        angle = (total_minutes / (24 * 60))* 2 * math.pi

        # draw circle
        for i in range(0, 360, 6):
            rad = math.radians(i)
            y = int(cy + radius * math.sin(rad))
            x = int(cx + radius * math.cos(rad))
            if 0 < y < h and 0 < x < w:
                stdscr.addstr(y, x, ".")

        # draw hand
        hy = int(cy + radius * math.sin(angle))
        hx = int(cx + radius * math.cos(angle))
        stdscr.addstr(hy, hx, ".")

        # the text
        stdscr.addstr(cy - radius - 2, cx - 10, "Meals in the Shire")
        stdscr.addstr(cy + radius + 2, cx - len(meal[2]) // 2, meal[2])
        stdscr.addstr(cy + radius + 3, cx - len(meal[3]) // 2, meal[3])

        stdscr.refresh()

        if stdscr.getch() == ord('q'):
            break

        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(draw_clock)

