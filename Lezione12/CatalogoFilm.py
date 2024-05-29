class MovieCatalog():
    def __init__(self) -> None:
        self.catalogo : dict = {}

    def add_movie(self, director_name : str, movies : list):
        if director_name not in self.catalogo:
            self.catalogo[director_name] = movies
    
    def remove_movie(self, director_name, movie_name):
        for i in self.catalogo:
            if director_name == self.catalogo[director_name]:
                if movie_name == self.catalogo[]
        
