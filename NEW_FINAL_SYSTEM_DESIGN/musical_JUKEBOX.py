class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class songs:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Playlist:
    def __init__(self):
        self.playlist = []
        self.user = []

    def add_to_playlist(self, name):
        self.playlist.append(songs(name))

    def display_playlist(self):
        for i in self.playlist:
            print(i.get_name())

    def check_song_available(self, song):
        for i in self.playlist:
            if i.get_name() == song:
                return i
            else:
                return False


class MusicalPlayer:
    def __init__(self):
        self.playlist = Playlist()
        self.database = {}

    def add_to_playlist(self, name):
        self.playlist.add_to_playlist(name)

    def display_playlist(self):
        self.playlist.display_playlist()

    def user_login(self, name):
        self.user = User(name)
        if name not in self.database:
            self.database[name] = {'name': self.user, 'user_playlist': Playlist()}
            print("User " + self.database[name]['name'].get_name() + " online")
        else:
            print("User is already online ")

    def add_user_playlist(self, name, song):
        value = self.playlist.check_song_available(song)
        if value == False:
            print("song not in the playslist")
        else:
            self.database[name]['user_playlist'].add_to_playlist(song)
        print(self.database[name]['user_playlist'].display_playlist())


myObj = MusicalPlayer()
myObj.add_to_playlist("1")
myObj.add_to_playlist("2")
myObj.add_to_playlist("3")
myObj.add_to_playlist("4")
myObj.display_playlist()

myObj.user_login("Elsy")
myObj.user_login("Elsy")

myObj.add_user_playlist("Elsy", "1")
