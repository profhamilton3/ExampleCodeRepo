""" datacsv.py
    upload a sample csv files sourced from w3schools.org
"""
import pandas as pd


class DataCsv:
    def __init__(self):
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }
        self.df = pd.DataFrame(data)
        self.datacsv = pd.DataFrame()  # intentionally empty
        print("INIT DATA FRAME:", self.df)

    def get_df(self):
        return self.df

    def set_df(self, newDF):
        if isinstance(newDF, pd.DataFrame):
            del self.df
            self.df = newDF

    def set_datacsv(self, data):
        if isinstance(data, pd.DataFrame):
            del self.datacsv
            self.datacsv = data

    def get_datacsv(self):
        return self.datacsv
