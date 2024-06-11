class Film:
    def __init__(self, id : int, title : str) -> None:
        self.__id = id
        self.__title = title
    
    def setID(self, id):
        self.__id = id
    
    def setTitle(self, title):
        self.__title = title

    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm):
        if self.__id == otherFilm.id:
            return True
        else:
            return False