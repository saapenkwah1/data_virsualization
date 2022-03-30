from shutil import which
import matplotlib.pyplot as plt
import numpy as np


x_values = np.linspace(0,2,100)
fig, ax =plt.subplots(figsize=(16, 9), layout='constrained')
ax.plot(x_values, x_values, label ='linear')
ax.plot(x_values,x_values**2, label= 'quadratic' )
ax.plot(x_values,x_values**3, label ='cubic')

#styling my x values
ax.set_xlabel("x label", fontsize =14)
ax.set_ylabel("y label", fontsize =14)
ax.set_title("simple plot", fontsize =20)

ax.tick_params(axis='both', which ='major', labelsize =12)
plt.legend()
plt.show()
