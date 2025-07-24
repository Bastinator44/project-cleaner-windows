from tkinter import * # type: ignore
from actions import *
from standard_werte import farbe_hg_b


def Fenster():
    fenster = Tk()
    fenster.title("Project-cleaner-Windows")
    fenster.geometry("1280x720")

    label = Label(fenster, text="Project-cleaner-Windows\nwaehle alle gewuenschten Einstellungen aus!")
    label.place(x=400, y=20)

# Allgemeine Einstellungen
    Label1 = Label(fenster, text="Allgemeine Einstellungen")
    Label1.place(x=100, y=80, width=300)


    Button1 = Button(fenster, text="Taskleiste Links", **farbe_hg_b, command=lambda: B01(active1)) # type: ignore
    Button1.place(x=100, y=120, width=300)
    active1 = Label(fenster, text="O")
    active1.place(x=80, y=120, width=10)

    Button2 = Button(fenster, text="Taskleiste Mitte", **farbe_hg_b, command=lambda: B02(active2)) # type: ignore
    Button2.place(x=100, y=160, width=300)
    active2 = Label(fenster, text="O")
    active2.place(x=80, y=160, width=10)

    Button3 = Button(fenster, text="Standard Hintergrund festlegen", **farbe_hg_b, command=lambda: B03(active3)) # type: ignore
    Button3.place(x=100, y=200, width=300)
    active3 = Label(fenster, text="O")
    active3.place(x=80, y=200, width=10)

    Button4 = Button(fenster, text="Suchleistenbildchen deaktivieren", **farbe_hg_b, command=lambda: B04(active4)) # type: ignore
    Button4.place(x=100, y=240, width=300)
    active4 = Label(fenster, text="O")
    active4.place(x=80, y=240, width=10)

    Button5 = Button(fenster, text="Suchleistenbildchen aktivieren", **farbe_hg_b, command=lambda: B05(active5)) # type: ignore
    Button5.place(x=100, y=280, width=300)
    active5 = Label(fenster, text="O")
    active5.place(x=80, y=280, width=10)

    Button6 = Button(fenster, text="Widgets deaktivieren", **farbe_hg_b, command=lambda: B06(active6)) # type: ignore
    Button6.place(x=100, y=320, width=300)
    active6 = Label(fenster, text="O")
    active6.place(x=80, y=320, width=10)

    Button7 = Button(fenster, text="Widgets aktivieren", **farbe_hg_b, command=lambda: B07(active7)) # type: ignore
    Button7.place(x=100, y=360, width=300)
    active7 = Label(fenster, text="O")
    active7.place(x=80, y=360, width=10)

    Button8 = Button(fenster, text="klassisches Aktionsmenue", **farbe_hg_b, command=lambda: B08(active8)) # type: ignore
    Button8.place(x=100, y=400, width=300)
    active8 = Label(fenster, text="O")
    active8.place(x=80, y=400, width=10)

    Button9 = Button(fenster, text="modernes Aktionsmenue", **farbe_hg_b, command=lambda: B09(active9)) # type: ignore
    Button9.place(x=100, y=440, width=300)
    active9 = Label(fenster, text="O")
    active9.place(x=80, y=440, width=10)

# Programm Einstellungen    
    Label2 = Label(fenster, text="Programm Einstellungen (noch nicht benutzen!)")
    Label2.place(x=700, y=80, width=300)

    Button10 = Button(fenster, text="Remove Apps from provisioned package", **farbe_hg_b, command=lambda: B10(active10)) # type: ignore
    Button10.place(x=540, y=120, width=300)
    active10 = Label(fenster, text="O")
    active10.place(x=520, y=120, width=10)

    Button11 = Button(fenster, text="Remove Apps from installed package", **farbe_hg_b, command=lambda: B11(active11)) # type: ignore


    close = Button(fenster, text="Schließen", command=fenster.destroy)
    close.place(x=95, y=660, width=300)

    pruefung = Button(fenster, text="Einstellungen pruefen", command=lambda: proof(active1, active2, active4, active5, active6, active7, active8, active9,))
    pruefung.place(x=490, y=660, width=300)

    sichern = Button(fenster, text="In Datei speichern", command=lambda: save(file_var))
    sichern.place(x=885, y=660, width=300)

    fenster.mainloop()