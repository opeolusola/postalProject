import requests as rq
import pandas as pd, os


#create a function that takes in one parameter which is postcode and extract city from the result of API call
def  getCity(postcode):
    
    #get the dynamic endpoint into a variable: end_point
    end_point = f"https://api.postcodes.io/postcodes/{postcode}"
    #store the result of the API call into a variable
    data = rq.get(end_point)
    try:
        #extract city from JSON
        city = (data.json()['result']['admin_ward'])
    except:
        #perhaps if a city is not found, say "Not Found"
        city = "Not Found"

    return city




