import os
import pandas as pd
import json


def dict_to_dataframe(dict):
    return pd.DataFrame.from_dict(dict, orient='index')


if __name__ == '__main__':
    print("-" * 44)
    print("\t Main Function")
    print("-" * 44)
    data = {'a':'10', 'b':'20', 'c':'30'}
    df = dict_to_dataframe(data)
    print(df.head(5))
