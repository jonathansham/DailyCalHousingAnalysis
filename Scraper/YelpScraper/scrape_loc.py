# source activate python2

import sample as s 
import json
import csv
import pandas as pd 

""" Search Parameters
limit = 1
term = 'food'
location = 'berkeley'
offset = 0 #Offset the list of returned business results by this amount
category_filter = "null"
radius_filter = 0 #in meters
southwest_lat = 37.853727
southwest_long = -122.278823
northeast_lat = 37.884056
northeast_long = -122.251139
bound = str(southwest_lat) +','+ str(southwest_long) +'|'+ str(northeast_lat) +','+ str(northeast_long)
latitude = 37.853727
longitude = -122.278823
cll = str(latitude) + ',' + str(longitude)
"""


def loc(latitude, longitude):
	return str(latitude) + ',' + str(longitude)

# Pull data for every apartment
# term = None, limit = None, r = None, ll = None, location = None, bounds = None
# f = open("summary.csv")
# data = json.loads(f.read())['addrs']
# size = len(data)

# for i in range(size):
#     ll = loc(data[i][2], data[i][3])
#     request = s.search(term = 'food', limit = 20, ll = ll)
#     with open('restaurants.json', 'a') as fp:
#     	json.dump(request, fp)

df = pd.read_csv('summary.csv')
size = len(df)
for i in range(1178, 2262):
    ll = loc(df['latitude'][i], df['longitude'][i])
    request = s.search(term = 'food', limit = 20, ll = ll)
    with open('yelp.json', 'a') as fp:
        json.dump(request, fp)


