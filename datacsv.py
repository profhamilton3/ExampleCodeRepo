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
        self.datacsv = None
        print("INIT DATA FRAME:", self.df)

    def get_df(self):
        return self.df

    def set_df(self, newDF):
        if isinstance(newDF,pandas.DataFrame) :
            del self.df
            self.df = newDF
        

    def load_datacsv(self):
        if self.datacsv is None :
            self.datacsv = pandas.read_csv('./data.csv')
        return self.datacsv

    def get_datacsv(self):
        return self.loadcsv(self)
