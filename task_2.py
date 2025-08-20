class Movies:
    def __init__(self, movies=None):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'    

class Drama(Movies):

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драма: {self.movies}'  
    
comedy = Comedy()
drama = Drama()
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))