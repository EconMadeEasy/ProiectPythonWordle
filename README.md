Scriptul words.py

#### Importarea Bibliotecilor
```python
import random
```
Aici importăm modulul random pentru a genera numere aleatoare pentru selectarea unui cuvânt din lista.

#### Listă de Cuvinte
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
# ... Mai multe cuvinte ...
your
yourself"""
```
Un șir lung conținând o listă de cuvinte, fiecare separate prin un caracter de linie nouă.

#### Divizarea Cuvintelor
```python
wordsList = words.split('\n')
```
Divizăm șirul lung într-o listă de cuvinte folosind caracterul de linie nouă ca separator.

#### Filtrarea Cuvintelor
```python
outputWordsList = []

for i in range(len(wordsList) - 1):
    selected = wordsList[i]
    
    if "".join(dict.fromkeys(selected)) == selected and len(selected) == 5:
        # Verificăm dacă există litere repetate și dacă lungimea cuvântului este de 5 caractere
        
        outputWordsList.append(selected)
```
Iterăm prin fiecare cuvânt din listă, verificând dacă are litere repetate și dacă lungimea sa este de 5 caractere. În caz afirmativ, îl adăugăm la outputWordsList.

#### Funcția pentru Obținerea unui Cuvânt
```python
def get_word():
    return random.choice(outputWordsList)
```
Această funcție returnează un cuvânt aleatoriu din lista filtrată de cuvinte.

Scriptul main.py

#### Importarea Bibliotecilor
```python
from tkinter import messagebox
from tkinter import *
import words
```
Importăm modulele necesare din biblioteca tkinter pentru crearea interfeței grafice, iar modulele words pentru a obține un cuvânt aleatoriu pentru joc.

#### Inițializarea Variabilelor Jocului
```python
word = words.get_word()
guessnum = 1
```
Inițializăm variabila word prin obținerea unui cuvânt aleatoriu folosind funcția get_word() din modulul words. guessnum ține evidența numărului de încercări.

#### Crearea Ferestrei GUI
```python
root = Tk()
root.config(bg=black)
root.title("Wordle")
```
Creăm fereastra principală tkinter cu un fundal negru și îi setăm titlul la "Wordle".

#### Funcția pentru Gestionarea Logicii de Ghicire
```python
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
            if word.lower() == guess.lower(): # Correct guess
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
        messagebox.showerror("Game Over", f"Game over! The word was {word.title()}").
```
Această funcție gestionează logica de ghicire atunci când utilizatorul apasă butonul "Guess".

#### Funcția pentru Restartarea Jocului
```python
def restartGame():
    global word, guessnum
    word = words.get_word()
    guessnum = 0
    # Clear any existing labels
    for widget in root.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()
    # Clear the input field
    wordInput.delete(0, END)
    # Focus on the input field
    wordInput.focus()

```
Această funcție reia jocul obținând un nou cuvânt și resetând numărul de încercări.

#### Crearea Elementelor GUI
```python
wordInput = Entry(root, font=("Helvetica", 16), bg=black, fg=white, insertbackground=white)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3, sticky="we")

wordGuessButton = Button(root, text="Guess", command=getGuess, bg=black, fg=white, font=("Helvetica", 14))
wordGuessButton.grid(row=999, column=3, columnspan=2, padx=5, pady=10, sticky="we")

restartButton = Button(root, text="Restart", command=restartGame, bg=black, fg=white, font=("Helvetica", 14))
restartButton.grid(row=1000, column=0, columnspan=5, padx=5, pady=(0, 10), sticky="we")
```
Creăm elementele GUI, cum ar fi câmpul de introducere, butonul de ghicit și butonul de repornire, și le plasăm în fereastra tkinter.

#### Rularea Aplicației
```python
root.mainloop()
```
Aceasta pornește bucla principală de evenimente a aplicației tkinter, care ascultă evenimente precum clicurile pe butoane și actualizează interfața grafică în consecință.
