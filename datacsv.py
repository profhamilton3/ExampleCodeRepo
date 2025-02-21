""" datacsv.py
    upload a sample csv files sourced from w3schools.org 
"""
import pandas as pd

class DataCsv:
    def _init__(self):
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }
        self.df = pd.DataFrame(data)
        self.datacsv = none
        print("INIT DATA FRAME:", df)

    def get_df(self):
        return self.df

    def load_datacsv(self):
        if self.datacsv is none :
            self.datacsv = pandas.read_csv('./data.csv')
        return self.datacsv

    def get_datacsv(self):
        return self.loadcsv(self)
