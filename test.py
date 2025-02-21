# test.py
import pandas as pd

def test_dataset():
    mydataset = {
        'cars': ["BMW", "Volvo", "Ford", "Toyota", "Hyundai", "Daiwu"],
        'passings': [3, 7, 2, 9, 6, 2]
    }
    myvar = pd.DataFrame(mydataset)
    print("Pandas DataFrame")
    assert myvar.empty == False
    print(myvar) 

def dataseries_toframe_test():
    a = [1, 7, 2, 12, 5, 3]
    b = [3, 3, 2, 2, 5, 3]
    mya = pd.Series(a, index = ["x", "y", "z", "a", "b", "c"])
    myb = pd.Series(b, index = ["x", "y", "z", "a", "b", "c"])
    assert myva.empty == False
    assert myva.empty == False
    print(mya)
    print(myb)
    df = pd.DataFrame({mya,myb})
    assert df.empty == False
    print(df)


