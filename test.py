# test.py
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford", "Toyota", "Hyundai", "Daiwu"],
  'passings': [3, 7, 2, 9,6,2]
}

myvar = pd.DataFrame(mydataset)
print("Pandas DataFrame")
print(myvar)

  
