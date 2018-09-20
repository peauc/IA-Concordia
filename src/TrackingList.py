class TrackingList:
    __list = []
    __listName = ""

    def list_has(self, node) -> bool:
        return node in self.__list

    def list_put(self, node) -> None:
        self.__list.append(node)

    def list_remove(self, node) -> None:
        try:
            self.__list.remove(node)
        except ValueError:
            f"Tried to remove the node {node} which was not in the {self.__listName}"
            exit(1)

    def __str__(self) -> str:
        return self.__list.__str__()

    def __init__(self, list_name) -> None:
        super().__init__()
        self.__listName = list_name

