import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp

def selecionar_diretorio():
    diretorio = filedialog.askdirectory(title="Selecione o diretório de download")
    if diretorio:
        diretorio_entry.delete(0, tk.END)
        diretorio_entry.insert(0, diretorio)
    listar_formatos()

def listar_formatos():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("URL Inválida", "Por favor, insira uma URL do vídeo.")
        return

    opcoes = {
        'format': 'best',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=False)
            formatos = info.get('formats', [])
            format_options = [(f['format_id'], f"{f['format']} - {f.get('height', 'N/A')}p - {f.get('ext', 'N/A')}") for f in formatos]
            formato_combobox['values'] = format_options
            formato_combobox.current(0)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao listar os formatos:\n{e}")

def baixar_video():
    url = url_entry.get().strip()
    diretorio = diretorio_entry.get().strip()
    formato = formato_combobox.get().split(" ")[0]  # Extrai apenas o format_id antes do primeiro espaço
    titulo = titulo_entry.get().strip() if titulo_entry.get().strip() else "%(title)s"

    if not url:
        messagebox.showwarning("URL Inválida", "Por favor, insira uma URL do vídeo.")
        return

    if not diretorio:
        messagebox.showwarning("Diretório Inválido", "Por favor, selecione um diretório.")
        return

    opcoes = {
        'format': formato,
        'outtmpl': f'{diretorio}/{titulo}.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
            messagebox.showinfo("Download Concluído", "O download foi concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo:\n{e}")

janela = tk.Tk()
janela.title("Downloader de Vídeo")
janela.geometry("450x350")

tk.Label(janela, text="URL do Vídeo:").pack(pady=5)
url_entry = tk.Entry(janela, width=50)
url_entry.pack(pady=5)

tk.Label(janela, text="Diretório de Download:").pack(pady=5)
diretorio_frame = tk.Frame(janela)
diretorio_frame.pack(pady=5)
diretorio_entry = tk.Entry(diretorio_frame, width=40)
diretorio_entry.pack(side=tk.LEFT)
tk.Button(diretorio_frame, text="Selecionar", command=selecionar_diretorio).pack(side=tk.LEFT)

tk.Label(janela, text="Formato:").pack(pady=5)
formato_combobox = ttk.Combobox(janela, width=47)
formato_combobox.pack(pady=5)
#tk.Button(janela, text="Listar Formatos", command=listar_formatos).pack(pady=5)

tk.Label(janela, text="Título (opcional):").pack(pady=5)
titulo_entry = tk.Entry(janela, width=50)
titulo_entry.pack(pady=5)

tk.Button(janela, text="Baixar Vídeo", command=baixar_video, bg="blue", fg="white").pack(pady=20)

# Iniciar a interface
janela.mainloop()
