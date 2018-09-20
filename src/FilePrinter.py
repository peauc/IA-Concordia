class FilePrinter():
    __file = None

    def __init__(self, fileName) -> None:
        self.__file = open(fileName, "w")
        super().__init__()

    def write(self, string) -> None:
        self.__file.write(string)

    def __del__(self):
        self.__file.close()

