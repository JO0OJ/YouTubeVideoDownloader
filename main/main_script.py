import tkinter as tk
from tkinter import ttk
from main import downloader, gui_elements

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Downloader de Vídeo")
    janela.geometry("450x350")

    # Criação dos widgets
    url_entry = gui_elements.criar_entry_rotulada(janela, "URL do Vídeo:")
    diretorio_entry = gui_elements.criar_entry_rotulada(janela, "Diretório de Download:")

    diretorio_btn = tk.Button(
        janela, text="Selecionar",
        command=lambda: gui_elements.criar_diretorio_selecao(janela, diretorio_entry)
    )
    diretorio_btn.pack()

    formato_combobox = ttk.Combobox(janela, width=47)
    tk.Label(janela, text="Formato:").pack(pady=5)
    formato_combobox.pack(pady=5)

    titulo_entry = gui_elements.criar_entry_rotulada(janela, "Título (opcional):")

    tk.Button(
        janela, text="Baixar Vídeo", bg="blue", fg="white",
        command=lambda: downloader.baixar_video(
            url_entry.get().strip(),
            diretorio_entry.get().strip(),
            formato_combobox.get().split(" ")[0],
            titulo_entry.get().strip() or "%(title)s"
        )
    ).pack(pady=20)

    # Evento para listar os formatos ao selecionar o diretório
    url_entry.bind("<FocusOut>", lambda e: downloader.listar_formatos(url_entry.get(), formato_combobox))

    # Iniciar a interface
    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
