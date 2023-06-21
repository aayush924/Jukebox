from tkinter import *
from playsound import playsound

root = Tk()
root.title("Virtual Jukebox!")


def button_click(s):
    if s == "1":
        playsound('Pop_Smoke_Mood_Swings.mp3')


# Title Label

head = Label(root, text="YOUR JUKEBOX!", bg="red", fg="white", padx=200, pady=20, font=("Arial Black", 30))
head.grid(row=0, column=0, columnspan=4)

# Buttons creation

button1 = Button(root, text='1', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("1")).grid(row=1, column=0)
button2 = Button(root, text='2', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("2")).grid(row=2, column=0)
button3 = Button(root, text='3', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("3")).grid(row=3, column=0)
button4 = Button(root, text='4', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("4")).grid(row=4, column=0)

button5 = Button(root, text='5', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("5")).grid(row=1, column=2)
button6 = Button(root, text='6', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("6")).grid(row=2, column=2)
button7 = Button(root, text='7', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("7")).grid(row=3, column=2)
button8 = Button(root, text='8', bg="red", fg="white", padx=40, pady=20, font=("Arial Black", 20),
                 command=lambda: button_click("8")).grid(row=4, column=2)

# Song List

song1 = Label(root, text='Mood Swings by Pop Smoke', bg="red", fg="white", padx=40, pady=20,
              font=("Arial Black", 20)).grid(row=1, column=1)
song2 = Label(root, text='Song 2', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=2,
                                                                                                          column=1)
song3 = Label(root, text='Song 3', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=3,
                                                                                                          column=1)
song4 = Label(root, text='Song 4', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=4,
                                                                                                          column=1)

song5 = Label(root, text='Song 5', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=1,
                                                                                                          column=3)
song6 = Label(root, text='Song 6', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=2,
                                                                                                          column=3)
song7 = Label(root, text='Song 7', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=3,
                                                                                                          column=3)
song8 = Label(root, text='Song 8', bg="red", fg="white", padx=50, pady=20, font=("Arial Black", 20)).grid(row=4,
                                                                                                          column=3)

root.mainloop()
