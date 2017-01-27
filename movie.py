import webbrowser


# In this class, properties of a movie is being initialised
class Movie():
    def __init__(self, title, story_line, poster, trailor, year, rating):
        self.title = title
        self.storyline = story_line
        self.poster_image_url = poster
        self.trailer_youtube_url = trailor
        self.year = year
        self.rating = rating
