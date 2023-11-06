import tkinter as tk
import tkinter.simpledialog


def create_word_row(word, answer, correct):
    word = word.upper()
    answer = answer.upper()
    canvas = tk.Canvas(window, width=len(answer)*100, height=100)

    x = 0
    memory = set()
    while x < len(answer):
        canvas.create_rectangle(x*100, 0, x*100+100, 100, fill="#3991d1")
        if (x >= len(word) and answer[x] == " ") or (x < len(word) and word[x] == " "):
            canvas.create_rectangle(x*100, 0, x*100+100, 100, fill="grey")
        elif (x < len(word) and answer[x] == word[x]) or (x >= len(word) and x in correct):
            canvas.create_rectangle(x*100, 0, x*100+100, 100, fill="#e41c40")
            correct.add(x)
        elif x < len(word):
            for y in range(len(answer)):
                if word[x] == answer[y] and (y >= len(word) or word[y] != answer[y]) and y not in memory:
                    canvas.create_oval(x*100, 0, x*100+100, 100, fill="#cdc24e")
                    memory.add(y)
        if x < len(word):
            canvas.create_text(x*100+50, 50, text=word[x], fill="white", font=("Helvetica", 24))
        elif x in correct:
            canvas.create_text(x*100+50, 50, text=answer[x], fill="white", font=("Helvetica", 24))
        x += 1

    return canvas, correct


answer = tkinter.simpledialog.askstring("Kies het antwoord", "Kies het antwoord:")

window = tk.Tk()
window.title("2 Woorden, 9 Letters Lingo")

row, correct = create_word_row("", answer, {0})
row.pack()

while True:
    guess = tkinter.simpledialog.askstring("Doe een poging", "Doe een poging: ")
    row.forget()
    row, correct = create_word_row(guess, answer, correct)
    row.pack()
    if len(correct) == len(answer) - answer.count(" "):
        break
    row, correct = create_word_row("", answer, correct)
    row.pack()

window.mainloop()

