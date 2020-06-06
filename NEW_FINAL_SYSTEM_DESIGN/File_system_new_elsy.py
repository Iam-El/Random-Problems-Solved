class Folder:
    def __init__(self, name, path, parent=None):
        self.name = name
        self.path = path
        self.parent = parent

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_parent(self):
        return self.path

    def set_name(self):
        return self.name

    def set_path(self):
        return self.path

    def set_parent(self):
        return self.parent

    def print_full_path(self):
        if self.parent is not None:
            return (self.parent.print_full_path() + self.path + self.name)
        else:
            return self.path + self.name


class Directory(Folder):
    def __init__(self, name, path, parent):
        super().__init__(name, path, parent)
        self.content=[]

    def create_new_folder(self,folder_name,path):
        folder=Directory(self,folder_name,path)
        self.content.append(folder)

    def print_folder(self):
        for i in self.content:
            return i.print_full_path()


class File(Folder):
    def __init__(self, name, path, parent):
        super().__init__(name, path, parent)


fileSystem = Directory("Home", '/', None)

file1 = File("elsy", fileSystem.get_path(), fileSystem)

print(file1.print_full_path())

fileSystem.create_new_folder("Newfolder",fileSystem)

print(fileSystem.print_folder())