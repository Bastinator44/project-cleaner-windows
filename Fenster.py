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


    Button1 = Button(fenster, text="Taskleiste Links", command=lambda: B01(active1))
    Button1.place(x=100, y=120, width=300)
    active1 = Label(fenster, text="O")
    active1.place(x=80, y=120, width=10)

    Button2 = Button(fenster, text="Taskleiste Mitte", command=lambda: B02(active2))
    Button2.place(x=100, y=160, width=300)
    active2 = Label(fenster, text="O")
    active2.place(x=80, y=160, width=10)

    Button3 = Button(fenster, text="Standard Hintergrund festlegen", command=lambda: B03(active3))
    Button3.place(x=100, y=200, width=300)
    active3 = Label(fenster, text="O")
    active3.place(x=80, y=200, width=10)

    Button4 = Button(fenster, text="Suchleistenbildchen deaktivieren", command=lambda: B04(active4))
    Button4.place(x=100, y=240, width=300)
    active4 = Label(fenster, text="O")
    active4.place(x=80, y=240, width=10)

    Button5 = Button(fenster, text="Suchleistenbildchen aktivieren", command=lambda: B05(active5))
    Button5.place(x=100, y=280, width=300)
    active5 = Label(fenster, text="O")
    active5.place(x=80, y=280, width=10)

    Button6 = Button(fenster, text="Widgets deaktivieren", command=lambda: B06(active6))
    Button6.place(x=100, y=320, width=300)
    active6 = Label(fenster, text="O")
    active6.place(x=80, y=320, width=10)

    Button7 = Button(fenster, text="Widgets aktivieren", command=lambda: B07(active7))
    Button7.place(x=100, y=360, width=300)
    active7 = Label(fenster, text="O")
    active7.place(x=80, y=360, width=10)

    Button8 = Button(fenster, text="klassisches Aktionsmenue", command=lambda: B08(active8))
    Button8.place(x=100, y=400, width=300)
    active8 = Label(fenster, text="O")
    active8.place(x=80, y=400, width=10)

    Button9 = Button(fenster, text="modernes Aktionsmenue", command=lambda: B09(active9))
    Button9.place(x=100, y=440, width=300)
    active9 = Label(fenster, text="O")
    active9.place(x=80, y=440, width=10)

# Programm Einstellungen    
    Label2 = Label(fenster, text="Programm Einstellungen")
    Label2.place(x=700, y=80, width=300)

    Button10 = Button(fenster, text="Remove Bing Weather", command=lambda: B10(active10))
    Button10.place(x=540, y=120, width=300)
    active10 = Label(fenster, text="O")
    active10.place(x=520, y=120, width=10)

    Button11 = Button(fenster, text="Remove Microsoft Paint", command=lambda: B11(active11))
    Button11.place(x=540, y=160, width=300)
    active11 = Label(fenster, text="O")
    active11.place(x=520, y=160, width=10)

    Button12 = Button(fenster, text="Remove Microsoft People", command=lambda: B12(active12))
    Button12.place(x=540, y=200, width=300)
    active12 = Label(fenster, text="O")
    active12.place(x=520, y=200, width=10)

    Button13 = Button(fenster, text="Remove Microsoft Solitaire", command=lambda: B13(active13))
    Button13.place(x=540, y=240, width=300)
    active13 = Label(fenster, text="O")
    active13.place(x=520, y=240, width=10)

    Button14 = Button(fenster, text="Remove Microsoft Solitaire Collection", command=lambda: B14(active14))
    Button14.place(x=540, y=280, width=300)
    active14 = Label(fenster, text="O")
    active14.place(x=520, y=280, width=10)

    Button15 = Button(fenster, text="Remove Microsoft Sticky Notes", command=lambda: B15(active15))
    Button15.place(x=540, y=320, width=300)
    active15 = Label(fenster, text="O")
    active15.place(x=520, y=320, width=10)

    Button16 = Button(fenster, text="Remove Screen Sketch", command=lambda: B16(active16))
    Button16.place(x=540, y=360, width=300)
    active16 = Label(fenster, text="O")
    active16.place(x=520, y=360, width=10)

    Button17 = Button(fenster, text="Remove Skype App", command=lambda: B17(active17))
    Button17.place(x=540, y=400, width=300)
    active17 = Label(fenster, text="O")
    active17.place(x=520, y=400, width=10)

    Button18 = Button(fenster, text="Remove Todos", command=lambda: B18(active18))
    Button18.place(x=540, y=440, width=300)
    active18 = Label(fenster, text="O")
    active18.place(x=520, y=440, width=10)

    Button19 = Button(fenster, text="Remove Windows Alarms", command=lambda: B19(active19))
    Button19.place(x=540, y=480, width=300)
    active19 = Label(fenster, text="O")
    active19.place(x=520, y=480, width=10)

    Button20 = Button(fenster, text="Remove Windows Calculator", command=lambda: B20(active20))
    Button20.place(x=540, y=520, width=300)
    active20 = Label(fenster, text="O")
    active20.place(x=520, y=520, width=10)

    Button21 = Button(fenster, text="Remove Windows Camera", command=lambda: B21(active21))
    Button21.place(x=540, y=560, width=300)
    active21 = Label(fenster, text="O")
    active21.place(x=520, y=560, width=10)

    Button22 = Button(fenster, text="Remove Windows Communications Apps", command=lambda: B22(active22))
    Button22.place(x=540, y=600, width=300)
    active22 = Label(fenster, text="O")
    active22.place(x=520, y=600, width=10)

    Button23 = Button(fenster, text="Remove Windows Sound Recorder", command=lambda: B23(active23))
    Button23.place(x=860, y=120, width=300)
    active23 = Label(fenster, text="O")
    active23.place(x=840, y=120, width=10)

    Button24 = Button(fenster, text="Remove Xbox Gaming Overlay", command=lambda: B24(active24))
    Button24.place(x=860, y=160, width=300)
    active24 = Label(fenster, text="O")
    active24.place(x=840, y=160, width=10)

    Button25 = Button(fenster, text="Remove Your Phone", command=lambda: B25(active25))
    Button25.place(x=860, y=200, width=300)
    active25 = Label(fenster, text="O")
    active25.place(x=840, y=200, width=10)

    Button26 = Button(fenster, text="Remove Zune Music", command=lambda: B26(active26))
    Button26.place(x=860, y=240, width=300)
    active26 = Label(fenster, text="O")
    active26.place(x=840, y=240, width=10)

    Button27 = Button(fenster, text="Remove Zune Video", command=lambda: B27(active27))
    Button27.place(x=860, y=280, width=300)
    active27 = Label(fenster, text="O")
    active27.place(x=840, y=280, width=10)

    # Schließen-Button
    button = Button(fenster, text="Schließen", command=fenster.destroy)
    button.place(x=540, y=850, width=300)

    fenster.mainloop()

