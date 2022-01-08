import os
import pandas as pd
import matplotlib.pyplot as plt

# Load City information to data frame
df = pd.read_csv("City.csv")

# Apply basic statistical computations using pandas describe() function 
dF.describe()

# Get Counts for a specific column
dF["city_name"].value_counts()

y = list(df.peopleCount)
plt.boxplot(y)
plt.show()
