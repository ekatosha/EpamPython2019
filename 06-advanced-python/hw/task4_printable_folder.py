import os


class PrintableFolder:
    def __init__(self, name, content=None):
        self.name = name
        self.content = []
        self._print = []
        index = name.rfind("\\")
        for root, dirs, files in os.walk(name, topdown=False):
            for file_name in files:
                self.content.append(file_name)
                self._print.append('{}\{}'.format(root[index:], file_name))
            for file_name in dirs:
                self.content.append(file_name)
        self.name = name[index+1:]

    def __str__(self):
        return "\n".join(self._print)

    def __iter__(self):
        return iter(self.content)


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name  # print out the file name

    def __eq__(self, value):
        return self.name == value
