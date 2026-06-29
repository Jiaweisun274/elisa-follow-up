from lseg.data.content import historical_pricing
import lseg.data as ld
import sqlite3
import datetime
import matplotlib.pyplot as plt


intrinsic_value = 51.05

ld.open_session()

response = historical_pricing.summaries.Definition(
    universe=["ELISA.HE"],
    count = 1,
    fields=["TRDPRC_1"]
).get_data()

print(response.data.df)

ld.close_session()


df = response.data.df

price = df.iloc[0]["TRDPRC_1"]
print(f"Current price of ELISA.HE: {price}")

gap_pct = (intrinsic_value - price) / price * 100
gap_pct = round(gap_pct,2)
print(f"Gap percentage to the intrinsct price calculated(51.05) is {gap_pct}%")

date = df.index[0].strftime("%Y-%m-%d")
notes = ""

conn = sqlite3.connect("../data/elisa_tracker.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS observations( id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT UNIQUE, price REAL,intrinsic_value REAL, gap_pct REAL, notes TEXT)")
cursor.execute("INSERT OR REPLACE INTO observations (date, price, intrinsic_value, gap_pct, notes) VALUES (?, ?, ?, ?, ?)", (date, price, intrinsic_value, gap_pct, notes))
conn.commit()
conn.close()


conn = sqlite3.connect("../data/elisa_tracker.db")
cursor = conn.cursor()
cursor.execute("SELECT date,price FROM observations ORDER BY date")
rows = cursor.fetchall()
dates = []
prices = []
for row in rows:
    dates.append(row[0])
    prices.append(row[1])



plt.plot(dates, prices, label = "Elisa closing price", color = "blue")
plt.axhline(y = intrinsic_value, label = "Intrinsic value (AE model, Dec 2025)", color = "red", linestyle = "--")
plt.title("Elisa corportion - price vs forecastion")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.savefig("../output/tracker_chart.png")