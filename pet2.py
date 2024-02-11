from itertools import count
import tkinter as tk
from PIL import Image, ImageTk
import random

class ImageLabel(tk.Label):
    """A label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        
        self.delay = 100

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

# Create the main application window
root = tk.Tk()
root.title("Random Kitten Actions")

# Create a list of kitten action GIFs
kitten_actions = ["kitten_left.gif", "kitten_right.gif", "kitten_sleep.gif", "kitten_stand.gif"]

# Function to randomly change the kitten's action
def change_action():
    # Randomly select a kitten action
    action = random.choice(kitten_actions)
    # Load and display the selected action GIF
    label.load(action)
    # Schedule the next action change after 5 seconds
    root.after(5000, change_action)

# Create an instance of the ImageLabel class
label = ImageLabel(root)
label.pack()

# Start the random action changes
change_action()

# Run the application
root.mainloop()