import pandas as pd
import openpyxl as op

# Sectors and stocks - fifth entry is etf
sectors = []
stocks = []
etfs = []

# Read in text file and split it apart
with open("GarnetFundTutorials/API/stocks.txt", "r") as file:

    for line in file:
        category, data = line.strip().split(" ", 1)
        sectors.append(category)

        data_parts = data.split(", ")

        for i in range(len(data_parts[:4])):
            stocks.append(data_parts[i].strip())

        etfs.append(data_parts[4])

print("Sectors:", sectors)
print("Stocks:", stocks)
print("Etfs:", etfs)

# Merge into pandas DataFrame
data = []
data.append(sectors)
data.append(stocks)
data.append(etfs)
print(data)
df = pd.DataFrame(data).transpose()
df.columns = ["Sector", "Stock", "ETF"]
print(df)

df.to_excel("GarnetFundTutorials/API/output1.xlsx", index=False)





