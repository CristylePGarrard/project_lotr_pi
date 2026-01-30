#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime
import math

WINDOW_SIZE = 420
BG_COLOR = "#f4ecd8"     # parchment
INK_COLOR = "#3b2f2f"    # dark ink
FADED_COLOR = "#8a7f6a"  # faded ink
HAND_COLOR = "#b59b4c"   # soft gold
FILL_COLOR = "#cfe3c1"   # pale Shire green

MEALS = [
    (0, 0, "Sleepy Time", "?"),
    (7, 0, "Breakfast", "Mereth Amanië"),
    (9, 0, "Second Breakfast", "Mereth Attëa"),
    (11, 0, "Elevenses", "Lómië Melmë"),
    (13, 0, "Luncheon", "Mereth Andúnë"),
    (16, 0, "Afternoon Tea", "Súra Lómië"),
    (18, 0, "Dinner", "Mereth Núra"),
    (21, 0, "Supper", "Lómelindi"),
]

# ------------------ LOGIC ------------------

def minutes_since_midnight(now):
    return now.hour * 60 + now.minute

def meal_minutes(h, m):
    return h * 60 + m

# ------------------ UI ------------------

class ShireClock:
    def __init__(self, root):
        self.root = root
        root.title("Mealtime in the Shire")
        root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        root.resizable(False,False)

        self.canvas = tk.Canvas(
                root,
                width=WINDOW_SIZE,
                height=WINDOW_SIZE,
                bg=BG_COLOR,
                highlightthickness=0
                )
        self.canvas.pack()

        self.center = WINDOW_SIZE // 2
        self.radius = WINDOW_SIZE // 2 - 50

        self.meal_labels = []

        self.draw_static()
        self.draw_meals()
        self.update_clock()

    # ---------- STATIC DRAWING ----------

    def draw_static(self):
        self.canvas.create_oval(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            outline=INK_COLOR,
            width=3
        )

        self.canvas.create_text(
            self.center,
            28,
            text="Mealtime in the Shire",
            fill=INK_COLOR,
            font=("Serif", 16, "italic")
        )

    def draw_meals(self):
        for h, m, name, elvish in MEALS:
            minutes = meal_minutes(h, m)
            angle = (minutes / (24 * 60)) * 2 * math.pi - math.pi / 2

            x = self.center + (self.radius - 20) * math.cos(angle)
            y = self.center + (self.radius - 20) * math.sin(angle)

            label = self.canvas.create_text(
                x, y,
                text=name,
                fill=FADED_COLOR,
                font=("Serif", 10),
                tags="meal"
            )

            self.meal_labels.append((minutes, label))

    # ---------- DYNAMIC UPDATE ----------

    def update_clock(self):
        self.canvas.delete("dynamic")

        now = datetime.now()
        now_minutes = minutes_since_midnight(now)

        # ----- Highlight current meal -----
        active_meal = None
        for minutes, label in self.meal_labels:
            if now_minutes >= minutes:
                active_meal = label

            self.canvas.itemconfig(
                label,
                font=("Serif", 10),
                fill=FADED_COLOR
            )

        if active_meal:
            self.canvas.itemconfig(
                active_meal,
                font=("Serif", 14, "bold"),
                fill=INK_COLOR
            )

        # ----- Day progress fill (midnight → now) -----
        extent = (now_minutes / (24 * 60)) * 360

        self.canvas.create_arc(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            start=237,  # your adjusted angle
            extent=extent,
            fill=LIGHTER_GREEN,
            outline="",
            style=tk.PIESLICE,
            stipple="gray50",
            tags=("dynamic", "fill")
        )

        self.canvas.tag_lower("fill")

        # ----- Day progress hand -----
        angle = (now_minutes / (24 * 60)) * 2 * math.pi - math.pi / 2

        hx = self.center + self.radius * math.cos(angle)
        hy = self.center - self.radius * math.sin(angle)

        self.canvas.create_line(
                self.center,
                self.center,
                hx,
                hy,
                fill=HAND_COLOR,
                width=4,
                capstyle=tk.ROUND,
                tags="dynamic"
                )
        # center dot
        self.canvas.create_oval(
            self.center - 4,
            self.center - 4,
            self.center + 4,
            self.center + 4,
            fill=INK_COLOR,
            outline="",
            tags="dynamic"
        )

        self.root.after(60000, self.update_clock)

# ------------------ RUN ------------------

if __name__ == "__main__":
    root = tk.Tk()
    ShireClock(root)
    root.mainloop()
