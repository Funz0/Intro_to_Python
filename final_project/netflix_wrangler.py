import pandas as pd

# read in data
data = pd.read_csv('data/netflix_titles.csv')

# inspect dataframe size and columns within
data.head()
data.columns

# replace missing values for cast, country and director w/ 'Unknown'
data['cast'].fillna('Unknown', inplace=True)
data['country'].fillna('Unknown', inplace=True)
data['director'].fillna('Unknown', inplace=True)
# drop any missing values in the selected columns
data.dropna(subset=['date_added','rating','duration'], inplace=True)
# assert no duplicates are in the dataframe
data.drop_duplicates(inplace=True)

# convert date added to datetime
data['date_added'] = pd.to_datetime(data['date_added'])

# ensure data is free of null values
print(data.isnull().sum())
# check out column info
print(data.info())

# export clean dataset inside 'data' folder
data.to_csv('data/netflix_clean.csv', index=False)
