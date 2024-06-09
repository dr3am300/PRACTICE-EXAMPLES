# EXAMPLE 2: To ensure viewers have an age-appropriate experience, movies come with specific ratings. Given a movie's rating (G, PG, PG-13, R) and the age of the person, inform the user if they can watch the movie based on their age.

movie_rating = input("Enter the movie rating (G, PG, PG-13, R): ")
age = int(input("Enter your age: "))
if movie_rating := "G": 
    print("You can watch the movie")
elif movie_rating == "PG" and age >= 10:
    print("You can watch the movie")
elif movie_rating == "PG-13" and age >= 13:
    print("You can watch the movie")
elif movie_rating == "R" and age >= 17:
    print("You can watch the movie")
else:
    print("You are not allowed to watch the movie")
    