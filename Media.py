import webbrowser


# Define The Class To Store My Favorite Movies
class Movie():
    """ Movie Class Contains The Defined Data OF
            The Movies That Will Be Stored With The
            Following Attributes
        ...
        ...

        Attributes:
            title: The Name Of The Movie
            Poster: The Movie Poster Image
            Trailer: The Movie Trailer Video
            ...
    """
    def __init__(self, Title, Poster, Trailer):
        """ Inits Movie class with The Previous Mentioned Attributes
        """
        self.title = Title
        self.poster_image_url = Poster
        self.trailer_youtube_url = Trailer
