import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://movieposters2.com/images/721919-b.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avator = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://cdn.europosters.eu/image/750/posters/avatar-limited-ed-one-sheet-sun-i7182.jpg",
                    "https://www.youtube.com/watch?v=a0CDJZu4M5I")

mel_robbins = media.Movie("5 Second Rule",
                        "The Truth About Motivation and How to Be Productive!",
                        "https://pbs.twimg.com/profile_images/976909620970078208/sOQYZ46-_400x400.jpg",
                        "https://www.youtube.com/watch?v=i129CFqBIzg")

school_of_rock = media.Movie('School of Rock',
                            'Using rock music to learn',
                            "https://s3.amazonaws.com/kravis-media/wp-content/uploads/2018/01/30153730/SchoolofRockFeature.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

shawshank = media.Movie("The Shawshank Redemption",
                        "A banker sentenced to life in prison in 1947 for the murder of his wife and her lover",
                        "http://www.moviepostersusa.com/media/catalog/product/cache/1/image/600x600/9df78eab33525d08d6e5fb8d27136e95/p/1/p116_1.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

movies = [toy_story, avator, mel_robbins, school_of_rock, shawshank]
# fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.valid_rating)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
