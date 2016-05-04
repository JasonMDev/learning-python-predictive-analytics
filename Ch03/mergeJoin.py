# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:41:51 2016

@author: jasonm_dev
"""


import pandas as pd

filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets/medals'
filename= 'Medals.csv'
file = filepath+'/'+filename

# IMPORT MAIN MEDAL FILE
data_main=pd.read_csv(file,encoding='latin_1')
data_main.head()
data_main.shape # Out: (8618, 8)
# ERROR 
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf8 
# in position 8: invalid start byte
# SOLUTION: used latin_1, ascii and utf-8 don't work


# Check to see how many unique athletes there are.
a=data_main['Athlete'].unique().tolist()
len(a) # Out: 6956

# IMPORT COUNTRY MAP
filename_country = 'Athelete_Country_Map.csv'
file_country = filepath+'/'+filename_country
country_map=pd.read_csv(file_country,encoding='latin_1')
country_map.head()
country_map.shape # Out: (6970, 2) with 6956 uniques.

# Uniques adding to total with 2 nationalities.
country_map[country_map['Athlete']=='Aleksandar Ciric']

# IMPORT SPORTS MAP
filename_sports = 'Athelete_Sports_Map.csv'
file_sports = filepath+'/'+filename_sports
sports_map=pd.read_csv(file_sports,encoding='latin_1')
sports_map.head()
sports_map.shape # Out: (6975, 2) 

# with very few doing more than one sport.
sports_map[(sports_map['Athlete']=='Chen Jing') | (sports_map['Athlete']=='Richard Thompson') | (sports_map['Athlete']=='Matt Ryan')]

# MERGE IMPORTED COUTRY MAP DATA FRAME FILES
merged=pd.merge(left=data_main,right=country_map,left_on='Athlete',right_on='Athlete')
merged.head()
merged.shape # Out: (8657, 9) > 8618 uniques because of inner join.

# See duplicated results. 
merged[merged['Athlete']=='Aleksandar Ciric']

# Drop duplicates from country_map data frame
country_map_dp=country_map.drop_duplicates(subset='Athlete') # Out: (6956, 2)

# Now retry merge as length is now the same as unique atheletes.
merged_dp=pd.merge(left=data_main,right=country_map_dp,left_on='Athlete',right_on='Athlete')
merged_dp.shape # Out: (8618, 9)

# MERGE IMPORTED SPORTS MAP DATA FRAME FILES
# Drop duplicates from country_map data frame
sports_map_dp=sports_map.drop_duplicates(subset='Athlete')
sports_map_dp.shape # Out: (6956, 2)

# Merge into final data.
merged_final=pd.merge(left=merged_dp,right=sports_map_dp,left_on='Athlete',right_on='Athlete')
merged_final.shape # Out: (8618, 10)
merged_final.head()


# MERGE TYPES
# PYTHON 2.7 uses '<>', whereas python3.5 uses '!='
# Prepare the data with some mismathes to show join examples.
country_map_dlt=country_map_dp[(country_map_dp['Athlete']!='Michael Phelps') & (country_map_dp['Athlete']!='Natalie Coughlin') & (country_map_dp['Athlete']!='Chen Jing')
                    & (country_map_dp['Athlete']!='Richard Thompson') & (country_map_dp['Athlete']!='Matt Ryan')]
len(country_map_dlt) # Out: 6951
sports_map_dlt=sports_map_dp[(sports_map_dp['Athlete']!='Michael Phelps') & (sports_map_dp['Athlete']!='Natalie Coughlin') & (sports_map_dp['Athlete']!='Chen Jing')
                    & (sports_map_dp['Athlete']!='Richard Thompson') & (sports_map_dp['Athlete']!='Matt Ryan')]
len(sports_map_dlt) # Out: 6951

data_main_dlt=data_main[(data_main['Athlete']!='Michael Phelps') & (data_main['Athlete']!='Natalie Coughlin') & (data_main['Athlete']!='Chen Jing')
                    & (data_main['Athlete']!='Richard Thompson') & (data_main['Athlete']!='Matt Ryan')]
len(data_main_dlt) # Out: 8605

# INNER JOIN EXAMPLE
merged_inner=pd.merge(left=data_main,right=country_map_dlt,how='inner',left_on='Athlete',right_on='Athlete')
len(merged_inner) # Out: 8605

# LEFT JOIN EXAMPLE
merged_left=pd.merge(left=data_main,right=country_map_dlt,how='left',left_on='Athlete',right_on='Athlete')
len(merged_left) # Out: 8618
# Check the athletes which don't have information because of the left join.
merged_left_slt=merged_left[merged_left['Athlete']=='Michael Phelps']
merged_left_slt

# RIGHT JOIN EXAMPLE
merged_right=pd.merge(left=data_main_dlt,right=country_map_dp,how='right',left_on='Athlete',right_on='Athlete')
len(merged_right) # Out: 8610
