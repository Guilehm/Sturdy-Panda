import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo)

print(type(ufo['City']))
print(type(ufo.City))

# creating new column
ufo['Location'] = (ufo.City + ', ' + ufo.State)
print(ufo.Location)

print(ufo.columns)
ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
print(ufo.columns)
