import tkinter as tk
import math
from datetime import datetime

# ------------------ CONFIG ------------------

WINDOW_SIZE = 420
BG_COLOR = "#f4ecd8"     # parchment
INK_COLOR = "#3b2f2f"    # dark ink
HAND_COLOR = "#b59b4c"   # soft gold

MEALS = [
    (7, 0,  "Breakfast",        "Mereth Amanië"),
    (9, 0,  "Second Breakfast", "Mereth Attëa"),
    (11, 0, "Elevenses",        "Lómië Melmë"),
    (13, 0, "Luncheon",         "Mereth Andúnë"),
    (16, 0, "Afternoon Tea",    "Súra Lómië"),
    (18, 0, "Dinner",           "Mereth Núra"),
    (21, 0, "Supper",           "Lómelindi"),
]

# ------------------ LOGIC ------------------

def current_meal(now):
    minutes = now.hour * 60 + now.minute
    last = MEALS[0]
    for h, m, name, elvish in MEALS:
        if minutes >= h * 60 + m:
            last = (name, elvish)
    return last

# ------------------ UI ------------------

class ShireClock:
    def __init__(self, root):
        self.root = root
        root.title("Shire Reckoning")
        root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        self.center = WINDOW_SIZE // 2
        self.radius = WINDOW_SIZE // 2 - 40

        self.draw_static()
        self.update_clock()

    def draw_static(self):
        # Outer circle
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
            30,
            text="Shire Reckoning",
            fill=INK_COLOR,
            font=("Serif", 16, "italic")
        )

    def update_clock(self):
        self.canvas.delete("dynamic")

        now = datetime.now()
        meal, elvish = current_meal(now)

        # Angle: progress through day
        minutes = now.hour * 60 + now.minute
        angle = (minutes / (24 * 60)) * 2 * math.pi - math.pi / 2

        hx = self.center + self.radius * math.cos(angle)
        hy = self.center + self.radius * math.sin(angle)

        # Hand
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

        # Center dot
        self.canvas.create_oval(
            self.center - 4,
            self.center - 4,
            self.center + 4,
            self.center + 4,
            fill=INK_COLOR,
            outline="",
            tags="dynamic"
        )

        # Meal text
        self.canvas.create_text(
            self.center,
            WINDOW_SIZE - 80,
            text=meal,
            fill=INK_COLOR,
            font=("Serif", 16),
            tags="dynamic"
        )

        self.canvas.create_text(
            self.center,
            WINDOW_SIZE - 55,
            text=elvish,
            fill=INK_COLOR,
            font=("Serif", 12, "italic"),
            tags="dynamic"
        )

        self.root.after(60000, self.update_clock)  # update every minute

# ------------------ RUN ------------------

if __name__ == "__main__":
    root = tk.Tk()
    ShireClock(root)
    root.mainloop()
