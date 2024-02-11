### words.py Script

#### Importing Libraries
```python
import random
```
Here we import the `random` module to generate random numbers for selecting a word from the list.

#### List of Words
```python
words = """a
ability
able
about
above
accept
according
account
across
act
action
# ... More words ...
your
yourself"""
```
A long string containing a list of words, each separated by a newline character.

#### Splitting Words
```python
wordsList = words.split('\n')
```
We split the long string into a list of words using the newline character as a separator.

#### Filtering Words
```python
outputWordsList = []

for i in range(len(wordsList) - 1):
    selected = wordsList[i]
    
    if "".join(dict.fromkeys(selected)) == selected and len(selected) == 5:
        # Check if there are any repeating letters and if the length of the word is 5
        
        outputWordsList.append(selected)
```
We iterate through each word in the list, checking if it has repeating letters and if its length is 5. If so, we add it to the `outputWordsList`.

#### Function to Get a Word
```python
def get_word():
    return random.choice(outputWordsList)
```
This function returns a random word from the filtered list of words.

### main.py Script

#### Importing Libraries
```python
from tkinter import messagebox
from tkinter import *
import words
```
We import the necessary modules from the tkinter library for creating the GUI, and we import the `words` module to get a random word for the game.

#### Initializing Game Variables
```python
word = words.get_word()
guessnum = 1
```
We initialize the `word` variable by getting a random word using the `get_word()` function from the `words` module. `guessnum` keeps track of the number of guesses.

#### Creating the GUI Window
```python
root = Tk()
root.config(bg=black)
root.title("Wordle")
```
We create the main tkinter window with a black background and set its title to "Wordle".

#### Function to Handle Guessing Logic
```python
def getGuess():
    global word, guessnum
    guess = wordInput.get().lower()
    guessnum += 1
    # Rest of the code...
```
This function handles the guessing logic when the user clicks the "Guess" button.

#### Function to Restart the Game
```python
def restartGame():
    global word, guessnum
    word = words.get_word()
    guessnum = 1
    # Rest of the code...
```
This function restarts the game by getting a new word and resetting the guess count.

#### Creating GUI Elements
```python
wordInput = Entry(root, font=("Helvetica", 16), bg=black, fg=white, insertbackground=white)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3, sticky="we")

wordGuessButton = Button(root, text="Guess", command=getGuess, bg=black, fg=white, font=("Helvetica", 14))
wordGuessButton.grid(row=999, column=3, columnspan=2, padx=5, pady=10, sticky="we")

restartButton = Button(root, text="Restart", command=restartGame, bg=black, fg=white, font=("Helvetica", 14))
restartButton.grid(row=1000, column=0, columnspan=5, padx=5, pady=(0, 10), sticky="we")
```
We create the GUI elements such as the input field, guess button, and restart button, and place them in the tkinter window.

#### Running the Application
```python
root.mainloop()
```
This starts the main event loop of the tkinter application, which listens for events such as button clicks and updates the GUI accordingly.
