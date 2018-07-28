import pandas as pd

# using another separator, and names, without header
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
orders = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)
print(orders)
print(orders.head())
