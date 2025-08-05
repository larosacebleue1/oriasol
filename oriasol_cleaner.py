import os
import shutil
import tempfile
import tkinter as tk
from tkinter import messagebox

# Dossiers à nettoyer
clean_targets = {
    "Temp Utilisateur": tempfile.gettempdir(),
    "Temp Windows": r"C:\Windows\Temp",
    "Cache DirectX": os.path.expandvars(r"%LocalAppData%\D3DSCache"),
    "Logs Windows": r"C:\Windows\Logs",
    "Cache Windows Update": r"C:\Windows\SoftwareDistribution\Download"
}

def clean_folder(path):
    deleted = 0
    if os.path.exists(path):
        for item in os.listdir(path):
            try:
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                    deleted += 1
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path, ignore_errors=True)
                    deleted += 1
            except:
                pass
    return deleted

def launch_clean():
    total_deleted = 0
    for label, path in clean_targets.items():
        total_deleted += clean_folder(path)
    messagebox.showinfo("Nettoyage terminé", f"{total_deleted} fichiers ou dossiers supprimés ✅")

def run_app():
    app = tk.Tk()
    app.title("Oriasol Cleaner")
    app.geometry("320x200")
    app.resizable(False, False)

    tk.Label(app, text="ORIASOL CLEANER", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(app, text="Votre PC, propre comme jamais", font=("Arial", 10)).pack()

    tk.Button(app, text="Lancer le nettoyage", command=launch_clean,
              bg="#007acc", fg="white", font=("Arial", 11)).pack(pady=15)

    tk.Button(app, text="Quitter", command=app.quit, font=("Arial", 10)).pack()

    app.mainloop()

run_app()
