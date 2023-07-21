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
    #console.print("EJEMPLO: ruta\\ruta\\nombre.mp3", style="bold red")
    console.print("SALIR = 0", style="bold blue")

 
def yt_python_downloader(url):
    def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
        pbar.update(len(data_chunk))
    try:
          
 
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
    except Exception as e:
        print("Error al descargar el video: ", str(e))
  
        
  
   #https://www.youtube.com/watch?v=IbAuuxBFwoo

def descargar_video(url, carpeta_destino="."):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Seleccionar la resolución más alta disponible
        stream = video.streams.get_highest_resolution()

        # Descargar el video en la carpeta especificada
        stream.download(output_path=carpeta_destino)

        print("¡Descarga completada con éxito!")
    except Exception as e:
        print("Error al descargar el video:", str(e))
        
#"http://youtube.com/watch?v=2lAe1cqCOXo"
  # https://www.youtube.com/watch?v=HXdmtAQYTpY
console.print("Desea descargar algun video :smiley: ?  0/1")
ans = int(input())
while ans != 0:
    #text()  
    print("Pega el enlace o sal con(0): ")
     
    try:
      url_video = str(input())
      if(url_video=="0"):
          break
      carpeta_destino = "./videos"
   # descargar_video(url_video, carpeta_destino)
      yt_python_downloader(url_video)
 
    except Exception as e:
      print('Quizas escribiste el enlace mal.')
console.print("Gracias :raccoon: :thumbs_up:")
