class MovieCatalog():
    def __init__(self) -> None:
        self.catalogo : dict = {}

    def add_movie(self, director_name : str, movies : list):
        if director_name not in self.catalogo:
            self.catalogo[director_name] = movies
        else:
            self.catalogo[director_name] = movies
    
    def remove_movie(self, director_name, movie_name):
        for k, v in self.catalogo.items():
            if director_name == k:
                for i in v:
                    if i == movie_name:
                        v.remove(movie_name)
    
    def list_directors(self):
        for k, v in self.catalogo.items():
            print(k, "\n")

    def get_movies_by_director(self, director_name):
        for k, v in self.catalogo.items():
            if director_name == k:
                print(f"i film di {k} sono: {v}")
    
    def search_movies_by_title(self, title):
        for k, v in self.catalogo.items():
            for i in v:
                if title == i:
                    print(k, " ", i)
                    break
                else:
                    print("nessun film con quel titolo")
                    break

catalogo : MovieCatalog = MovieCatalog()

catalogo.add_movie("tarantino", ["django", "pulp fiction", "trinita"])
catalogo.add_movie("christofer nolan", ["oppenheimer", "interstellar"])
catalogo.add_movie("leonardo", ["Fioravanti"])

catalogo.remove_movie("tarantino", "django")

catalogo.list_directors()

catalogo.get_movies_by_director("christofer nolan")

catalogo.search_movies_by_title("oppenheimer")