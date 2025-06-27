from tkinter import *
from actions import *



def Fenster():
    fenster = Tk()
    fenster.title("Project-cleaner-Windows")
    fenster.geometry("1280x720")

    label = Label(fenster, text="Project-cleaner-Windows\nwaehle alle gewuenschten Einstellungen aus!")
    label.place(x=400, y=20)

# Allgemeine Einstellungen
    Label1 = Label(fenster, text="Allgemeine Einstellungen")
    Label1.place(x=100, y=80, width=300)


    Button1 = Button(fenster, text="Taskleiste Links", command=lambda: print("Taskleiste Links ausgewaehlt"))
    Button1.place(x=100, y=120, width=300)

    Button2 = Button(fenster, text="Taskleiste Mitte", command=lambda: print("Taskleiste Mitte ausgewaehlt"))
    Button2.place(x=100, y=160, width=300)

    Button3 = Button(fenster, text="Standard Hintergrund festlegen", command=lambda: print("Standard Hintergrund festgelegt"))
    Button3.place(x=100, y=200, width=300)

    Button4 = Button(fenster, text="Suchleistenbildchen deaktivieren", command=lambda: print("Suchleistenbildchen deaktiviert"))
    Button4.place(x=100, y=240, width=300)

    Button5 = Button(fenster, text="Suchleistenbildchen aktivieren", command=lambda: print("Suchleistenbildchen aktiviert"))
    Button5.place(x=100, y=280, width=300)

    Button6 = Button(fenster, text="Widgets deaktivieren", command=lambda: print("Widgets deaktiviert"))
    Button6.place(x=100, y=320, width=300)

    Button7 = Button(fenster, text="Widgets aktivieren", command=lambda: print("Widgets aktiviert"))
    Button7.place(x=100, y=360, width=300)

    Button8 = Button(fenster, text="klassisches Aktionsmenue", command=lambda: print("Klassisches Aktionsmenue ausgewaehlt"))
    Button8.place(x=100, y=400, width=300)

    Button9 = Button(fenster, text="modernes Aktionsmenue", command=lambda: print("Modernes Aktionsmenue ausgewaehlt"))
    Button9.place(x=100, y=440, width=300)

# Programm Einstellungen    
    Label2 = Label(fenster, text="Programm Einstellungen")
    Label2.place(x=700, y=80, width=300)

    Button10 = Button(fenster, text="Remove Bing Weather", command=lambda: print("Remove Bing Weather ausgewaehlt"))
    Button10.place(x=540, y=120, width=300)

    Button11 = Button(fenster, text="Remove Microsoft Paint", command=lambda: print("Remove Microsoft Paint ausgewaehlt"))
    Button11.place(x=540, y=160, width=300)

    Button12 = Button(fenster, text="Remove Microsoft People", command=lambda: print("Remove Microsoft People ausgewaehlt"))
    Button12.place(x=540, y=200, width=300)

    Button13 = Button(fenster, text="Remove Microsoft Solitaire", command=lambda: print("Remove Microsoft Solitaire ausgewaehlt"))
    Button13.place(x=540, y=240, width=300)

    Button14 = Button(fenster, text="Remove Microsoft Solitaire Collection", command=lambda: print("Remove Microsoft Solitaire Collection ausgewaehlt"))
    Button14.place(x=540, y=280, width=300)

    Button15 = Button(fenster, text="Remove Microsoft Sticky Notes", command=lambda: print("Remove Microsoft Sticky Notes ausgewaehlt"))
    Button15.place(x=540, y=320, width=300)

    Button16 = Button(fenster, text="Remove Screen Sketch", command=lambda: print("Remove Screen Sketch ausgewaehlt"))
    Button16.place(x=540, y=360, width=300)

    Button17 = Button(fenster, text="Remove Skype App", command=lambda: print("Remove Skype App ausgewaehlt"))
    Button17.place(x=540, y=400, width=300)

    Button18 = Button(fenster, text="Remove Todos", command=lambda: print("Remove Todos ausgewaehlt"))
    Button18.place(x=540, y=440, width=300)

    Button19 = Button(fenster, text="Remove Windows Alarms", command=lambda: print("Remove Windows Alarms ausgewaehlt"))
    Button19.place(x=540, y=480, width=300)

    Button20 = Button(fenster, text="Remove Windows Calculator", command=lambda: print("Remove Windows Calculator ausgewaehlt"))
    Button20.place(x=540, y=520, width=300)

    Button21 = Button(fenster, text="Remove Windows Camera", command=lambda: print("Remove Windows Camera ausgewaehlt"))
    Button21.place(x=540, y=560, width=300)

    Button22 = Button(fenster, text="Remove Windows Communications Apps", command=lambda: print("Remove Windows Communications Apps ausgewaehlt"))
    Button22.place(x=540, y=600, width=300)

    Button23 = Button(fenster, text="Remove Windows Sound Recorder", command=lambda: print("Remove Windows Sound Recorder ausgewaehlt"))
    Button23.place(x=860, y=120, width=300)

    Button24 = Button(fenster, text="Remove Xbox Gaming Overlay", command=lambda: (print("Remove Xbox Gaming Overlay ausgewaehlt"), B24()))
    Button24.place(x=860, y=160, width=300)

    Button25 = Button(fenster, text="Remove Your Phone", command=lambda: (print("Remove Your Phone ausgewaehlt"), B25()))
    Button25.place(x=860, y=200, width=300)

    Button26 = Button(fenster, text="Remove Zune Music", command=lambda: (print("Remove Zune Music ausgewaehlt"), B26()))
    Button26.place(x=860, y=240, width=300)

    Button27 = Button(fenster, text="Remove Zune Video", command=lambda: (print("Remove Zune Video ausgewaehlt"), B27()))
    Button27.place(x=860, y=280, width=300)

    # Schließen-Button
    button = Button(fenster, text="Schließen", command=fenster.destroy)
    button.place(x=540, y=850, width=300)

    fenster.mainloop()