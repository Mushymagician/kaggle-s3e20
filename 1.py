#!python3

import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# test = pd.read_csv('./input/test.csv')
train = pd.read_csv('./input/train.csv')

null_c = train.isnull().sum()

null_cols = null_c[ null_c > len(train) * 0.5].index

#correlation with columns that have null values
correlation_emission = train[null_cols].apply(lambda col : col.corr(train['emission']))
#reindexing the correlation
correlation_emission =  correlation_emission.reindex(correlation_emission.abs().sort_values(ascending = False).index)

# Checking if the column in numeric or not and then filling NaNs as Mean of the column

train_avg = train.apply(lambda col: col.fillna(col.mean()) if np.issubdtype(col.dtype, np.number) else col)

# Checking if there is any null vlaues
n_null_c = train_avg.isnull().sum()
print(n_null_c[n_null_c > 1])


selc = ['SulphurDioxide_SO2_column_number_density',
'SulphurDioxide_cloud_fraction',
'Cloud_cloud_top_height',
'Cloud_cloud_base_pressure',
'Cloud_cloud_optical_depth',
'Ozone_solar_azimuth_angle',
'emission']

corr_matrix = train_avg[selc].corr()

plt.figure(figsize = (8,6))
sns.heatmap(corr_matrix, annot=True, cmap = 'coolwarm')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(train_avg['longitude'], train_avg['latitude'], c=train_avg['emission'], cmap='viridis', s=5)
plt.colorbar(label='Emission')
plt.title('Geographical Distribution of Emission')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()