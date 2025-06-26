from tkinter import *

def Fenster():
    fenster = Tk()
    fenster.title("Project-cleaner-Windows")
    fenster.geometry("400x300")
    
    label = Label(fenster, text="Project-cleaner-Windows\nwähle alle gewünschten Einstellungen aus!")
    label.pack(pady=20)
    
    button = Button(fenster, text="Schließen", command=fenster.destroy)
    button.pack(pady=10)
    
    fenster.mainloop()