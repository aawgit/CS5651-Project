import pandas as pd


raw_data = pd.read_csv('./data/Mobile banking app - collected data.csv')

COL_NAME_GENDER = 'Gender'
COL_NAME_AGE = 'Age'
DISTANCE_H = 'Distance to bank from home'
INCOME = 'Monthly income'
FREQ = 'Frequency of usage'
SECUTIRY = 'Rating in terms of security (electronic)'

columns = ['Timestamp', 'Gender', 'Age', 'Location', 'Education',
       'Employment status', 'Monthly income', 'Married or not',
       'Type of banking account', 'Starting year ', 'Types of services',
       'Frequency of usage', 'Way of withdrawing money', 'Amount withdrawn',
       'Distance to bank from home', 'Distance to bank from work place',
       'Rating in terms of cost',
       'Rating in terms of time saving',
       'Rating in terms of time of use',
       'Rating in terms of physical security',
       'Rating in terms of security (electronic)']

one_hot_distance_h = pd.get_dummies(raw_data[DISTANCE_H], prefix='Distance ')
one_hot_gender = pd.get_dummies(raw_data[COL_NAME_GENDER], prefix='Gender ')
one_hot_freq = pd.get_dummies(raw_data[FREQ])

data = pd.concat([raw_data, one_hot_freq], axis = 1)

gr_by_gender = data.groupby(COL_NAME_GENDER).sum().reset_index()
gr_by_income = data.groupby(INCOME).sum().reset_index()
gr_by_sec_rating = data.groupby(SECUTIRY).sum().reset_index()

gr_by_sec_rating.to_csv('./by_security.csv')
