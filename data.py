import csv
import matplotlib.pyplot as plt
'''
code taken from https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
'''

# get data from csv
years, wo, consumption= [], [], []
with open("istherecorrelation.csv", "r") as f:
    data = csv.reader(f, delimiter=';')
    next(data)
    for row in data:
        years.append(int(row[0]))
        wo.append(float(row[1].replace(",", ".")))
        consumption.append(int(row[2]))


# plot data
fig, ax1 = plt.subplots()

ax1.plot(years, consumption, '-o')
ax1.set_xlabel("year")
ax1.set_ylabel("NL Beer consumption [x1000 hectoliter]", color='tab:blue')
ax1.set_xlim(years[0], years[-1])
ax1.set_title("Beer consumption and WO in NL per year")
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.grid()

ax2 = ax1.twinx() 
ax2.plot(years, wo, 'r-o')
ax2.set_ylabel("WO [x1000]", color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.savefig("correlation.png", dpi=300)
plt.show()
