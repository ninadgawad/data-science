import os
import pandas as pd
import json

def convertdict2dataframe(dict):
  return pd.DataFrame.from_dict(dict)  


if __name__ == '__main__':
  print("-" * 45)
  print("\t Main Function")
  print("-" * 45)
  dict = {"a":"10","b":"20","c":"30"}
  df = convertdict2dataframe(dict)
  print(df.head(5))
