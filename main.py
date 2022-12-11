import moviepy.editor
from colorama import init, Style, Fore


def mp():
    Path = input(Fore.BLUE + "Введите видео-файл:")
    try:
      video = moviepy.editor.VideoFileClip(f'{Path}')
      audio = video.audio
      audio.write_audiofile(f'{Path}.mp3')
      print(Fore.GREEN + "Готово")
    except:
      print(Fore.RED + 'Ошибка')

mp()