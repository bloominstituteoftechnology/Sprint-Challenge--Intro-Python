# importing csv module
import pandas as pd

# csv file name
filename = "cities.csv"

df = pd.read_csv (filename, skiprows = 1 )

print(df.head(5))
