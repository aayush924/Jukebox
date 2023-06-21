from tkinter import *

root = Tk()
root.title("JUKEBOX!")


def displayMenu():
    menu = {'1': 'Song 1', '2': 'Song 2', '3': 'Song 3'}
    for i in menu.keys():
        show_label = Label(root, text=menu[i], bg="Red", fg="yellow")
        show_label.pack()


show_button = Button(root, text="Click to see SONG LIST!", command=displayMenu, bg="yellow", fg="brown")
show_button.pack()

root.mainloop()
