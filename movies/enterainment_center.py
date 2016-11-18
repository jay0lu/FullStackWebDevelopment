import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/toy-story-1995/large_agy8DheVu5zpQFbXfAdvYivF2FU.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

the_matrix = media.Movie("The Matrix",
                         "A programmer is brought back to reason and reality when learning he was living in a program created by gigantic machines which make human birth artificial. In order to set humanity free, Neo will have to face many enemies by using technologies and self-trust.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# print(the_matrix.storyline)
# the_matrix.show_trailer()

red = media.Movie("Red",
                  "When his peaceful life is threatened by a high-tech assassin, former black-ops agent Frank Moses reassembles his old team in a last ditch effort to survive and uncover his assailants.",
                  "https://upload.wikimedia.org/wikipedia/en/4/41/Red_ver7.jpg",
                  "https://www.youtube.com/watch?v=-JZ_moituIo")

jason_bourne = media.Movie("Jason Bourne",
                   "The CIA's most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.",
                   "https://upload.wikimedia.org/wikipedia/en/8/8b/Jason_Bourne_soundtrack_cover.jpg",
                   "https://www.youtube.com/watch?v=F4gJsKZvqE4")

print(red.poster_image_url)

movies = [toy_story, the_matrix, red, jason_bourne]
fresh_tomatoes.open_movies_page(movies)
