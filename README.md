# Movie Manager System (AlmaEconomics assessment)

For this assessment, I have developed a script using argparse to accept arguments to return all movies based on genre, overwrite the score for the chosen movie, and display the necessary information to achieve the project requirements. Although, this project involves a large dataset and the use of pandas entirely would be the optimal approach, instead I have used list comprehension and algorithms approach. This decision was driven by the project's specific requirements, favouring a lightweight and straightforward solution. 

## Installation

To run this application, you'll need to set-up a virtual enviroment and install the following libaries, Pandas and Matplotlib. 

## How to use

```python
# This will display all movies based on the specified genre - In this case Horror
python MovieManagerSystem.py -g Horror 

# This will overwrite the score for the specified movie (Movie title is case-sensitive so copy exact from data structure)
python MovieManagerSystem.py -u Toy Story (1995) 9 

# Running the script without options will return total number of movies, average score of all movies, top N movie with highest score, all unique genres, visually represent score distribution
python MovieManagerSystem.py  
```
