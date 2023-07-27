import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = '../Data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])

        except ValueError:
            print(f"Missing data for {row[2]}")
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()
plt.show()
