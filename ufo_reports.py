import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo)

print(type(ufo['City']))
print(type(ufo.City))

print(ufo.City + ' ' + ufo.State)
