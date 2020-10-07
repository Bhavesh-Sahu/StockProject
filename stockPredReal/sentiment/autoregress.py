import numpy as np 
import pandas as pd
import csv 


file = open('../csv/INFY.BO.csv')
reader = csv.reader(file)
# next(reader) ​
dates = []
values=[]
for​ row ​ in​ reader:
    values.append(float(row[​6​])) ​ # Column 1 has closing price
    dates.append(datetime.strptime(row[​0], ​ "%Y-%m-%d"​ )) ​ # Column 0 has dates

model = AR(values, dates=dates, freq=​ 'D'​)
predictions = model.fit().predict()
# Trim leading values used for first prediction
actual_values = values[len(values) - len(predictions):]
dates = dates[len(dates) - len(predictions):]
# Calculate Root mean squared error
print(​ "Root mean squared error:"​ , sqrt(mean_squared_error(actual_values, predictions)))