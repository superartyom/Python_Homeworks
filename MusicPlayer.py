import os
import random
import tkinter
from tkinter import ttk


class Song:
    def __init__(self, artist, song_name, length, album=None, year=None):
        self.artist = artist
        self.album = album
        self.year = year
        self.name = song_name
        self.length = length
    def __str__(self):
        return f'artist: {self.artist}\nAlbum: {self.album}\n Year: {self.year}\n Name: {self.name}'


class PlayList:
    def __init__(self):
        self.songs: [Song] = []

    # @staticmethod
    def load_songs(self, path, listbox: tkinter.Listbox):
        if not os.path.exists(path):
            return

        files = os.listdir(path)
        for index, file in enumerate(files):
            ffile, extension = file.split('.')
            if extension == 'mp3':
                length = MP3('/'.join.([path, file])).info.length
                artist, name = ffile.split(' - ')
                listbox.insert(index, file)
                song = Song(artist, name, length)
                song.id = index
                self.songs.append(song)

        # with open(path, 'r') as file:
        #     for x in file.readlines():
        #         artist, album, year, name = x.split('\t')
        #         song = Song(artist, album, year, name)
        #         self.songs.append(song)

    def add_song(self, artist, name, album, year):
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


class Screen(tkinter.Tk):
    pass


class Player(tkinter.Frame):
    i = 0

    def __init__(self, playlist, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.playlist: PlayList = playlist
        self.is_playing = False
        self.now_playing = ''
        # self.media_player = vlc.MediaPlayer()
        self.current_timestep = 0
    def setup_player(self):
        self.grid(column=0, row=0, sticky='ewns')
        txt = tkinter.StringVar(value='Nothing Plays')
        # Status Label
        Status = tkinter.Label(self, textvar=txt, font=('Helvetica', 15), borderwidth=1, relief='flat')
        Status.grid(row=0, column=0, columnspan=4, sticky='ew')
        # Volume scale
        time = ttk.Scale(self)
        time.grid(row=1, column=0, columnspan=4, sticky='ew')
        # Buttons
        Play_Button = tkinter.Button(self, text='Play', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                     relief='flat',
                                     borderwidth=1, background='#0fa621', activebackground='#0fa621',
                                     command=Player.play)
        Play_Button.grid(row=2, column=0, sticky='ew')
        Play_Button.bind('<Button-1>', func=Player.play)
        Pause_Button = tkinter.Button(self, text='Pause', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                      relief='flat', borderwidth=1, background='#ff0000', activebackground='#ff0000')
        Pause_Button.grid(row=2, column=1, sticky='ew')
        Pause_Button.bind('<Button-1>', func=Player.pause)
        Previous_Button = tkinter.Button(self, text='Previous song', font=('Helvetica', 10, 'bold'), width=10,
                                         height=2,
                                         relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
        Previous_Button.grid(row=2, column=2, sticky='nsew')

        Next_Button = tkinter.Button(self, text='Next song', font=('Helvetica', 10, 'bold'), width=10, height=2,
                                     relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
        Next_Button.grid(row=2, column=3, sticky='ew')
        # Song List Box
        List = tkinter.Listbox(self)
        List.grid(row=3, column=0, columnspan=4, sticky='nsew')

        def get_name(event):
            name = event.widget.get(event.widget.curselocation())
            print(name)

        List.bind('<Double-Button>', get_name)
        # Scrollbar
        Scroll = tkinter.Scrollbar(self)
        Scroll.grid(column=3, row=3, sticky='esn')

        # Connecting scrollbar to list box
        List.config(yscrollcommand=Scroll.set)
        Scroll.config(command=List.yview)
        # LoadSongsFromPath
        self.playlist.load_songs('./Music', List)

    def play(self, song=None, play_index=0):
        if play_index > len(self.playlist.songs):
            print(f'No song at index {play_index}')
            return
        if self.current_timestep and self.now_playing == ' - '.join([song.artist, song.name])+'.mp3':
            # self.media_player.set_pause(0)
            self.is_playing = True
            return
        if not self.is_playing:
            path = '.Music/Muse - Pressure.mp3'
            if song:
                path = '.Music/' + ' - '.join([song.artist, song.name])+'.mp3'
            self.now_playing = path.split('/')[-1]
            # media = vlc.Media('')
            # print(self.media_player.get_time() / 1000)
            # self.media_player.set(media)
            # self.media_player.play()
            # self.is_playing = True
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
            self.current_timestep = self.media_player.get_time() // 1000
            self.current_timestep = self.
            self.is_playing = False
            # self.media_player.set_pause(1)
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

    def select_song(self, event):
        self.is_playing = False
        self.now_playing = event.widget.get(event.widget.curselocation())
        artist, song_name = self.now_playing.split('-')
        song_name = song_name.split('.')[0]
        self.play()
        for song in self.playlist.songs:
            if song.name == song_name and song.artist == artist:
                self.play(song)
            else:
                return

if __name__ == '__main__':
    window = tkinter.Tk()

    window.title('Music Player')
    window.geometry('480x260')
    window.resizable(width=False, height=False)

    playlist = PlayList()
    player = Player(playlist, window)
    player.setup_player()

    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)
    window.columnconfigure(3, weight=2)
    window.mainloop()
