from turtle import color
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_vlaues, rw.y_vlaues, linewidth =2)

    #Emphazise the first and last points plotted
    ax.scatter(0,0, s=100, c='green', edgecolors='none')
    ax.scatter(rw.x_vlaues[-1],rw.y_vlaues[-1], s=100, c='red' )

    #Removing Axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break