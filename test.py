import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
from pandas import read_csv
url='Downloads/diabetes_dataset.csv'
data=read_csv(url)
scatter_matrix(data[['Pregnancies','Glucose']])
plt.show()