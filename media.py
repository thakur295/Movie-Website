import movie
import fresh_tomatoes
import urllib  # for using urlopen function
import ast     # for converting string into a dictionary


''' this function takes movie's Id as an argument and
    returns it's details in dictionary formate '''


def getMovieDetail(id):
    connection = urllib.urlopen("http://www.omdbapi.com/?i=" + id +
                                "&plot=short&r=json")  # opening url
    output = connection.read()        # reading url
    value = ast.literal_eval(output)  # converting string into dictionary
    connection.close()                # closing url connection
    return value


# sending Ids of films to the funtion which return it's details
value = getMovieDetail("tt2338151")
pk = movie.Movie(value.get('Title'), value.get('Plot'), value.get('Poster'),
                 "https://www.youtube.com/watch?v=SOXWc32k4zA",
                 value.get('Year'), value.get('imdbRating'))

value = getMovieDetail("tt0871510")
chakDeIndia = movie.Movie(value.get('Title'), value.get('Plot'),
                          value.get('Poster'),
                          "https://www.youtube.com/watch?v=6a0-dSMWm5g",
                          value.get('Year'), value.get('imdbRating'))

value = getMovieDetail("tt3863552")
bajrangiBhaijaan = movie.Movie(value.get('Title'), value.get('Plot'),
                               value.get('Poster'),
                               "https://www.youtube.com/watch?v=4nwAra0mz_Q",
                               value.get('Year'), value.get('imdbRating'))

value = getMovieDetail("tt2631186")
baahubali = movie.Movie(value.get('Title'), value.get('Plot'),
                        value.get('Poster'),
                        "https://www.youtube.com/watch?v=VdafjyFK3ko",
                        value.get('Year'), value.get('imdbRating'))

value = getMovieDetail("tt4169250")
msd = movie.Movie(value.get('Title'), value.get('Plot'), value.get('Poster'),
                  "https://www.youtube.com/watch?v=6L6XqWoS8tw",
                  value.get('Year'), value.get('imdbRating'))

value = getMovieDetail("tt5713232")
madari = movie.Movie(value.get('Title'), value.get('Plot'),
                     value.get('Poster'),
                     "https://www.youtube.com/watch?v=j4s3JmLGLCA",
                     value.get('Year'), value.get('imdbRating'))

# creating list of movies
movies = [pk, chakDeIndia, bajrangiBhaijaan, baahubali, msd, madari]

# opening movie page
fresh_tomatoes.open_movies_page(movies)
