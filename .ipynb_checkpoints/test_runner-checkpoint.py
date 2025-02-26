# test_runner.py - pytest will run this automatically
# we will list it explicitely in the yml file just in case
import pytest
import pandas
import datacsv

@pytest.fixture
def df_data():
    ds = {
        'cars': ["BMW", "Volvo", "Ford", "Toyota", "Hyunda", "Cheverolete", "Oldsmobile", "Pontiac", "Buick"],
        'passings': [3, 7, 2, 6, 5, 3, 4, 8, 4]
    }
    dataframe = pandas.DataFrame(ds)
    return dataframe

def test_one(df_data):
    print(df_data)
    assert False == (df_data).empty

def test_two():
    s1 = pandas.Series([0, 1, 2, 4, 5, 6, 2])
    print(s1)
    assert False == s1.empty
    

def test_three(df_data):
    print((df_data).loc[0])
    assert False == (df_data).loc[0].empty

def test_datacsv():
    dcsv = datacsv.DataCsv()
    assert True == dcsv.get_datacsv().empty

def test_datacsv_get_df():
    dcsv = datacsv.DataCsv()
    df = dcsv.get_df()
    assert False == df.empty

def test_readcsv():
    d = pandas.read_csv('./data.csv')
    assert False == d.empty

def test_datacsv_set_get_datacsv():
    data = pandas.read_csv('./data.csv')
    assert False == data.empty
    dcsv = datacsv.DataCsv()
    dcsv.set_datacsv(data)
    df = dcsv.get_datacsv()
    assert False == df.empty
