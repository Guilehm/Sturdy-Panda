import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo)

print(type(ufo['City']))
print(type(ufo.City))

# creating new column
ufo['Location'] = (ufo.City + ', ' + ufo.State)
print(ufo.Location)

# renaming columns
print(ufo.columns)
ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
print(ufo.columns)

# overwrite columns
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time', 'location']
ufo.columns = ufo_cols
print(ufo.columns)

# overwrite columns while reading file
ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols)

# replace spaces to underscores in header
ufo.columns = ufo.columns.str.replace(' ', '_')
print(ufo.columns)
