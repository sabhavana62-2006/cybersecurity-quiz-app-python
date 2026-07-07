import tkinter as tk
import random
from tkinter import messagebox
from questions import questions

random.shuffle(questions)

score = 0
current_question = 0

window = tk.Tk()
window.title("Cybersecurity Quiz Application")
window.geometry("700x500")

question_label = tk.Label(window, text="", font=("Arial", 18, "bold"), wraplength=600)
question_label.pack(pady=20)

selected = tk.StringVar()

radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=selected, value="", font=("Arial", 13))
    rb.pack(anchor="w")
    radio_buttons.append(rb)


def load_question():
    global current_question

    q = questions[current_question]

    question_label.config(
        text=f"Question {current_question + 1} of {len(questions)}\n\n{q['question']}"
    )

    selected.set("")

    for i in range(4):
        radio_buttons[i].config(
            text=q["options"][i],
            value=q["options"][i]
        )


def next_question():
    global current_question, score

    if selected.get() == "":
        messagebox.showwarning("Warning", "Please select an answer.")
        return

    if selected.get() == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        percentage = (score / len(questions)) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "Fail"

        messagebox.showinfo(
            "Quiz Completed",
            f"🎉 Quiz Completed!\n\n"
            f"Score : {score}/{len(questions)}\n"
            f"Percentage : {percentage:.0f}%\n"
            f"Grade : {grade}"
        )

        window.destroy()


next_button = tk.Button(
    window,
    text="Next",
    command=next_question,
    bg="blue",
    fg="white",
    font=("Arial", 14, "bold")
)

next_button.pack(pady=20)

load_question()

window.mainloop()