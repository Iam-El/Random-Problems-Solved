# music player system design


class User():

    def __init__(self, fn, email):
        self.fn = fn
        self.email = email
        self.playlist=Playlist()
        self.favorites=Playlist()


    def get_firstname(self):
        return self.fn

    def get_email(self):
        return self.email

    def get_userinfor(self):
        return self.fn + "---Email ID--->" + self.email

    def add_song_to_user(self,songs):
        self.playlist.add_songs(songs)

    def get_user_song(self):
        return self.playlist.get_songs()



class Playlist:

    def __init__(self, songs=[]):
        self.songs = songs

    def get_songs(self):
        return self.songs

    def add_songs(self,songs):
        self.songs.append(songs)



class CDplayer:
    pass



# class Favorites:
#
#     def __init__(self, favorites):
#         self.favorites = favorites
#




# Main music player class


class MusicPlayer:

    # Constructor
    def __init__(self, songs):
        self.database = {}
        self.session = {}
        self.playlist = Playlist(songs)

    def add_user(self, fn, email):
        user_name = User(fn, email)
        if email not in self.database:
            self.database[email] = user_name
        else:
            print("User is already in our database!!!!!")

    def check_online(self, email):
        if email not in self.session:
            self.session[email] = self.database[email]
        else:
            print("User is not online currently")
        return self.session

    def make_offline(self, email):
        if email in self.session:
            del self.session[email]
            return self.session
        else:
            print("User is already Offline")

    def check_offline(self, email):
        if email in self.session:
            print("User is Online")
        else:
            print("User is OFFline")

    def get_user_info(self, email):
        return self.session[email].get_userinfor()

    def get_universal_playlist(self):
        return self.playlist.get_songs()

    def add_user_playlist(self, email, song):
        songs = self.get_universal_playlist()

        if song in songs:
            print(song)
            self.database[email].add_song_to_user(song)
            print(self.database[email].get_user_song())
            print("congratulations !! song been added to the playlist")
            print("---------")
        else:
            print("Song doesnt exist in playlist")

    # def add_user_favorites(self,email):
    #     userSongs=self.database[email].get_user_song()
    #     favorites = Favorites(userSongs)
    #     print(userSongs)




my_obj = MusicPlayer(["a", "b", "c", "d", "e"])
my_obj.add_user("Elsy", "elsyfernandes215@gmail.com")
print(my_obj.check_online('elsyfernandes215@gmail.com'))
print(my_obj.get_user_info('elsyfernandes215@gmail.com'))
print(my_obj.get_universal_playlist())
my_obj.add_user_playlist('elsyfernandes215@gmail.com', 'b')
my_obj.add_user_playlist('elsyfernandes215@gmail.com', 'p')
my_obj.add_user_playlist('elsyfernandes215@gmail.com', 'a')
my_obj.add_user_favorites('elsyfernandes215@gmail.com','b')
# print(my_obj.add_user_favorites('elsyfernandes215@gmail.com'))
# my_obj.check_offline('elsyfernandes215@gmail.com')
