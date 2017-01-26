import movie
import fresh_tomatoes
import urllib
import ast

connection = urllib.urlopen("http://www.omdbapi.com/?t=pk&y=2014&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
pk = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=SOXWc32k4zA",value.get('Year'),value.get('imdbRating'))
connection.close()

connection = urllib.urlopen("http://www.omdbapi.com/?t=airlift&y=2016&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
AirLift = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=vb5xCMbMfZ0",value.get('Year'),value.get('imdbRating'))
connection.close()

connection = urllib.urlopen("http://www.omdbapi.com/?t=bajrangi&y=2015&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
BajrangiBhaijaan = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=4nwAra0mz_Q",value.get('Year'),value.get('imdbRating'))                 
connection.close()

connection = urllib.urlopen("http://www.omdbapi.com/?t=baahubali&y=2015&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
Baahubali = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=VdafjyFK3ko",value.get('Year'),value.get('imdbRating'))
connection.close()

connection = urllib.urlopen("http://www.omdbapi.com/?i=tt4169250&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
msd = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=6L6XqWoS8tw",value.get('Year'),value.get('imdbRating'))
connection.close()

connection = urllib.urlopen("http://www.omdbapi.com/?i=tt5713232&plot=short&r=json")
output = connection.read()
value = ast.literal_eval(output)
madari = movie.Movie(value.get('Title'),value.get('Plot'),value.get('Poster'),"https://www.youtube.com/watch?v=j4s3JmLGLCA",value.get('Year'),value.get('imdbRating'))
connection.close()                 

movies = [pk,AirLift,BajrangiBhaijaan,Baahubali,msd,madari]
fresh_tomatoes.open_movies_page(movies)

