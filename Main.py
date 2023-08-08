#!python3

import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime 

# test = pd.read_csv('./input/test.csv')
train = pd.read_csv('./input/train.csv')


# Checking if the column in numeric or not and then filling NaNs as Mean of the column
train_avg = train.apply(lambda col: col.fillna(col.mean()) if np.issubdtype(col.dtype, np.number) else col)


selc = ['SulphurDioxide_SO2_column_number_density',
'SulphurDioxide_cloud_fraction',
'Cloud_cloud_top_height',
'Cloud_cloud_base_pressure',
'Cloud_cloud_optical_depth',
'Ozone_solar_azimuth_angle',
'emission']


#train_avg['date'] = datetime.strptime(str(train_avg['year'])+str(train_avg['week_no'].astype(str).str.zfill(2))+'-0', '%Y%W-%w')
#train_avg['date'] = train_avg[].apply(lambda row: year_week(row.year, row.week), axis=1)
#train_avg['date'] = pd.to_datetime(train_avg['year'].astype(str) + train_avg['week_no'].astype(str).str.zfill(2) + '-0', format='%Y%U-%w')


rows = zip(train['year'], train['week_no'])  # Creating a zip object

def get_dt(year, week_no):
    date = datetime.strptime(f'{year}-{week_no}-1', "%Y-%W-%w")
    return date

dates = [get_dt(year, week) for year, week in rows]
train_avg['date'] = pd.to_datetime(dates)
print(train_avg['date'])
