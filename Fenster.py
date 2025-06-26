from tkinter import *


def Fenster():
    fenster = Tk()
    fenster.title("Project-cleaner-Windows")
    fenster.geometry("1280x720")

    label = Label(fenster, text="Project-cleaner-Windows\nwaehle alle gewuenschten Einstellungen aus!")
    label.place(x=400, y=20)

    # Allgemeine Einstellungen (links)
    Label1 = Label(fenster, text="Allgemeine Einstellungen")
    Label1.place(x=100, y=80)

    # Variablen für Checkboxen (Allgemeine Einstellungen)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    # Importiere die Funktionen aus einer anderen Datei (z.B. actions.py)
    from actions import (
        taskleiste_links,
        taskleiste_mitte,
        standard_hintergrund_festlegen,
        suchleistenbildchen_deaktivieren,
        suchleistenbildchen_aktivieren,
        widgets_deaktivieren,
        widgets_aktivieren,
        klassisches_aktionsmenue,
        modernes_aktionsmenue,
        remove_bing_weather,
        remove_microsoft_paint,
        remove_microsoft_people,
        remove_microsoft_solitaire,
        remove_microsoft_solitaire_collection,
        remove_microsoft_sticky_notes,
        remove_screen_sketch,
        remove_skype_app,
        remove_todos,
        remove_windows_alarms,
        remove_windows_calculator,
        remove_windows_camera,
        remove_windows_communications_apps,
        remove_windows_sound_recorder,
        remove_xbox_gaming_overlay,
        remove_your_phone,
        remove_zune_music,
        remove_zune_video
    )

    # Callback-Funktionen für Checkboxen
    def on_var1():
        if var1.get():
            taskleiste_links()
    def on_var2():
        if var2.get():
            taskleiste_mitte()
    def on_var3():
        if var3.get():
            standard_hintergrund_festlegen()
    def on_var4():
        if var4.get():
            suchleistenbildchen_deaktivieren()
    def on_var5():
        if var5.get():
            suchleistenbildchen_aktivieren()
    def on_var6():
        if var6.get():
            widgets_deaktivieren()
    def on_var7():
        if var7.get():
            widgets_aktivieren()
    def on_var8():
        if var8.get():
            klassisches_aktionsmenue()
    def on_var9():
        if var9.get():
            modernes_aktionsmenue()
    def on_var10():
        if var10.get():
            remove_bing_weather()
    def on_var11():
        if var11.get():
            remove_microsoft_paint()
    def on_var12():
        if var12.get():
            remove_microsoft_people()
    def on_var13():
        if var13.get():
            remove_microsoft_solitaire()
    def on_var14():
        if var14.get():
            remove_microsoft_solitaire_collection()
    def on_var15():
        if var15.get():
            remove_microsoft_sticky_notes()
    def on_var16():
        if var16.get():
            remove_screen_sketch()
    def on_var17():
        if var17.get():
            remove_skype_app()
    def on_var18():
        if var18.get():
            remove_todos()
    def on_var19():
        if var19.get():
            remove_windows_alarms()
    def on_var20():
        if var20.get():
            remove_windows_calculator()
    def on_var21():
        if var21.get():
            remove_windows_camera()
    def on_var22():
        if var22.get():
            remove_windows_communications_apps()
    def on_var23():
        if var23.get():
            remove_windows_sound_recorder()
    def on_var24():
        if var24.get():
            remove_xbox_gaming_overlay()
    def on_var25():
        if var25.get():
            remove_your_phone()
    def on_var26():
        if var26.get():
            remove_zune_music()
    def on_var27():
        if var27.get():
            remove_zune_video()

    # Trace-Methoden für Checkboxen setzen
    var1.trace_add("write", lambda *args: on_var1())
    var2.trace_add("write", lambda *args: on_var2())
    var3.trace_add("write", lambda *args: on_var3())
    var4.trace_add("write", lambda *args: on_var4())
    var5.trace_add("write", lambda *args: on_var5())
    var6.trace_add("write", lambda *args: on_var6())
    var7.trace_add("write", lambda *args: on_var7())
    var8.trace_add("write", lambda *args: on_var8())
    var9.trace_add("write", lambda *args: on_var9())
    var10.trace_add("write", lambda *args: on_var10())
    var11.trace_add("write", lambda *args: on_var11())
    var12.trace_add("write", lambda *args: on_var12())
    var13.trace_add("write", lambda *args: on_var13())
    var14.trace_add("write", lambda *args: on_var14())
    var15.trace_add("write", lambda *args: on_var15())
    var16.trace_add("write", lambda *args: on_var16())
    var17.trace_add("write", lambda *args: on_var17())
    var18.trace_add("write", lambda *args: on_var18())
    var19.trace_add("write", lambda *args: on_var19())
    var20.trace_add("write", lambda *args: on_var20())
    var21.trace_add("write", lambda *args: on_var21())
    var22.trace_add("write", lambda *args: on_var22())
    var23.trace_add("write", lambda *args: on_var23())
    var24.trace_add("write", lambda *args: on_var24())
    var25.trace_add("write", lambda *args: on_var25())
    var26.trace_add("write", lambda *args: on_var26())
    var27.trace_add("write", lambda *args: on_var27())
    # Allgemeine Einstellungen Buttons und Checkboxen
    Checkbutton(fenster, variable=var1, onvalue=1, offvalue=0).place(x=260, y=120)
    Button1 = Button(fenster, text="Taskleiste Links", command=lambda: print("Taskleiste Links ausgewaehlt"))
    Button1.place(x=300, y=120)

    Checkbutton(fenster, variable=var2, onvalue=1, offvalue=0).place(x=260, y=160)
    Button2 = Button(fenster, text="Taskleiste Mitte", command=lambda: print("Taskleiste Mitte ausgewaehlt"))
    Button2.place(x=300, y=160)

    Checkbutton(fenster, variable=var3, onvalue=1, offvalue=0).place(x=260, y=200)
    Button3 = Button(fenster, text="Standard Hintergrund festlegen", command=lambda: print("Standard Hintergrund festgelegt"))
    Button3.place(x=300, y=200)

    Checkbutton(fenster, variable=var4, onvalue=1, offvalue=0).place(x=260, y=240)
    Button4 = Button(fenster, text="Suchleistenbildchen deaktivieren", command=lambda: print("Suchleistenbildchen deaktiviert"))
    Button4.place(x=300, y=240)

    Checkbutton(fenster, variable=var5, onvalue=1, offvalue=0).place(x=260, y=280)
    Button5 = Button(fenster, text="Suchleistenbildchen aktivieren", command=lambda: print("Suchleistenbildchen aktiviert"))
    Button5.place(x=300, y=280)

    Checkbutton(fenster, variable=var6, onvalue=1, offvalue=0).place(x=260, y=320)
    Button6 = Button(fenster, text="Widgets deaktivieren", command=lambda: print("Widgets deaktiviert"))
    Button6.place(x=300, y=320)

    Checkbutton(fenster, variable=var7, onvalue=1, offvalue=0).place(x=260, y=360)
    Button7 = Button(fenster, text="Widgets aktivieren", command=lambda: print("Widgets aktiviert"))
    Button7.place(x=300, y=360)

    Checkbutton(fenster, variable=var8, onvalue=1, offvalue=0).place(x=260, y=400)
    Button8 = Button(fenster, text="klassisches Aktionsmenue", command=lambda: print("Klassisches Aktionsmenue ausgewaehlt"))
    Button8.place(x=300, y=400)

    Checkbutton(fenster, variable=var9, onvalue=1, offvalue=0).place(x=260, y=440)
    Button9 = Button(fenster, text="modernes Aktionsmenue", command=lambda: print("Modernes Aktionsmenue ausgewaehlt"))
    Button9.place(x=300, y=440)

    # Programm Einstellungen (rechts)
    Label2 = Label(fenster, text="Programm Einstellungen")
    Label2.place(x=700, y=80)

    # Variablen für Checkboxen (Programm Einstellungen)
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    var19 = IntVar()
    var20 = IntVar()
    var21 = IntVar()
    var22 = IntVar()
    var23 = IntVar()
    var24 = IntVar()
    var25 = IntVar()
    var26 = IntVar()
    var27 = IntVar()

    # Programm Einstellungen Buttons und Checkboxen
    Checkbutton(fenster, variable=var10, onvalue=1, offvalue=0).place(x=860, y=120)
    Button10 = Button(fenster, text="Remove Bing Weather", command=lambda: print("Remove Bing Weather ausgewaehlt"))
    Button10.place(x=900, y=120)

    Checkbutton(fenster, variable=var11, onvalue=1, offvalue=0).place(x=860, y=160)
    Button11 = Button(fenster, text="Remove Microsoft Paint", command=lambda: print("Remove Microsoft Paint ausgewaehlt"))
    Button11.place(x=900, y=160)

    Checkbutton(fenster, variable=var12, onvalue=1, offvalue=0).place(x=860, y=200)
    Button12 = Button(fenster, text="Remove Microsoft People", command=lambda: print("Remove Microsoft People ausgewaehlt"))
    Button12.place(x=900, y=200)

    Checkbutton(fenster, variable=var13, onvalue=1, offvalue=0).place(x=860, y=240)
    Button13 = Button(fenster, text="Remove Microsoft Solitaire", command=lambda: print("Remove Microsoft Solitaire ausgewaehlt"))
    Button13.place(x=900, y=240)

    Checkbutton(fenster, variable=var14, onvalue=1, offvalue=0).place(x=860, y=280)
    Button14 = Button(fenster, text="Remove Microsoft Solitaire Collection", command=lambda: print("Remove Microsoft Solitaire Collection ausgewaehlt"))
    Button14.place(x=900, y=280)

    Checkbutton(fenster, variable=var15, onvalue=1, offvalue=0).place(x=860, y=320)
    Button15 = Button(fenster, text="Remove Microsoft Sticky Notes", command=lambda: print("Remove Microsoft Sticky Notes ausgewaehlt"))
    Button15.place(x=900, y=320)

    Checkbutton(fenster, variable=var16, onvalue=1, offvalue=0).place(x=860, y=360)
    Button16 = Button(fenster, text="Remove Screen Sketch", command=lambda: print("Remove Screen Sketch ausgewaehlt"))
    Button16.place(x=900, y=360)

    Checkbutton(fenster, variable=var17, onvalue=1, offvalue=0).place(x=860, y=400)
    Button17 = Button(fenster, text="Remove Skype App", command=lambda: print("Remove Skype App ausgewaehlt"))
    Button17.place(x=900, y=400)

    Checkbutton(fenster, variable=var18, onvalue=1, offvalue=0).place(x=860, y=440)
    Button18 = Button(fenster, text="Remove Todos", command=lambda: print("Remove Todos ausgewaehlt"))
    Button18.place(x=900, y=440)

    Checkbutton(fenster, variable=var19, onvalue=1, offvalue=0).place(x=860, y=480)
    Button19 = Button(fenster, text="Remove Windows Alarms", command=lambda: print("Remove Windows Alarms ausgewaehlt"))
    Button19.place(x=900, y=480)

    Checkbutton(fenster, variable=var20, onvalue=1, offvalue=0).place(x=860, y=520)
    Button20 = Button(fenster, text="Remove Windows Calculator", command=lambda: print("Remove Windows Calculator ausgewaehlt"))
    Button20.place(x=900, y=520)

    Checkbutton(fenster, variable=var21, onvalue=1, offvalue=0).place(x=860, y=560)
    Button21 = Button(fenster, text="Remove Windows Camera", command=lambda: print("Remove Windows Camera ausgewaehlt"))
    Button21.place(x=900, y=560)

    Checkbutton(fenster, variable=var22, onvalue=1, offvalue=0).place(x=860, y=600)
    Button22 = Button(fenster, text="Remove Windows Communications Apps", command=lambda: print("Remove Windows Communications Apps ausgewaehlt"))
    Button22.place(x=900, y=600)

    Checkbutton(fenster, variable=var23, onvalue=1, offvalue=0).place(x=860, y=640)
    Button23 = Button(fenster, text="Remove Windows Sound Recorder", command=lambda: print("Remove Windows Sound Recorder ausgewaehlt"))
    Button23.place(x=900, y=640)

    Checkbutton(fenster, variable=var24, onvalue=1, offvalue=0).place(x=860, y=680)
    Button24 = Button(fenster, text="Remove Xbox Gaming Overlay", command=lambda: print("Remove Xbox Gaming Overlay ausgewaehlt"))
    Button24.place(x=900, y=680)

    Checkbutton(fenster, variable=var25, onvalue=1, offvalue=0).place(x=860, y=720)
    Button25 = Button(fenster, text="Remove Your Phone", command=lambda: print("Remove Your Phone ausgewaehlt"))
    Button25.place(x=900, y=720)

    Checkbutton(fenster, variable=var26, onvalue=1, offvalue=0).place(x=860, y=760)
    Button26 = Button(fenster, text="Remove Zune Music", command=lambda: print("Remove Zune Music ausgewaehlt"))
    Button26.place(x=900, y=760)

    Checkbutton(fenster, variable=var27, onvalue=1, offvalue=0).place(x=860, y=800)
    Button27 = Button(fenster, text="Remove Zune Video", command=lambda: print("Remove Zune Video ausgewaehlt"))
    Button27.place(x=900, y=800)

    # Schließen-Button
    button = Button(fenster, text="Schließen", command=fenster.destroy)
    button.place(x=540, y=850)

    fenster.mainloop()