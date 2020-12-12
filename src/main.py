import pandas as pd
import plotter as pltr


raw_data = pd.read_csv('./data/Mobile banking app - collected data.csv')

COL_NAME_GENDER = 'Gender'
COL_NAME_AGE = 'Age'
DISTANCE_H = 'Distance to bank from home'
FREQ = 'Frequency of usage'

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


by_freq_1 = data.groupby(FREQ).sum().reset_index()


gr_by_gender = raw_data.groupby(COL_NAME_GENDER).count().reset_index()

labels = gr_by_gender[COL_NAME_GENDER]
sizes = gr_by_gender[COL_NAME_AGE]
pltr.plot_py_chart(sizes, labels, 'By gender')

raw_data.head()
