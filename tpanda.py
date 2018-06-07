import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# country = pd.Series(['Nepal', 'US', 'India'])
# print(country)
# population = pd.Series(['1m','300m','1B'])
# print(population)
# table = pd.DataFrame({'Country Name':country,'Population':population})
# # print(table)
# #
# # california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
# # california_housing_dataframe.describe()
# # # print(california_housing_dataframe)
# # # print(california_housing_dataframe.describe())
# # # print(california_housing_dataframe.head())
# # california_housing_dataframe.hist('housing_median_age')
# # plt.show()
#
# print(table['Country Name'])
# print(table['Country Name'][1])

#Exercises
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
city_details = pd.DataFrame({ 'City name': city_names, 'Population': population })
city_details['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
city_details['Population density'] = city_details['Population'] / city_details['Area square miles']

city_details['Is wide and has saint name'] = (city_details['Area square miles'] > 50) & city_details['City name'].apply(lambda name: name.startswith('San'))
print(city_details)

print(city_details.index)
