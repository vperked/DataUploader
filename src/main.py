import pandas as pd
import mysql.connector
import json
def readConfig():
     with open("config.json", "r") as file: ## Open config.json
        config_data = json.load(file) ## Load it
        return config_data
def connectToMySQL(host, user, password): ### Host and other information is passed through the function to connect.
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")  # Else responds with the error and returns nothing
        return None
def mergeData():
    firstSet = {'Name': [input("Insert a name:")],
            'Age' : [input("Insert a age:")] }
    secondSet = {'Game': [input("Insert a game:")],
             'Show': ['StrangerThings']} # Establishing the data
    df1 = pd.DataFrame(firstSet) 
    df2 = pd.DataFrame(secondSet)
    mergedData = pd.merge(df1, df2) # Merge both data frames 
    return mergedData # and finally we return the merged data.
def insertData(db):
    db.cursor()
    sql = "INSERT INTO test (Name, Age, Game, Show) VALUES (%s, %s, %s, %s)"
    data = mergeData
    
config = readConfig()
db_connection = connectToMySQL(config["host"], config["user"], config["password"])
if db_connection:
    print("Connected, running function.")
    mergeData()
