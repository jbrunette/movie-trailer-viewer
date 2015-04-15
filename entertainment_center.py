# Import required modules
import media
import fresh_tomatoes

# The Matrix
the_matrix = media.Movie("The Matrix",
                        "In a world of 1s and 0s...are you a zero, or The One?",
                        "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# The Lego Movie
the_lego_movie = media.Movie("The Lego Movie",
                     "The story of a nobody who saved everybody",
                     "http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
                     "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

# Ghostbusters
ghostbusters = media.Movie("Ghostbusters",
                             "We're ready to believe you.",
                             "http://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png",
                             "https://www.youtube.com/watch?v=vntAEVjPBzQ")

# Back to the Future
back_to_the_future = media.Movie("Back to the Future",
                          "Marty McFly's having the time of his life. The only question is -- what time is it?",
                          "http://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                          "https://www.youtube.com/watch?v=yosuvf7Unmg")

# The Fifth Element
the_fifth_element = media.Movie("The Fifth Element",
                                "It Mu5t Be Found.",
                                "http://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                                "https://www.youtube.com/watch?v=VkX7dHjL-aY")

# Big Trouble in Little China
big_trouble_in_little_china = media.Movie("Big Trouble in Little China",
                           "It's all in the reflexes!",
                           "http://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=592EiTD2Hgo")

# Load movies into array
movies = [the_matrix, the_lego_movie, ghostbusters, back_to_the_future, the_fifth_element, big_trouble_in_little_china]

# Build and open movies page
fresh_tomatoes.open_movies_page(movies)
