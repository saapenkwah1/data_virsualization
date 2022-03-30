import matplotlib.pyplot as plt

x_values = range(1, 10001)
y_values =[X**2 for X in x_values]

#Create fig with a single axes. plot values in a scatter diagram.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=2)

#set title and label styles
ax.set_title("Square Numbers",  fontsize = 20)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

#set size tick label
ax.tick_params(axis ='both', which ='major', labelsize = 12)
#set range for each axis
ax.axis([0, 1100, 0, 1100000])
plt.show()


