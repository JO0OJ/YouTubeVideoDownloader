import yt_dlp
from tkinter import messagebox

# Lista de formatos de vídeo sem áudio
FORMATOS_VIDEO_SEM_AUDIO = [
    "242", "243", "244", "247", "278", "302", "303", "394", "395", "396",
    "397", "398", "399", "598", "602", "603", "604", "605", "606", "612", "617"
]

# Lista de formatos que não funcionam corretamente
FORMATOS_NAO_FUNCIONAM = [
    "600_drc", "133", "134", "135", "136", "160", "229", "230", "231",
    "269", "298", "299", "311", "312", "597"
]

def listar_formatos(url, combobox):
    if not url:
        messagebox.showwarning("URL Inválida", "Por favor, insira uma URL do vídeo.")
        return

    opcoes = {'format': 'best', 'quiet': True}

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=False)
            formatos = info.get('formats', [])
            format_options = [
                (f['format_id'], f"{f['format']} - {f.get('height', 'N/A')}p - {f.get('ext', 'N/A')}")
                for f in formatos if f['format_id'] not in FORMATOS_NAO_FUNCIONAM
            ]
            combobox['values'] = format_options
            combobox.current(0)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao listar os formatos:\n{e}")

def baixar_video(url, diretorio, formato_selecionado, titulo):
    if not url:
        messagebox.showwarning("URL Inválida", "Por favor, insira uma URL do vídeo.")
        return
    if not diretorio:
        messagebox.showwarning("Diretório Inválido", "Por favor, selecione um diretório.")
        return

    opcoes = {'outtmpl': f'{diretorio}/{titulo}.%(ext)s'}
    somente_video = formato_selecionado in FORMATOS_VIDEO_SEM_AUDIO

    opcoes['format'] = f"{formato_selecionado}+140" if somente_video else formato_selecionado

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
            messagebox.showinfo("Download Concluído", "O download foi concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo:\n{e}")
