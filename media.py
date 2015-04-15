# This class provides a way to store movie related information
class Movie():
    """ This class provides a way to store movie related information"""

    # Constructor:
    #   Params
    #     - movie_title - Title of movie
    #     - movie_tagline - Tagline for the movie (from posters, etc)
    #     - poster_image - URL to poster image
    #     - trailer_youtube - URL to Youtube trailer for movie
    def __init__(self, movie_title, movie_tagline, poster_image, trailer_youtube):
        self.title = movie_title
        self.tagline = movie_tagline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

