#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime
import math

WINDOW_SIZE = 420
BG_COLOR = "#F4ECDF" # parchment
INK_COLOR = "#012E34" # dark ink
HAND_COLOR = "#556B00" # soft gold
FADED_COLOR = '#8a7f6a' # faded ink
SUN_COLOR = "#d4b25c" # warm sun gold
STAR_COLOR = "#8faecb" # soft starlight



MEALS = [
        (7, 0, "Breakfast", "Mereth Amanie"),
        (9, 0, "Second Breakfast", "Mereth Attea"),
        (11, 0, "Elevenses", "Lomie Melme"),
        (13, 0, "Luncheon", "Mereth Andune"),
        (16, 0, "Afternoon Tea", "Sura Lomie"),
        (18, 0, "Dinner", "Mereth Nura"),
        (21, 0, "Supper", "Lomelindi")
        ]

# -------------- logic --------------
def minutes_since_midnight(now):
    return now.hour *60 + now.minute

def meal_minutes(h,m):
    return h* 60 + m

# ----------------ui-----------------

class ShireClock:
    def __init__(self, root):
        self.root = root
        root.title("Mealtime")
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

        self.center = WINDOW_SIZE //2
        self.radius = WINDOW_SIZE // 2 - 50
        
        self.meal_labels = []

        self.draw_static()
        self.draw_meals()
        self.update_clock()

# ------------static drawing ----------
    def draw_static(self):
        # outer circle
        self.canvas.create_oval(
                self.center - self.radius,
                self.center - self.radius,
                self.center + self.radius,
                self.center + self.radius,
                outline=INK_COLOR,
                width=3
                )
        # Title
        self.canvas.create_text(
                self.center,
                28,
                text="Meal Time",
                fill=INK_COLOR,
                width=3
                )

    def draw_meals(self):
        for h,m,name, elvish in MEALS:
            minutes = meal_minutes(h, m)
            angle = (minutes / (24*60)) * 2 * math.pi - math.pi/2
            x = self.center + (self.radius - 20) * math.cos(angle)
            y = self.center + (self.radius - 20) * math.sin(angle)

            label = self.canvas.create_text(
                    x, y,
                    text=name,
                    fill=FADED_COLOR,
                    font=("Serif", 19),
                    tags="meal"
                    )
            self.meal_labels.append((minutes, label))

    # ---------- dynamic update ----------

    def update_clock(self):
        self.canvas.delete("dynamic")

        now = datetime.now()
        now_minutes = minutes_since_midnight(now)
        active_meal = None
        for minutes, label in self.meal_labels:
            if now_minutes >= minutes:
                active_meal = label
                self.canvas.itemconfig(
                        label,
                        font={"Serif", 10},
                        fill=FADED_COLOR
                        )

        if active_meal:
            self.canvas.itemconfig(
                    active_meal,
                    font=("Serif", 14, "bold"),
                    fill=INK_COLOR
                    )
    # ------ day progress hand --------
        angle = (now_minutes / (24 * 60)) * 2 * math.pi - math.pi/2

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
                self.center -4,
                self.center +4,
                self.center +4,
                fill=INK_COLOR,
                outline="",
                tags="dynamic"
                )

        self.root.after(60000, self.update_clock)
            

# ------ run it

if __name__ == "__main__":
    root = tk.Tk()
    ShireClock(root)
    root.mainloop()
