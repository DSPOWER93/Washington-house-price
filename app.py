
# Importing the Libraries
from flask import Flask, redirect, url_for, render_template, request, session
# from flask_wtf import CsrfProtect
import numpy as np
import pandas as pd
import geocoder
import joblib
from math import acos,cos,radians,sin


# Loading the Trained Model
filename = 'Xgboost.sav'
#load saved modeyl
xgb_model = joblib.load(filename)

############ Distance from Evergreen Bridge.
def distance_evergreen_bridge(lat,long):
  D7 =  47.640295 # LAT OF EVERGREEN BRIDGE.
  E7 = -122.258628 # LONG OF EVERGREEN BRIDGE.
  D8 = lat
  E8 = long
  distance = 6371*acos(cos(radians(90-D7))*cos(radians(90-D8))+sin(radians(90-D7))*sin(radians(90-D8))*cos(radians(E7-E8)))
  return distance


#  Finding Co-ordinates using Zipcode.
zip_code = pd.read_csv("https://raw.githubusercontent.com/DSPOWER93/Data/main/us-zip-code-latitude-and-longitude.csv", sep = ';')
#  function to fnd geo-point
def find_geopoint(zipcode):
  find_point = zip_code[zip_code['Zip'] == zipcode]
  lat = find_point['Latitude']
  lng = find_point['Longitude']
  return float(lat),float(lng)


# The below command creates WSGI application Web Services Gateway interface.
app = Flask(__name__)


#  Landing Webpage.
@app.route(rule='/') # route basically says the webpage you want user to land to.
def welcome():
    return render_template('index.html') # we are directly routing audience to the HTML page.


# Landing Page
@app.route(rule='/success/<int:score>/<float:lat>/<float:long>') # route basically says the webpage you want user to land to
def success(score, lat, long):
    return render_template('results.html', result=score, lat=lat, lng= long)

#### Page showing the results for HTML.
@app.route(rule='/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        sqft_lot = float(request.form['sqft_lot'])
        Area_living = float(request.form['Area_living'])
        sqft_basement = float(request.form['sqft_basement'])
        sqft_above = Area_living - sqft_basement
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        floors = int(request.form['floors'])
        View_side = float(request.form['View_side'])
        condition = float(request.form['condition'])
        try:
            water = float(request.form.get('check'))
        except TypeError:
            water = 0
        year = 2020 - int(request.form['year'])
        renovation_year = 2020 - int(request.form['year'])
        street_address = str(request.form['street_address'])
        inputCity = str(request.form['inputCity'])
        zipcode = int(request.form['zipcode'])
        complete_address = street_address + ' , ' + inputCity + ' , WA ' + str(zipcode)
        coordinates = geocoder.osm(complete_address)
        if(coordinates.lat == None):
            lat, long = find_geopoint(zipcode)
        else:
            lat, long = coordinates.lat, coordinates.lng
        City_Mercer_Island = int(np.where(inputCity == 'Mercer Island', 1, 0))
        City_Clyde_Hill = int(np.where(inputCity == 'Clyde Hill', 1, 0))
        City_Yarrow_Point = int(np.where(inputCity == 'Yarrow Point', 1, 0))
        City_Medina = int(np.where(inputCity == 'Medina', 1, 0))
        City_Seattle = int(np.where(inputCity == 'Seattle', 1, 0))
        City_Algona = int(np.where(inputCity == 'Algona', 1, 0))
        City_Skykomish = int(np.where(inputCity == 'Skykomish', 1, 0))
        City_SeaTac = int(np.where(inputCity == 'SeaTac', 1, 0))
        City_Pacific = int(np.where(inputCity == 'Pacific', 1, 0))
        distance_evergreen_bridge_ = distance_evergreen_bridge(lat,long)
        final_entry = pd.DataFrame({
            'bedrooms': [bedrooms], 'bathrooms': [bathrooms], 'sqft_living': [Area_living],'sqft_lot': [sqft_lot],
            'floors': [floors], 'waterfront': [water], 'view': [View_side], 'condition': [condition],
            'sqft_above': [sqft_above], 'sqft_basement': [sqft_basement],'City_Mercer_Island': [City_Mercer_Island],
            'City_Clyde_Hill': [City_Clyde_Hill],'City_Yarrow_Point': [City_Yarrow_Point], 'City_Medina': [City_Medina],
             'City_Seattle': [City_Seattle] , 'City_Algona': [City_Algona], 'City_Skykomish': [City_Skykomish],
             'City_SeaTac':[City_SeaTac], 'City_Pacific': [City_Pacific],'Lat_': [lat], 'long_': [long],
             'distance_evergreen_bridge': [distance_evergreen_bridge_], 'below_renton_airport': [0], 'house_age': [year],
            'renovation_age':[renovation_year]
        })

        predicted_price = float(xgb_model.predict(final_entry))
        predicted_price = int(round(np.exp(predicted_price),0))

    res = ""
    return redirect(url_for('success', score=round(predicted_price/1000, 0), lat=lat, long=long*-1))


if __name__ == '__main__':
    app.run(debug=True)  # the advantage of applying Degbug = True is that weblink auto refreshs with changes made in app.


