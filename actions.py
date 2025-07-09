import os
from tkinter import filedialog

global file_var
file_var = []
dictionary_files = {
        "A1": "Allgemeine Einstellungen/1_Taskleiste_links.bat",
        "A2": "Allgemeine Einstellungen/2_Taskleiste_zentriert.bat",
        "A3": "Allgemeine Einstellungen/3_Standard_Hintergrundfestlegen.bat",
        "A4": "Allgemeine Einstellungen/4_Suchleistenbildchen_deaktivieren.bat",
        "A5": "Allgemeine Einstellungen/5_Suchleistenbildchen_aktivieren.bat",
        "A6": "Allgemeine Einstellungen/6_Widgets_deaktivieren.bat",
        "A7": "Allgemeine Einstellungen/7_Widgets_aktivieren.bat",
        "A8": "Allgemeine Einstellungen/8_klassisches_Aktionsmenue.bat",
        "A9": "Allgemeine Einstellungen/9_modernes_Aktionsmenue.bat",
        "P1": "Programm Einstellungen/Remove_BingWeather.bat",
        "P2": "Programm Einstellungen/Remove_MSPaint.bat",
        "P3": "Programm Einstellungen/Remove_People.bat",
        "P4": "Programm Einstellungen/Remove_ScreenSketch.bat",
        "P5": "Programm Einstellungen/Remove_SkypeApp.bat",
        "P6": "Programm Einstellungen/Remove_Todos.bat",
        "P7": "Programm Einstellungen/Remove_WindowsAlarms.bat",
        "P8": "Programm Einstellungen/Remove_WindowsCalculator.bat",
        "P9": "Programm Einstellungen/Remove_WindowsCamera.bat",
        "P10": "Programm Einstellungen/Remove_WindowsCommunicationsApps.bat",
        "P11": "Programm Einstellungen/Remove_WindowsSoundRecorder.bat",
        "P12": "Programm Einstellungen/Remove_XboxGamingOverlay.bat",
        "P13": "Programm Einstellungen/Remove_YourPhone.bat",
        "P14": "Programm Einstellungen/Remove_ZuneMusic.bat",
        "P15": "Programm Einstellungen/Remove_ZuneVideo.bat",
        "P16": "Programm Einstellungen/Remove_MicrosoftSolitaire.bat",
        "P17": "Programm Einstellungen/Remove_MicrosoftSolitaireCollection.bat",
        "P18": "Programm Einstellungen/Remove_MicrosoftStickyNotes.bat"
    }

def B01(active1):
    active_content = active1.cget("text")
    if active_content == "O":
        active1.config(text="X")
        file_var.append("A1")
    if active_content == "X":
        file_var.remove("A1")
        active1.config(text="O")

def B02(active2):
    active_content = active2.cget("text")
    if active_content == "O":
        active2.config(text="X")
        file_var.append("A2")
    if active_content == "X":
        file_var.remove("A2")
        active2.config(text="O")

def B03(active3):
    active_content = active3.cget("text")
    if active_content == "O":
        active3.config(text="X")
        file_var.append("A3")
    if active_content == "X":
        file_var.remove("A3")
        active3.config(text="O")

def B04(active4):
    active_content = active4.cget("text")
    if active_content == "O":
        active4.config(text="X")
        file_var.append("A4")
    if active_content == "X":
        file_var.remove("A4")
        active4.config(text="O")

def B05(active5):
    active_content = active5.cget("text")
    if active_content == "O":
        active5.config(text="X")
        file_var.append("A5")
    if active_content == "X":
        file_var.remove("A5")
        active5.config(text="O")

def B06(active6):
    active_content = active6.cget("text")
    if active_content == "O":
        active6.config(text="X")
        file_var.append("A6")
    if active_content == "X":
        file_var.remove("A6")
        active6.config(text="O")

def B07(active7):
    active_content = active7.cget("text")
    if active_content == "O":
        active7.config(text="X")
        file_var.append("A7")
    if active_content == "X":
        file_var.remove("A7")
        active7.config(text="O")

def B08(active8):
    active_content = active8.cget("text")
    if active_content == "O":
        active8.config(text="X")
        file_var.append("A8")
    if active_content == "X":
        file_var.remove("A8")
        active8.config(text="O")

def B09(active9):
    active_content = active9.cget("text")
    if active_content == "O":
        active9.config(text="X")
        file_var.append("A9")
    if active_content == "X":
        file_var.remove("A9")
        active9.config(text="O")

def B10(active10):
    active_content = active10.cget("text")
    if active_content == "O":
        active10.config(text="X")
        file_var.append("P1")
    if active_content == "X":
        file_var.remove("P1")
        active10.config(text="O")

def B11(active11):
    active_content = active11.cget("text")
    if active_content == "O":
        active11.config(text="X")
        file_var.append("P2")
    if active_content == "X":
        file_var.remove("P2")
        active11.config(text="O")

