import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def clean_folder(path):
    deleted = 0
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                    deleted += 1
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    deleted += 1
            except Exception as e:
                print(f"Impossible de supprimer : {item_path} ({e})")
    except Exception as e:
        print(f"Accès refusé à : {path} ({e})")
    return deleted

def run_cleaning():
    folders_to_clean = [
        os.getenv('TEMP'),
        os.getenv('TMP'),
        str(Path.home() / "AppData" / "Local" / "Temp"),
    ]

    total_deleted = 0
    for folder in folders_to_clean:
        total_deleted += clean_folder(folder)

    messagebox.showinfo("Nettoyage terminé", f"{total_deleted} fichiers/dossiers supprimés.")

# Interface utilisateur
window = tk.Tk()
window.title("Oriasol Cleaner")
window.geometry("300x150")

btn_clean = tk.Button(window, text="🧹 Lancer le nettoyage", command=run_cleaning, font=("Arial", 12))
btn_clean.pack(pady=20)

btn_quit = tk.Button(window, text="Quitter", command=window.quit, font=("Arial", 10))
btn_quit.pack()

window.mainloop()
