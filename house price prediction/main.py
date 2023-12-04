# import pandas as pd
# from flask import Flask, render_template,request
# import pickle

# # Read the CSV file into a DataFrame
# data = pd.read_csv('house price prediction\Cleaned_Data.csv')
# pipe = pickle.load(open("house price prediction\RidgeModel.pkl",'rb'))


# app = Flask(__name__)

# @app.route('/')
# def home():
#     # Use the correct variable name (data) and sort the unique values
#     locations = sorted(data['location'].unique())
#     return render_template('index.html', locations=locations)

# @app.route('/predict',methods=['POST'])
# def predict():
#     locations = request.form.get('locations')
#     bhk = request.form.get('bhk')
#     bath = request.form.get('bath')
#     sqft = request.form.get('sqft')

#     print(locations,bhk,bath,sqft)
#     input = pd.DataFrame([[locations,bhk,bath,sqft]],columns=['locations','total_sqft','bath','bhk'])
#     prediction = pipe.predict(input)[0]



#     return str(prediction)

# if __name__ == '__main__':
#     app.run(debug=True)

import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np


# Read the CSV file into a DataFrame
data = pd.read_csv('house price prediction\Cleaned_Data.csv')
pipe = pickle.load(open("house price prediction\RidgeModel.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    # Use the correct variable name (data) and sort the unique values
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location, bhk, bath, sqft)
    # Ensure the order of columns in the DataFrame matches the order of values
    input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input_data)[0] * 1e5

    return str(np.round(prediction,2))

if __name__ == '__main__':
    app.run(debug=True)

