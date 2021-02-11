from tkinter import *
import math
from words import WordGenerator


word_generator = WordGenerator()

def countdown(count=60):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer.config(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        update()
        current_word.config(text=f'Final Score: {len(word_generator.correct_words)}')



def update():
    answer.delete(0, END)
    answer.focus()
    word_generator.generate_word()
    current_word.config(text=word_generator.current_word)
    score.config(text=f'Score: {word_generator.score}')

def check_answer(event):
    word = answer.get()
    word_generator.check(word)
    update()

def press_start():
    if word_generator.score > 0:
        word_generator.score = 0
        word_generator.correct_words = []
        countdown()
        update()
    else:
        countdown()
        update()

window = Tk()
window.title("Typing Speed")
window.config(padx=20, pady=20, bg='green')
window.minsize(300, 300)

timer = Label(text="0:00", font=("Comic-Sans", 30, 'bold'), fg='yellow', bg='green', highlightthickness=0)
timer.grid(row=0, column=0)
start_button = Button(text="Start Game", command=press_start, highlightthickness=0)
start_button.grid(row=3, column=1, pady=20)
score = Label(text=f'Score: {word_generator.score}', fg='#6026BF', bg='green', font=('Courier', 20, 'bold'))
score.grid(row=0, column=2)
current_word = Label(text=word_generator.current_word, font=("Arial", 30, 'bold'), bg='green')
current_word.grid(row=1, column=1)
answer = Entry(width=20, highlightthickness=0)
answer.grid(row=2, column=1)

window.bind("<space>", check_answer)
window.bind("<Return>", check_answer)
window.mainloop()