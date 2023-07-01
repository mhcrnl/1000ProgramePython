import tkinter as tk
from tkinter import filedialog
from pygame import mixer

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        play_song(file_path)

def play_song(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def stop_song():
    mixer.music.stop()

def create_player():
    player = tk.Tk()
    player.title("Song Player")

    open_button = tk.Button(player, text="Open", command=open_file)
    open_button.pack()

    stop_button = tk.Button(player, text="Stop", command=stop_song)
    stop_button.pack()

    player.mainloop()

create_player()
