Auszuführende Befehle Windows:

Vorbereitung (Windows)
  lässt das virtual environment ausführbar machen (Für den jeweiligen Benutzer)
    
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

  erstellt ein virtual environemt 
    
    python -m venv venv

  startet das virtual environment
    
    .venv\Scripts\activate

Vorbereitung (Linux)
  erstellt ein virtual environment

    python3 -m venv venv

  startet das virtual environment

    