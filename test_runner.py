# test_runner.py - pytest will run this automatically
# we will list it explicitely in the yml file just in case
import pytest
import pandas
import seaborn as sns
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
    assert (df_data).size > 0


def test_two():
    s1 = pandas.Series([0, 1, 2, 4, 5, 6, 2])
    print(s1)
    assert s1.size > 0


def test_three(df_data):
    print((df_data).loc[0])
    assert (df_data).loc[0].size > 0


def test_datacsv():
    dcsv = datacsv.DataCsv()
    assert 0 == dcsv.get_datacsv().size


def test_datacsv_get_df():
    dcsv = datacsv.DataCsv()
    df = dcsv.get_df()
    assert df.size > 0


def test_readcsv():
    d = pandas.read_csv('./data.csv')
    assert d.size > 0


def test_datacsv_set_get_datacsv():
    data = pandas.read_csv('./data.csv')
    assert data.size > 0
    dcsv = datacsv.DataCsv()
    dcsv.set_datacsv(data)
    df = dcsv.get_datacsv()
    assert df.size > 0


def test_edata_load():
    data = sns.load_data('flights')
    assert data.size > 0
