import os
from tkinter import filedialog

global file_var
file_var = ["G1"]
dictionary_files = {
        "G1": "Allgemeine Einstellungen/10_adminrechte.bat",
        "A1": "Allgemeine Einstellungen/1_Taskleiste_links.bat",
        "A2": "Allgemeine Einstellungen/2_Taskleiste_zentriert.bat",
        "A3": "Allgemeine Einstellungen/3_Standard_Hintergrundfestlegen.bat",
        "A4": "Allgemeine Einstellungen/4_Suchleistenbildchen_deaktivieren.bat",
        "A5": "Allgemeine Einstellungen/5_Suchleistenbildchen_aktivieren.bat",
        "A6": "Allgemeine Einstellungen/6_Widgets_deaktivieren.bat",
        "A7": "Allgemeine Einstellungen/7_Widgets_aktivieren.bat",
        "A8": "Allgemeine Einstellungen/8_klassisches_Aktionsmenue.bat",
        "A9": "Allgemeine Einstellungen/9_modernes_Aktionsmenue.bat",
        "P1": "Programm Einstellungen/1_remove_apps_prov_package.bat"
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

def proof(active1, active2, active4, active5, active6, active7, active8, active9):
    if len(file_var) == 1:
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