from tkinter import messagebox
from tkinter import *
import words

word = words.get_word()

# Colors
green = '#007d21'
yellow = '#e2e600'
black = "#000000"
white = "#FFFFFF"

guessnum = 1

root = Tk()
root.config(bg=black)
root.title("Wordle")

# Function to handle the guessing logic
def getGuess():
    global word, guessnum
    guess = wordInput.get().lower()
    guessnum += 1
    
    # Clear the input field
    wordInput.delete(0, END)
    
    # Focus on the input field to make the insertion cursor visible
    wordInput.focus()
    
    # Set the insertion cursor position to the beginning of the input field
    wordInput.icursor(0)
    
    if guessnum <= 5:
        if len(guess) == 5:
            if word == guess: # Correct guess
                messagebox.showinfo("Correct!", f"Congratulations! The word was {word.title()}")
            else:             # Incorrect guess
                for i, letter in enumerate(guess):
                    label = Label(root, text=letter.upper(), bg=black, fg=white, font=("Helvetica", 16, "bold"), width=5, height=2, bd=0, highlightthickness=2, relief="solid", highlightbackground="gray", padx=5, pady=5)
                    label.grid(row=guessnum, column=i, padx=5, pady=5)
                    
                    if letter == word[i]: # Right letter in right place
                        label.config(bg=green, fg=black)
                    elif letter in word:   # Right letter in wrong place
                        label.config(bg=yellow, fg=black)
        else:
            messagebox.showerror("Invalid Guess", "Please enter 5 characters for your guess")
    else:
        messagebox.showerror("Game Over", f"Game over! The word was {word.title()}")

# Function to restart the game
def restartGame():
    global word, guessnum
    word = words.get_word()
    guessnum = 1
    # Clear any existing labels
    for widget in root.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()
    # Clear the input field
    wordInput.delete(0, END)
    # Focus on the input field
    wordInput.focus()

# GUI elements
wordInput = Entry(root, font=("Helvetica", 16), bg=black, fg=white, insertbackground=white)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3, sticky="we")

wordGuessButton = Button(root, text="Guess", command=getGuess, bg=black, fg=white, font=("Helvetica", 14))
wordGuessButton.grid(row=999, column=3, columnspan=2, padx=5, pady=10, sticky="we")

# Create the restart button
restartButton = Button(root, text="Restart", command=restartGame, bg=black, fg=white, font=("Helvetica", 14))
restartButton.grid(row=1000, column=0, columnspan=5, padx=5, pady=(0, 10), sticky="we")

root.mainloop()
