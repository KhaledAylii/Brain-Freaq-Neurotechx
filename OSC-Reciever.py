from liblo import *
import sys 
import time
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)
        
    alpha, delta, beta, theta, gamma = [0], [0], [0], [0], [0]
    #receive EEG data
    @make_method('/muse/elements/alpha_absolute', 'ffff')
    def alpha_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        #recives data from each sensor at the path
        self.alpha = [x * 10 for x in list(args)]
        #stores values from each sensor in bels and converts them to decibels by multiplying it by 10
    @make_method('/muse/elements/delta_absolute', 'ffff')
    def delta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.delta = [x * 10 for x in list(args)]
    @make_method('/muse/elements/beta_absolute', 'ffff')
    def beta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.beta = [x * 10 for x in list(args)]
    @make_method('/muse/elements/theta_absolute', 'ffff')
    def theta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.theta = [x * 10 for x in list(args)]
    @make_method('/muse/elements/gamma_absolute', 'ffff')
    def gamma_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.gamma = [x * 10 for x in list(args)]

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()
if __name__ == "__main__":
    def animated_barplot():
            N = 5
            x = [20,20,20,20,20]
            rects = plt.barh(range(N), x,  align = 'center')
            while 1:
                x = [server.alpha[0],
                     server.delta[0],
                     server.beta[0],
                     server.theta[0],
                     server.gamma[0]]
                for rect, h in zip(rects, x):
                    x = [server.alpha[0],
                         server.delta[0],
                         server.beta[0],
                         server.theta[0],
                         server.gamma[0]]
                    print "swag"
                    rect.set_height(h)
                fig.canvas.draw()

    fig = plt.figure()
    win = fig.canvas.manager.window
    win.after(100, animated_barplot)
    plt.show()
    while 1:
        time.sleep(1)