def B12(active12):
    active_content = active12.cget("text")
    if active_content == "O":
        active12.config(text="X")
        file_var.append("P3")
    if active_content == "X":
        file_var.remove("P3")
        active12.config(text="O")

def B13(active13):
    active_content = active13.cget("text")
    if active_content == "O":
        active13.config(text="X")
        file_var.append("P4")
    if active_content == "X":
        file_var.remove("P4")
        active13.config(text="O")

def B14(active14):
    active_content = active14.cget("text")
    if active_content == "O":
        active14.config(text="X")
        file_var.append("P5")
    if active_content == "X":
        file_var.remove("P5")
        active14.config(text="O")

def B15(active15):
    active_content = active15.cget("text")
    if active_content == "O":
        active15.config(text="X")
        file_var.append("P6")
    if active_content == "X":
        file_var.remove("P6")
        active15.config(text="O")

def B16(active16):
    active_content = active16.cget("text")
    if active_content == "O":
        active16.config(text="X")
        file_var.append("P7")
    if active_content == "X":
        file_var.remove("P7")
        active16.config(text="O")

def B17(active17):
    active_content = active17.cget("text")
    if active_content == "O":
        active17.config(text="X")
        file_var.append("P8")
    if active_content == "X":
        file_var.remove("P8")
        active17.config(text="O")

def B18(active18):
    active_content = active18.cget("text")
    if active_content == "O":
        active18.config(text="X")
        file_var.append("P9")
    if active_content == "X":
        file_var.remove("P9")
        active18.config(text="O")

def B19(active19):
    active_content = active19.cget("text")
    if active_content == "O":
        active19.config(text="X")
        file_var.append("P10")
    if active_content == "X":
        file_var.remove("P10")
        active19.config(text="O")

def B20(active20):
    active_content = active20.cget("text")
    if active_content == "O":
        active20.config(text="X")
        file_var.append("P11")
    if active_content == "X":
        file_var.remove("P11")
        active20.config(text="O")

def B21(active21):
    active_content = active21.cget("text")
    if active_content == "O":
        active21.config(text="X")
        file_var.append("P12")
    if active_content == "X":
        file_var.remove("P12")
        active21.config(text="O")

def B22(active22):
    active_content = active22.cget("text")
    if active_content == "O":
        active22.config(text="X")
        file_var.append("P13")
    if active_content == "X":
        file_var.remove("P13")
        active22.config(text="O")

def B23(active23):
    active_content = active23.cget("text")
    if active_content == "O":
        active23.config(text="X")
        file_var.append("P14")
    if active_content == "X":
        file_var.remove("P14")
        active23.config(text="O")

def B24(active24):
    active_content = active24.cget("text")
    if active_content == "O":
        active24.config(text="X")
        file_var.append("P15")
    if active_content == "X":
        file_var.remove("P15")
        active24.config(text="O")

def B25(active25):
    active_content = active25.cget("text")
    if active_content == "O":
        active25.config(text="X")
        file_var.append("P16")
    if active_content == "X":
        file_var.remove("P16")
        active25.config(text="O")

def B26(active26):
    active_content = active26.cget("text")
    if active_content == "O":
        active26.config(text="X")
        file_var.append("P17")
    if active_content == "X":
        file_var.remove("P17")
        active26.config(text="O")

def B27(active27):
    active_content = active27.cget("text")
    if active_content == "O":
        active27.config(text="X")
        file_var.append("P18")
    if active_content == "X":
        file_var.remove("P18")
        active27.config(text="O")

def proof(active1, active2, active4, active5, active6, active7, active8, active9):
    if len(file_var) == 0:
        print("Es wurde nichts ausgewaehlt.")
    else:
        if "A1" in file_var and "A2" in file_var:
            B01(active1)
            B02(active2)
            print("Taskleisten  Einstellungen wurden entfernt.")
        if "A4" in file_var and "A5" in file_var:
            B04(active4)
            B05(active5)
            print("Suchleisten  Einstellungen wurden entfernt.")
        if "A6" in file_var and "A7" in file_var:
            B06(active6)
            B07(active7)
            print("Widgets      Einstellungen wurden entfernt.")
        if "A8" in file_var and "A9" in file_var:
            B08(active8)
            B09(active9)
            print("Aktionsmenue Einstellungen wurden entfernt.")
    
    print("Pruefung abgeschlossen.")

def save(file_var):
    file_paths = work(file_var)
    text = work2(file_paths)
    safe(text)

def work(file_var):
    file_paths = ""
    for file in file_var:
        next_path = dictionary_files.get(file)
        if next_path is not None:
            file_paths += next_path + "\n"
    return file_paths

def work2(file_paths):
    text = ""
    for file_path in file_paths.splitlines():
        inhalt = open(file_path, "r").read()
        text += inhalt + "\n"
    return text

def safe(text):
    # Öffnet den Speichern-Dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".bat",
        filetypes=[("Scheiß Verficktes Windows Script", "*.bat"), ("Alle Dateien", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)