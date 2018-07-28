import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
print(movies.describe())
print(movies.dtypes)
print(movies.describe(include=['object']))
