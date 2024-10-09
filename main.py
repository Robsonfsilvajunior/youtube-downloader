import os
from yt_dlp import YoutubeDL
from tkinter import *
from tkinter import messagebox
from tkinter import  filedialog
from tkinter import StringVar

def  download_video(url,formato,path):
    try:
        if formato == 'mp4':
            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s')
            }
        elif formato  == 'mp3':
            ydl_opts = {
                'format': 'bestaudio[ext=m4a]',
                    'outtmpl': os.path.join(path, '%(title)s.%(ext)s')
            }

        with  YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", f"Download concluído em: {path}")

    except  Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {str(e)}")

def escolher_pasta():
    pasta_selecionada =  filedialog.askdirectory()
    caminho_var.set(pasta_selecionada)
    
def iniciar_download():
    url = url_var.get()
    formato = formato_var.get()
    caminho = caminho_var.get()
    
    # Validações
    if not url:
        messagebox.showwarning("Aviso", "Insira um link de vídeo do YouTube.")
        return
    if not caminho:
        messagebox.showwarning("Aviso", "Selecione uma pasta para salvar o arquivo.")
        return
    
    #download principal
    download_video(url, formato, caminho)

# Criando a janela principal
app = Tk()
app.title("YouTube Downloader")
app.geometry("500x300")

# Variáveis
url_var = StringVar()
formato_var = StringVar(value="mp4")
caminho_var = StringVar()

# Interface gráfica
Label(app, text="URL do vídeo do YouTube:").pack(pady=10)
Entry(app, textvariable=url_var, width=50).pack()

Label(app, text="Formato:").pack(pady=10)
Radiobutton(app, text="MP4", variable=formato_var, value="mp4").pack()
Radiobutton(app, text="MP3", variable=formato_var, value="mp3").pack()

Label(app, text="Escolha a pasta de destino:").pack(pady=10)
Entry(app, textvariable=caminho_var, width=50).pack()
Button(app, text="Escolher Pasta", command=escolher_pasta).pack(pady=5)

Button(app, text="Baixar", command=iniciar_download, bg="green", fg="white").pack(pady=20)

# Executando o app
app.mainloop()

