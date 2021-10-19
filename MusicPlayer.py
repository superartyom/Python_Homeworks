import os
import random
import tkinter
from tkinter import ttk
import vlc


class Song:
    def __init__(self, artist, album, year, song_name):
        self.artist = artist
        self.album = album
        self.year = year
        self.name = song_name

    def __str__(self):
        return f'artist: {self.artist}\nAlbum: {self.album}\n Year: {self.year}\n Name: {self.name}'


class PlayList:
    def __init__(self):
        self.songs: [Song] = []

    def load_songs(self, path):
        if not os.path.exists(path):
            return
        with open(path, 'r') as file:
            for x in file.readlines():
                artist, album, year, name = x.split('\t')
                song = Song(artist, album, year, name)
                self.songs.append(song)

    def add_song(self, artist, album, year, name):
        for sng in self.songs:
            if sng.name == name and sng.artist == artist and sng.year == year and sng.year == album:
                self.songs.append(Song(artist, album, year, name))

    def remove_song(self, artist, album, year, name):
        for sng in self.songs:
            if sng.name == name and sng.artist == artist and sng.year == year and sng.year == album:
                self.songs.remove(sng)

    def show_songs(self):
        for song in self.songs:
            print(song)
            print("_" * 100)


class Player:
    i = 0

    def __init__(self, playlist):
        self.playlist: PlayList = playlist
        self.is_playing = False
        self.now_playing = ''
        self.media_player = vlc.MediaPlayer()

    def setup(self):
        pass

    def play(self, play_index=0):
        if play_index > len(self.playlist.songs):
            print(f'No song at index {play_index}')
            return
        if not self.is_playing:
            media = vlc.Media('')
            self.media_player.set(media)
            self.media_player.play()
            self.is_playing = True
            # self.now_playing = self.playlist.songs[play_index]
            # print(f'Now playing\n{self.playlist.songs[play_index]}')
            # print('=' * 100)
        else:
            print('Player is already active')
            print('=' * 100)
        return

    def show_current_song_info(self):
        print('=' * 100)
        print(self.now_playing)
        print('=' * 100)

    def next_song(self):
        index = self.playlist.songs.index(self.now_playing)
        if index <= len(self.playlist.songs) - 1:
            self.is_playing = False
            self.play(index)
        else:
            print('We have reached the end of our playlist')

    def prev_song(self):
        index = self.playlist.songs.index(self.now_playing) - 1
        if index > 0:
            self.is_playing = False
            self.play(index)
        else:
            print('We have reached the beginning of our playlist')
        self.play(index)

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            print('The player has been stopped')
        else:
            print('Player is not active')

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            self.media_player.set_pause(1)
            print('The player has been paused')
        else:
            print('Player is not active')

    def shuffle(self):
        shuffled = self.playlist.songs.copy()
        shuffled.remove(self.now_playing)
        random.shuffle(shuffled)
        self.playlist.songs = shuffled.insert(0, self.now_playing)

    def __str__(self):
        return f'This player has a playlist containing {len(self.playlist.songs)} songs'


if __name__ == '__main__':
    window = tkinter.Tk()

    window.title('Music Player')
    window.geometry('480x260')
    window.resizable(width=False, height=False)

    playlist = PlayList()
    player = Player(playlist)

    txt = tkinter.StringVar(value='Nothing Plays')
    # Status Label
    Status = tkinter.Label(window, textvar=txt, font=('Helvetica', 15), borderwidth=1, relief='flat')
    Status.grid(row=0, column=0, columnspan=4, sticky='ew')
    # Volume scale
    Volume = ttk.Scale(window)
    Volume.grid(row=1, column=0, columnspan=4, sticky='ew')
    # Buttons
    Play_Button = tkinter.Button(window, text='Play', font=('Helvetica', 10, 'bold'), width=10, height=2, relief='flat',
                                 borderwidth=1, background='#0fa621', activebackground='#0fa621', command=Player.play)
    Play_Button.grid(row=2, column=0, sticky='ew')
    Play_Button.bind('<Button-1>', func=Player.play)
    Pause_Button = tkinter.Button(window, text='Pause', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                  relief='flat', borderwidth=1, background='#ff0000', activebackground='#ff0000')
    Pause_Button.grid(row=2, column=1, sticky='ew')
    Pause_Button.bind('<Button-1>', func=Player.pause)
    Previous_Button = tkinter.Button(window, text='Previous song', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                     relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
    Previous_Button.grid(row=2, column=2, sticky='nsew')

    Next_Button = tkinter.Button(window, text='Next song', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                 relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
    Next_Button.grid(row=2, column=3, sticky='ew')
    # Song List Box
    List = tkinter.Listbox(window)
    List.grid(row=3, column=0, columnspan=4, sticky='nsew')

    # Scrollbar
    Scroll = tkinter.Scrollbar(window)
    Scroll.grid(column=3, row=3, sticky='esn')

    # Connecting scrollbar to list box
    List.config(yscrollcommand=Scroll.set)
    Scroll.config(command=List.yview)
    # Connecting list box to song list
    # with open('./Albums.txt') as words:
    #     for
    #

    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)
    window.columnconfigure(3, weight=2)
    window.mainloop()
