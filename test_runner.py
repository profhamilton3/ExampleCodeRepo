#test_runner.py - pytest will run this automatically
#we will list it explicitely in the yml file just in case
import pytest
import pandas


@pytest.fixture
def df_data():
    ds = {
        'cars': ["BMW", "Volvo", "Ford","Toyota", "Hyunda", "Cheverolete"],
        'passings': [3, 7, 2, 6, 5]
    }
    return pandas.DataFrame(ds)
    

def test_one(df_data):
  assert False = dataframe


def test_two():
  s1 = pandas.Series([0,1,2,4,5,6,2])
  assert False == s1.empty
  print(s1)


