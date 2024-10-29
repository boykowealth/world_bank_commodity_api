import pandas as pd

class WOLRD_BANK_COMMODITY():

    def data():
        url = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"

        headers = [
            "Date_Old", "Crude oil, average", "Crude oil, Brent", "Crude oil, Dubai", "Crude oil, WTI", "Coal, Australian", 
            "Coal, South African **", "Natural gas, US", "Natural gas, Europe", "Liquefied natural gas, Japan", 
            "Natural gas index", "Cocoa", "Coffee, Arabica", "Coffee, Robusta", "Tea, avg 3 auctions", 
            "Tea, Colombo", "Tea, Kolkata", "Tea, Mombasa", "Coconut oil", "Groundnuts", "Fish meal", 
            "Groundnut oil **", "Palm oil", "Palm kernel oil", "Soybeans", "Soybean oil", "Soybean meal", 
            "Rapeseed oil", "Sunflower oil", "Barley", "Maize", "Sorghum", "Rice, Thai 5%", "Rice, Thai 25%", 
            "Rice, Thai A.1", "Rice, Viet Namese 5%", "Wheat, US SRW", "Wheat, US HRW", "Banana, Europe", 
            "Banana, US", "Orange", "Beef **", "Chicken **", "Lamb **", "Shrimps, Mexican", "Sugar, EU", 
            "Sugar, US", "Sugar, world", "Tobacco, US import u.v.", "Logs, Cameroon", "Logs, Malaysian", 
            "Sawnwood, Cameroon", "Sawnwood, Malaysian", "Plywood", "Cotton, A Index", "Rubber, TSR20 **", 
            "Rubber, RSS3", "Phosphate rock", "DAP", "TSP", "Urea", "Potassium chloride **", "Aluminum", 
            "Iron ore, cfr spot", "Copper", "Lead", "Tin", "Nickel", "Zinc", "Gold", "Platinum", "Silver"
        ]

        #---FIX HEADERS---#
        headers = [header.replace("**", "").upper() for header in headers] # Convert headers to uppercase and remove any '**'
        headers = [header.replace(", ", "_").upper() for header in headers] # Replace Commas With Underscores
        headers = [header.replace(" ", "_").upper() for header in headers] # Replace Spaces With Underscores

        #---OPEN FILE AND CLEAN---#
        data = pd.read_excel(url, sheet_name='Monthly Prices', skiprows=6, header=None)
        data = data.replace("…", 0)
        data.columns = headers
        data['DATE'] = pd.to_datetime(data['DATE_OLD'], format='%YM%m') # Normalize Dates
        data = data.drop(columns=['DATE_OLD'])

        return data
