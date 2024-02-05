import csv 
import pandas as pd
import math
import argparse
import matplotlib.pyplot as plt

#argparse for task 3.1 and 4.1 
def parse_arg():
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-g', '--genre', type=str, help='Specify genre to display movies in that genre')
    argParser.add_argument('-u', '--update', nargs='+', help='To update the score of your chosen movie')
    # argParser.add_argument('score', type = float, help='Enter the score to update')
    args = argParser.parse_args()
    return args.genre, args.update 

#task 1
def load_csv(filename):
    list_of_movies = []
    with open(filename, encoding='ANSI') as movieData:
        read_movieData = csv.DictReader(movieData, delimiter=',')
        for i in read_movieData:
            list_of_movies.append(i)
    return list_of_movies

#task 2.1
def avg_score(movieList):
    total = 0.0
    count = 0
    for row in movieList:
        score_str = row['IMDB Score']
        if score_str:
            score_float = float(score_str)
            total += score_float
            count += 1
    score = total / count
    return score

#task 2.2
def high_score(movies):
    score = []
    value_max = float(-math.inf)
    for row in movies:
        score_str = row['IMDB Score']
        if score_str:
            score_float = float(score_str)
            if score_float > value_max:
                value_max = score_float
                score = [row]
            elif score_float == value_max:
                score.append(row)
    return score

#task 3.1
def filter_on_genre(genre, filename):
    genreFilter = []
    for row in filename:
        if genre in row['Genre']:
            genreFilter.append(row)
    return genreFilter

#task 3.2
def unique_genre(filename):
    argUnique = set()
    for row in filename:
        genres = row['Genre'].split('|')
        argUnique.update(genres)
    
    uniqueList = list(argUnique)
    uniqueList.sort()
    return uniqueList

#task 4.1
def update_score(filename, movieChoice, score):
    for row in filename:
        if row['Title'] == movieChoice:
            row['IMDB Score'] = str(score)

    #Writing back to the same data structure
    with open('movies.csv', 'w', encoding='ANSI', newline='') as movie_data:
        fieldnames = ['imdbId', 'Imdb Link', 'Title', 'IMDB Score', 'Genre', 'Poster']
        writer = csv.DictWriter(movie_data, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filename)

# task 5
def chart(filename):

    df = pd.DataFrame(filename)
    plt.rcParams["figure.autolayout"] = True
    plt.figure(figsize=(15, 6))

    ratings = df['IMDB Score'].value_counts().sort_index()
    #numbers gets a list of all the scores - needs to be string because the ratings are in float
    numbers = [str(score) for score in ratings.index]

    #keys = x, data = y
    plt.bar(numbers, ratings)
    plt.xticks(rotation=45, ha='right')
    
    plt.xlabel('Score')
    plt.ylabel('Number of ratings')
    plt.title('Distribution of movie scores')
    plt.show()

if __name__ == '__main__':
    genre, update = parse_arg()
    movie = 'movies.csv'
    movieFile = load_csv("movies.csv")  

    if genre: #task 3.1 - Display movies based on specified genre
        genrePick = genre
        if genrePick:
            filteredMovies = filter_on_genre(genrePick, movieFile)
            for row in filteredMovies:
                print(f"{row['Title']} - Genre: {row['Genre']}")
            print(" -----------------------------------------------------------")
            print(f"Movies where '{genrePick}' is the unique genre: \n")
            for row in filteredMovies:
                if row['Genre'] == genrePick:
                    print(f"{row['Title']} - Genre: {row['Genre']}")  
    elif update: #task 4.1 - overwrite the score of specific movie
        movieUpdate = ' '.join(update[:-1])
        score = float(update[-1])
        update_score(movieFile, movieUpdate, score)
        print(f"Updated score for {movieUpdate} is {score}")    

    else:
        total_movies = len(movieFile) #task 1 - Display the total number of movies
        averageScore = avg_score(movieFile) #task 2.1 - Display the average score of all movies
        highestScore = high_score(movieFile) 
        ListUnique = unique_genre(movieFile)
        print(f'The total number of movies is: {total_movies}')
        print(f'The movie average score is: {'%.2f' % averageScore}')
        print('\n')
        print('The highest scoring movies are: ')
        for row in highestScore: #task 2.2 - Display top N movies with highest score
            print(f"{row['Title']} - IMDB Score: {row['IMDB Score']}")
        print('\n')
        print('Here are the unique Genres: ')
        for genre in ListUnique: #task 3.2 - Display all unique genres in the movie data
            print(genre)
        chart(movieFile) #task 5 - Visually represent movie score distribution
        
        




