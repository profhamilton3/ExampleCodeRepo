# test.py
import pandas as pd

def test_dataset():
    mydataset = {
        'cars': ["BMW", "Volvo", "Ford", "Toyota", "Hyundai", "Daiwu"],
        'passings': [3, 7, 2, 9, 6, 2]
    }
    myvar = pd.DataFrame(mydataset)
    print("Pandas DataFrame")
    print(myvar) 
    assert myvar.size > 0

def test_dataseries_toframe():
    a = [1, 7, 2, 12, 5, 3]
    b = [3, 3, 2, 2, 5, 3]
    mya = pd.Series(a, index = ["x", "y", "z", "a", "b", "c"])
    myb = pd.Series(b, index = ["x", "y", "z", "a", "b", "c"])
    print(mya)
    print(myb)
    df = pd.DataFrame({'a':mya,'b':myb})
    print(df)
    assert mya.size > 0
    assert myb.size > 0
    assert df.size > 0
