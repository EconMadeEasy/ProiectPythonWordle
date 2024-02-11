import tkinter as tk
import random
import time
from PIL import Image, ImageTk
from itertools import count

def create_window():
    """Create and configure the main window."""
    root = tk.Tk()
    root.attributes("-topmost", True)  # Set window always on top
    root.geometry("150x150")
    root.wm_attributes('-transparentcolor', '#0a0909')  # Create transparent window
    #root.overrideredirect(True)  # Remove window decorations
    return root

def move_window(root, direction):
    """Move the window in the specified direction."""
    x, y = root.winfo_x(), root.winfo_y()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    if direction == "left" and x > 0:
        root.geometry("+{}+{}".format(x - 2, y))
    elif direction == "right" and x + root.winfo_width() < screen_width:
        root.geometry("+{}+{}".format(x + 2, y))

def walk_left(root, steps):
    """Animate the cat walking left."""
    global current_image_index_left
    for _ in range(steps):
        move_window(root, "left")

def walk_right(root, steps):
    """Animate the cat walking right."""
    global current_image_index_right
    for _ in range(steps):
        move_window(root, "right")


class ImageLabel(tk.Label):
    """A label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = -1
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        
        self.delay = 1000

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

# List of GIFs for different actions
GIFS = [
    "images\SkinnyCatBitmaps\SkinnyCatWalkingLeftBitmaps\SkinniKatBlue.gif",
    "images\SkinnyCatBitmaps\SkinnyCatWalkingRightBitmaps\SkinniKatBlue.gif",
    "images\SkinniKatBlueSleeping.gif",
    "images\SkinniKatBlueStanding.gif"
]

def pick_random_action():
    """Pick a random GIF from the list of actions"""
    return random.choice(GIFS)

def display_random_action(label):
    """Display a random action on the label"""
    action = pick_random_action()
    label.load(action)

def main():
    # Create the main window
    root = create_window()
    root.title("Random Cat Actions")

    # Create the label for displaying cat actions
    cat_label = ImageLabel(root)
    cat_label.pack()

    # Function to repeatedly display random actions
    def repeat_random_action():
        display_random_action(cat_label)
        # Choose a random interval between actions (1-5 seconds)
        interval = random.randint(1000, 5000)
        root.after(interval, repeat_random_action)

    # Start displaying random actions
    repeat_random_action()

    root.mainloop()

if __name__ == "__main__":
    main()
