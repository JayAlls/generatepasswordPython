import string
from random import *
from tkinter import *

# Fonction


def generate_password():
    min_letter = 6
    max_letter = 24
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(min_letter, max_letter)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    with open("password_list.txt", "a+") as file:
        file.write(password + "\n")
        file.close()


# WINDOW

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x540")
window.minsize(720, 540)
window.config(background="#6b705c")

# FRAME

middle_frame = Frame(window, bg="#6b705c")

# Title

title = Label(window, text="Générateur de MDP", bg="#6b705c", font=("Courrier", 40), fg="white")
title.pack()

# Password Entry

password_entry = Entry(middle_frame, bg="#6b705c", fg="white", font=("Helvetica", 25))
password_entry.pack()


# Bouton

btn_generate = Button(middle_frame, text="Générer", font=("Helvetica", 20), bg="#fff", fg="#6b705c", command=generate_password)

btn_generate.pack(pady=20)
middle_frame.pack(expand=YES)
window.mainloop()
