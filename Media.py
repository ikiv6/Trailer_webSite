import webbrowser
# Define The Class To Store My Favorite Movies
class Movie():
    def __init__(self,Title,Poster,Trailer):

        self.title = Title
        self.poster_image_url = Poster
        self.trailer_youtube_url =Trailer
# Define A Function to Run The Movie Trailer 
    def Show_Trailer(self):
        webbrowser.open(self.Movie_Trailer)
