import matplotlib.pyplot as plt
import numpy as np
def setup_backend(backend='TkAgg'):
    import sys
    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl
    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt
    return plt

def animate():
    # http://www.scipy.org/Cookbook/Matplotlib/Animations
    mu, sigma = 100, 15
    N = 4
    x = mu + sigma * np.random.randn(N)
    rects = plt.bar(range(N), x, align='center')
    for i in range(50):
        x = mu + sigma * np.random.randn(N)
        for rect, h in zip(rects, x):
            rect.set_height(h)
        fig.canvas.draw()

plt = setup_backend()
fig = plt.figure()
win = fig.canvas.manager.window
win.after(10, animate)
plt.show()
