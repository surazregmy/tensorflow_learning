import math
from IPython  import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.options.display.float_format = '{:.1f}'.format
tf.reset_default_graph()

california_housing_dataset = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",",encoding="utf-8-sig")
california_housing_dataset = california_housing_dataset.reindex(np.random.permutation(california_housing_dataset.index))
california_housing_dataset /= 1000.0
# # print(california_housing_dataset)
# print(california_housing_dataset.describe())

#Building the model
#Define the feature room
my_feature = california_housing_dataset['total_rooms']
feature_columns = [tf.feature_column.numeric_column('total_rooms')]

#Define the target
targets = california_housing_dataset['median_house_value']

# my_features =  {key: np.array(value) for key, value in dict(my_feature).items()}

ds = Dataset.from_tensor_slices((my_feature,targets))

