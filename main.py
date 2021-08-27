import os, pandas as pd
from definedFunctions import getCity

if __name__ == "__main__":
    #reading the raw data and save to a dataframe
    df = pd.read_csv('Postcodes.csv')
    #create an empty list called cities which will be populated
    cities =[]
    # Loop through each row to get postcode and pass the postcode into getCity function to extract the city.
    for index , row in df.iterrows():
        pst_cd= row[0]
        city = getCity(pst_cd)
        #populate list: cities
        cities.append(city)

    #create a new column called City in the dataframe with the values: cities
    df["City"]=cities

    #save the new dataframe to a csv called uk_cities
    df.to_csv("uk_cities.csv", index=False)