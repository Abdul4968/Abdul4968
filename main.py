from pytube import YouTube
from colorama import init, Fore
import os
 
def on_complete(stream, filepath):
    print("Download Complete!")
    print(filepath)
 
def on_progress(stream, chunk, bytes_remaining):
    progress_string = f"{round(100 - (bytes_remaining / stream.filesize * 100),2)}%"
    print(progress_string)

while True:
  init()
  link = input("Youtube link: ")
  video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)
   
  
  os.system("clear")
  print(Fore.RED + f"link:       \033[39m {link}")
  print(Fore.RED + f"Thumbnail:  \033[39m {video_object.thumbnail_url}")
  print(Fore.GREEN + f"Title:      \033[39m {video_object.title}")
  print(Fore.GREEN + f"Author:     \033[39m {video_object.author}")
  print(Fore.BLUE + f"Length:     \033[39m {round(video_object.length / 60,2)} minutes")
  print(Fore.BLUE + f"Views:      \033[39m {video_object.views / 1000000} million")
  
  print("")
  
  print(
      Fore.YELLOW + "Download options:" + 
      Fore.GREEN + "(b)est \033[39m|" + 
      Fore.RED + " (w)orst \033[39m|" + 
      Fore.BLUE + " (a)udio \033[39m")
  download_choice = input("Choice: ")
   
  if download_choice == "b":
      vd = video_object.streams.get_highest_resolution().download()
  elif download_choice == "w":
      vd = video_object.streams.get_lowest_resolution().download()
  elif download_choice == "a":
      vd = video_object.streams.get_audio_only().download()
  else:
      exit
  
  #vd.show()
