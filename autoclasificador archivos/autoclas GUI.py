import os
import shutil
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

def organizar_archivos_por_extension(directorio_origen, directorio_destino, progress_var, scrolled_text):
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    archivos = os.listdir(directorio_origen)
    total_archivos = len(archivos)

    for i, filename in enumerate(archivos):
        archivo_origen = os.path.join(directorio_origen, filename)

        if os.path.isfile(archivo_origen):
            _, extension = os.path.splitext(filename)
            extension = extension[1:]
            carpeta_destino = os.path.join(directorio_destino, extension)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            archivo_destino = os.path.join(carpeta_destino, filename)
            shutil.move(archivo_origen, archivo_destino)

            scrolled_text.insert(tk.END, f'Movido: {filename} a {carpeta_destino}\n')
            scrolled_text.see(tk.END)

        progress_var.set((i + 1) / total_archivos * 100)
        root.update_idletasks()

def seleccionar_directorio_origen():
    directorio_origen = filedialog.askdirectory()
    origen_entry.delete(0, tk.END)
    origen_entry.insert(0, directorio_origen)

def seleccionar_directorio_destino():
    directorio_destino = filedialog.askdirectory()
    destino_entry.delete(0, tk.END)
    destino_entry.insert(0, directorio_destino)

root = tk.Tk()
root.title("Organizador de Archivos")

origen_label = ttk.Label(root, text="Directorio Inicial:")
origen_label.pack(pady=5)

origen_entry = ttk.Entry(root, width=50)
origen_entry.pack(pady=5)

origen_button = ttk.Button(root, text="Buscar Inicial", command=seleccionar_directorio_origen)
origen_button.pack(pady=5)

destino_label = ttk.Label(root, text="Directorio Final:")
destino_label.pack(pady=5)

destino_entry = ttk.Entry(root, width=50)
destino_entry.pack(pady=5)

destino_button = ttk.Button(root, text="Buscar Destino", command=seleccionar_directorio_destino)
destino_button.pack(pady=5)

progress_var = tk.DoubleVar()
progress = ttk.Progressbar(root, variable=progress_var, maximum=100, length=300)
progress.pack(pady=10)

info_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
info_text.pack(pady=10)

start_button = ttk.Button(root, text="Organizar Archivos", command=lambda: organizar_archivos_por_extension(origen_entry.get(), destino_entry.get(), progress_var, info_text))
start_button.pack(pady=10)

root.mainloop()