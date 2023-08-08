#!python3

import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
import plotly.express as px

train = pd.read_csv('./input/train.csv')

null_c = train.isnull().sum()
null_cols = null_c[ null_c > len(train) * 0.5].index

# Checking if the column in numeric or not and then filling NaNs as Mean of the column
train_avg = train.apply(lambda col: col.fillna(col.mean()) if np.issubdtype(col.dtype, np.number) else col)

selc = ['SulphurDioxide_SO2_column_number_density',
'SulphurDioxide_cloud_fraction',
'Cloud_cloud_top_height',
'Cloud_cloud_base_pressure',
'Cloud_cloud_optical_depth',
'Ozone_solar_azimuth_angle',
'emission']


plt.figure(figsize = (8,6))
sns.heatmap(train_avg[selc].corr(), annot=True, cmap = 'coolwarm')
plt.show()

top_1k = train_avg.nlargest(1000, 'emission')
plt.figure(figsize=(10, 6))
plt.scatter(top_1k['longitude'], top_1k['latitude'], c=top_1k['emission'], cmap='viridis', s=50)
plt.colorbar(label='Emission')
plt.title('Geographical Distribution of top 1000 Emission')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


