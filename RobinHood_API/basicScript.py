import robin_stocks.robinhood as r
import pandas as pd

# User login using linux/unix terminal commands
file = open(".password.txt", "r")
username = file.readline()[:-1]
password = file.readline()[:-1]
r.login(username, password)
print("Sign in successful.")

dataframe1 = pd.read_excel("GarnetFundTutorials/FileIO/output.xlsx")

sectors = dataframe1["Sector"].to_list()
sectors = [x for x in sectors if x==x]
stocks = dataframe1["Stock"].to_list()
stocks = [x for x in stocks if x==x]
etfs = dataframe1["ETF"].to_list()
etfs = [x for x in etfs if x==x]

print(stocks)

print("Sectors:", sectors)
print("Stocks:", stocks)
print("ETFS:", etfs)

for stock in stocks:
    print(r.get_fundamentals(stock, info="open"))