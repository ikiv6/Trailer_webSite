import fresh_tomatoes
import Media
# List Of My Favorite Movies That Contains The (Title,Image Poster,Trailer URL)
Deadpool = Media.Movie(
                       "Deadpool",
                       "https://goo.gl/HXVR9v",
                       "https://youtu.be/FyKWUTwSYAs?t=50")
Evile_Dead = Media.Movie("Evil Dead",
                         "https://goo.gl/Lx6iuE",
                         "https://www.youtube.com/watch?v=lWG_w5w8ZLs")
What_Happened_To_Monday = Media.Movie(
    "What Happened To Monday",
    "https://goo.gl/nmsas6",
    "https://www.youtube.com/watch?v=5F-YEbm65a8")
The_Stangers = Media.Movie("The Strangers",
                           "https://goo.gl/V5wzCh",
                           "https://www.youtube.com/watch?v=91-Z20uttEk")
IT = Media.Movie("IT",
                 "https://goo.gl/CQD2nA",
                 "https://www.youtube.com/watch?v=hAUTdjf9rko")
The_Conjuring_2 = Media.Movie("The Conjuring 2",
                              "https://goo.gl/4MevCZ",
                              "https://www.youtube.com/watch?v=VFsmuRPClr4")
# Array TO Store The Movies At Then Call It Using The fresh_tomatoes.py
movies = [Deadpool,
          Evile_Dead,
          What_Happened_To_Monday,
          The_Stangers,
          IT,
          The_Conjuring_2]
fresh_tomatoes.open_movies_page(movies)
