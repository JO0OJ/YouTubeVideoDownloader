import tkinter as tk
from tkinter import filedialog

def criar_entry_rotulada(janela, texto, largura=50):
    tk.Label(janela, text=texto).pack(pady=5)
    entry = tk.Entry(janela, width=largura)
    entry.pack(pady=5)
    return entry

def criar_diretorio_selecao(janela, entry):
    diretorio = filedialog.askdirectory(title="Selecione o diretório de download")
    if diretorio:
        entry.delete(0, tk.END)
        entry.insert(0, diretorio)
