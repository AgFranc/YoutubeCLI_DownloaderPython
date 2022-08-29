
from rich.progress import track
from pytube import YouTube 
from rich.console import Console
import time
from pytube import Stream
from pytube import YouTube
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich import print
from rich.pretty import Pretty
from rich.panel import Panel
 
console = Console()


def text():
    console.print("""_____________________________________________________________________________         
 _____________________________________________________________________________        
  ____/\\\\\__/\\\\\\\\\\_____/\\\\\\\\\\_______________/\\\\\\\\\\\\\\\\\____/\\\\\\\\\_/\\\\___________       
   ___\//\\\\\/\\\\\___/\\\\\\\\\\\\\\\\\\\\\____________/\\\\\/////\\\\\___\//\\\\\/\\\\\____________      
    ____\//\\\\\\\\\___\////\\\\\////____________\/\\\\\\\\\\\\\\\\\\\\_____\//\\\\\\\\\_____________     
     _____\//\\\\\_______\/\\\\\________________\/\\\\\//////_______\//\\\\\______________    
      __/\\\\_/\\\\\________\/\\\\\_/\\\\____________\/\\\\\__________/\\\\_/\\\\\_______________   
       _\//\\\\\\\\/_________\//\\\\\\\\\_____________\/\\\\\_________\//\\\\\\\\/________________  
        __\////____________\/////______________\///___________\////__________________ """, style="bold red")
    console.print("EJEMPLO: ruta\\ruta\\nombre.mp3", style="bold red")
    console.print("SALIR = 0", style="bold blue")

 
def yt_python_downloader():
    def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
        pbar.update(len(data_chunk))
    try:
        print("Pega el enlace: ")
 
        def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
            pbar.update(len(data_chunk))


        url = input()
        yt = YouTube(url, on_progress_callback=progress_callback)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading video to '{stream.default_filename}'")
        pbar = tqdm(total=stream.filesize, unit="bytes")
        path = stream.download()
        pbar.close()

        #table
         
        #print(f"Saved video to {path}")  
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Fecha", style="dim", width=12)
        table.add_column("Titulo")
        table.add_column("Estado", justify="right")
        table.add_column("Ubicación", justify="right")
        table.add_row(
    "Today", f"{stream.default_filename}", "DESCARGADO", f"{path}"
)
 
 
        console.print(table)
 
        console.print(Panel("Desea descargar algun video? 2 veces =>   0/1"))
        ans = int(input())
    except:
        print("Intenta de nuevo")


#"http://youtube.com/watch?v=2lAe1cqCOXo"
  # https://www.youtube.com/watch?v=HXdmtAQYTpY
console.print("Desea descargar algun video :smiley: ?  0/1")
ans = int(input())
while ans != 0:
    text()  
    yt_python_downloader()
    ans = int(input())
console.print("Gracias :raccoon: :thumbs_up:")
