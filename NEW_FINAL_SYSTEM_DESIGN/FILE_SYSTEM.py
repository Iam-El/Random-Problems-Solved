class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.path = "/" + name
        self.parent = parent

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_full_path(self):
        if self.parent is not None:
            return self.parent.get_full_path() + self.path
        else:
            return self.path


class Directory(Folder):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.content = []

    def create_file(self, file_name):
        file = File(file_name, self)
        self.content.append(file)

    def create_folder(self, folder_name):
        file = Directory(folder_name, self)
        self.content.append(file)

    def print_contents(self):
        for f in self.content:
            print(f.get_full_path())



    def get_folder(self,folder_name):
        for f in self.content:
            if folder_name==f.get_name():
                return f



class File(Folder):
    def __init__(self, name, parent):
        super().__init__(name, parent)


fileSystem = Directory("Home", None)

fileSystem.create_folder("ttgtgtgtgt")

fileSystem.print_contents()

folder=fileSystem.get_folder("ttgtgtgtgt")

folder.create_file("somefile")

folder.print_contents()



#
# fileSystem.create_file("elsy.py")
#
#
#
# fileSystem.print_contents()







# file1 = File("Elsy", fileSystem)
# file2 = File("Aaron", fileSystem)
# folder = Directory("NewFolder", fileSystem)
# file3 = File("Aaron4444", folder)
#
# print(fileSystem.get_full_path())
# print(file1.get_full_path())
# print(file2.get_full_path())
# print(folder.get_full_path())
# print(file3.get_full_path())
