import pandas as pd
import os


def milking(request_json):
    try:
        #df = pd.read_csv(r"C:\Users\satishkumar.s\Desktop\Milkrare\factory\Haptikdata.csv",encoding='latin-1')
        #df = pd.read_csv('Haptik_API-main/Milkrare/factory/Haptikdata.csv')
        url = "https://raw.githubusercontent.com/wazsee/Haptik_API/main/Milkrare/factory/Haptikdata.csv"
        df = pd.read_csv(url)

        #df = pd.read_csv('Milkrare/factory/Haptikdata.csv')
        #df = pd.read_csv('https://github.com/wazsee/Haptik_API/blob/8ae1f0c3d8313c965d3de47b6b71f5bae53a0988/Milkrare/factory/Haptikdata.csv')
        print("df")
        

        #request_json['Milk1_Dry2'] = 1 if request_json['Milk1_Dry2'] == "milk" else 2

        response_values = df.loc[
            (df['Phone_Number']==request_json['Phone_Number'])
            ]
        print(df.head())

        
        response = {}
        #response['Farmer Name'] = response_values['Farmer Name'].values[0]
        response['Region Name'] = response_values['Region Name'].values[0]
        response['District Name'] = response_values['District Name'].values[0]
        response['Pin Code'] = response_values['Pin Code'].values[0] 
        #response['Plant Name'] = response_values['Plant Name'].values[0]
        response['Plant Code'] =int(response_values['Plant Code'].values[0])
        response['MCC Name'] = response_values['MCC Name'].values[0]
        response['MCC Code'] = int(response_values['MCC Code'].values[0])
        
        

        return response
    except Exception as e:
        return str(e)
    
