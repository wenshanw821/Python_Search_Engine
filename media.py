import webbrowser

class Movie():

    '''The class provides a way to store movie related information. '''

    valid_rating = ['G', 'PG', 'PG-13', 'R']
    # give the memory for a movie.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_youtube_url)
