from tkinter import *
import pygame
from PIL import ImageTk, Image

root = Tk()
root.title("Virtual Jukebox!")
root.configure(background='#1e1100')

pygame.mixer.init()


# Play Music Function
def button_click(s):
    if s == "1":
        pygame.mixer.music.load('Ed Sheeran  Shape of You.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "2":
        pygame.mixer.music.load('Justin Bieber  Peaches ft Daniel Caesar Giveon.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "3":
        pygame.mixer.music.load('Maroon 5  Girls Like You.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "4":
        pygame.mixer.music.load('The Weeknd  Blinding Lights.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "5":
        pygame.mixer.music.load('Kabira Encore  Yeh Jawaani Hai Deewani.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "6":
        pygame.mixer.music.load('Naagin  Vayu.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "7":
        pygame.mixer.music.load('Daryaa.mp3')
        pygame.mixer.music.play(loops=0)
    elif s == "8":
        pygame.mixer.music.load('Garmi.mp3')
        pygame.mixer.music.play(loops=0)


# Stop Music Function
def stop_func():
    pygame.mixer.music.stop()


global paused
paused = False


# Pause Music Function
def pause_func(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# Background Image

background_img = ImageTk.PhotoImage(Image.open("juke1.png"))
img_label = Label(image=background_img).grid(row=1, column=2, columnspan=2, rowspan=3)

# Title Label

head = Label(root, text="YOUR JUKEBOX!", bg="#d69651", fg="#1e1100", padx=200, pady=20, font=("Harrington", 60, "bold"))
head.grid(row=0, column=0, columnspan=6)

# Buttons creation

button1 = Button(root, text='1', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("1")).grid(row=1, column=0)
button2 = Button(root, text='2', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("2")).grid(row=2, column=0)
button3 = Button(root, text='3', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("3")).grid(row=3, column=0)
button4 = Button(root, text='4', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("4")).grid(row=4, column=0)

button5 = Button(root, text='5', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("5")).grid(row=1, column=4)
button6 = Button(root, text='6', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("6")).grid(row=2, column=4)
button7 = Button(root, text='7', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("7")).grid(row=3, column=4)
button8 = Button(root, text='8', bg="#d69651", fg="#1e1100", padx=20, pady=20, font=("Harrington", 12, "bold"),
                 command=lambda: button_click("8")).grid(row=4, column=4)

# Song List

song1 = Label(root, text='Shape Of You', justify='left', bg="#d69651", fg="#1e1100", padx=62, pady=20,
              font=("Harrington", 12, "bold")).grid(row=1, column=1)
song2 = Label(root, text='Peaches', bg="#d69651", fg="#1e1100", padx=75, pady=20, font=("Harrington", 12, "bold")).grid(
    row=2,
    column=1)
song3 = Label(root, text='Girls Like You', bg="#d69651", fg="#1e1100", padx=62, pady=20,
              font=("Harrington", 12, "bold")).grid(
    row=3, column=1)
song4 = Label(root, text='Blinding Lights', bg="#d69651", fg="#1e1100", padx=62, pady=20,
              font=("Harrington", 12, "bold")).grid(
    row=4, column=1)
song5 = Label(root, text='Kabira', bg="#d69651", fg="#1e1100", padx=75, pady=20, font=("Harrington", 12, "bold")).grid(
    row=1,
    column=5)
song6 = Label(root, text='Naagin', bg="#d69651", fg="#1e1100", padx=75, pady=20, font=("Harrington", 12, "bold")).grid(
    row=2,
    column=5)
song7 = Label(root, text='Daryaa', bg="#d69651", fg="#1e1100", padx=75, pady=20, font=("Harrington", 12, "bold")).grid(
    row=3,
    column=5)
song8 = Label(root, text='Garmi', bg="#d69651", fg="#1e1100", padx=75, pady=20, font=("Harrington", 12, "bold")).grid(
    row=4,
    column=5)

# Music Control Buttons

stop_btn = Button(root, text='[]', bg="#d69651", fg="#1e1100", padx=19, pady=20, font=("Harrington", 12, "bold"),
                  command=stop_func).grid(row=4, column=3)
pause_btn = Button(root, text='||', bg="#d69651", fg="#1e1100", padx=19, pady=20, font=("Harrington", 12, "bold"),
                   command=lambda: pause_func(paused)).grid(row=4, column=2)

root.mainloop()
