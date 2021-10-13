"""OOP"""

import os
import random


# MusicPlayer homework
# Now we are going to add some more methods to our classes. It makes sense to have an add_song and remove_song
# methods in our playlist class, so we can modify our playlist whenever we'd like to.
# So:
#   a) Create an add_song method in Playlist class. The method should take a Song as a parameter (or name, artist
#   etc. e.g. the parameters needed to create a song) and add it to our song list
#   b) Create a remove_song method in Playlist class. The method should take a Song as a parameter and remove it
#   from our song list.
#   c) Now, we need to develop our Player class. Add a play method. The method will print which song is playing now.
#   By default when we press play on a player it starts playing the first song, so you can do just that. Also,
#   your player needs to know whether it plays something at the moment or no (so a boolean attribute can be useful).
#   d) Create a method to show the current songs' information. If no song is playing, let the user know.
#   e) Create two methods - next_song and prev_song. When we call these methods, the next song in the playlist
#   will start playing.
#   f) Create a shuffle method, which will shuffle our playlist.
# When you've reached this point, feel free to add some other methods, which you'll find useful (for example search
# for a song, show the playlist, etc.). Good luck!

# Մեր կլասերը ընլայնելու ժամանակն է։ Նախ մեր Playlist կլասին ավելացնենք add_song և remove_song մեթոդներ։
#   a) Ստեղծել add_song մեթոդ, որը կվերցնի մեկ արգումենտ՝ Song, կամ չորս արգումենտ, որոնցով հնարավոր է ստեղծել Song տիպի
#   օբյեկտ։
#   b) Ստեղծել remove_song մեթոդ, որը կվերցնի մեկ արգումենտ` Song, և կջնջի տվյալ երգը song_list-ից։
#   c) Player կլասին ավելացնել play մեթոդ։ Մեթոդը կտպի, թե որ երգն է միացել։ Նվագարկիչները սովորաբար սկսում են երգել
#   առաջին երգից։ Կարող եք մեթոդը հենց այդպես իմպլեմենտացնել։
#   d) Ստեղծել մեթոդ, որը ցույց կտա միացած երգի ինֆորմացիան։ Եթե ոչ մի երգ միացած չէ, տեղեկացնել։
#   e) Ստեղծել երկու մեթոդ` next_song և prev_song։ Այս մեթոդները կանչելուց համապատասխանաբար կմիանա հաջորդ կամ նախորդ
#   երգը
#   f) Ստեղծել shuffle մեթոդ, որը կխառնի playlist-ի երգերը։
# Այս ամենը ստեղծելուց հետո կարող եք ավելացնել ցանկացած այլ մեթոդ, որ անհրաժեշտ կհամարեք։ Բոլորիդ հաջողությու՛ն։
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

    def play(self, play_index=0):
        if play_index > len(self.playlist.songs):
            print(f'No song at index {play_index}')
            return
        if not self.is_playing:
            self.is_playing = True
            self.now_playing = self.playlist.songs[play_index]
            print(f'Now playing\n{self.playlist.songs[play_index]}')
            print('=' * 100)
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
            print('Player isnt active')

    def shuffle(self):
        shuffled = self.playlist.songs.copy()
        shuffled.remove(self.now_playing)
        random.shuffle(shuffled)
        self.playlist.songs = shuffled.insert(0, self.now_playing)

    def __str__(self):
        return f'This player has a playlist containing {len(self.playlist.songs)} songs'
