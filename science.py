import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn')
fig, ax = plt.subplots()  # a figure with a single Axes
ax.plot(input_values,squares, linewidth = 2)

#set title and label on the axes
ax.set_title("Sqaure Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize= 14)
ax.set_ylabel("Square of Value", fontsize= 14)

#size of tick labels
ax.tick_params(axis='both', labelsize =14)
plt.show()
