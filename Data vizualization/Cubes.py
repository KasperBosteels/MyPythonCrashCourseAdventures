from matplotlib import pyplot as plt

x_values = range(1,10)
y_values = [x**3 for x in x_values]
plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.axis([0,10,0,x_values[-1]**3 + 10])

ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()