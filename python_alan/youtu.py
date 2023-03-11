#importar modulo
from pytube import YouTube
from pytube.cli import on_progress

#para inserir url do video
link = input('Link to video: ')#inserir o link entre aspas 

#mostrar progresso de download
yt = YouTube(link, on_progress_callback=on_progress)

#mostrar o titulo
print('titulo=',yt.title)

#mostrar que o download iniciou
print ('baixando.....')

#para baixar a meior resoluçao do video
ys = yt.streams.get_highest_resolution()
ys.download()