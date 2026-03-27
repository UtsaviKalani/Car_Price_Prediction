import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.DataFrame({
    'year': [2015,2016,2017,2018,2019,2020,2014,2013,2021,2022],
    'km_driven': [50000,40000,30000,20000,15000,10000,60000,70000,8000,5000],
    'fuel_type': [0,0,0,1,1,1,0,0,1,1],
    'price': [5,6,7,8,9,10,4,3,11,12]
})

X = data[['year','km_driven','fuel_type']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved successfully!")
