import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return (line,)
    
    
# animation function. This is called sequentially
def animate(i, data):
    x = data['wl']
    y = np.sin(data[data.columns[i]])
    line.set_data(x, y)
    return (line,)
    
def animate_spectra(data):
    fig, ax = plt.subplots()
    ax.set_ylim(( 0, 1.0e-14))
    ax.set_xlim((2500, 5500))
    line, = ax.plot([], [], lw=2)
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=101, interval=100, blit=True)
    HTML(anim.to_html5_video())

