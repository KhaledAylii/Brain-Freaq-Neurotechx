from liblo import *

import sys 
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive EEG data
    @make_method('/muse/elements/alpha_absolute', 'ffff')
    def alpha_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.alpha = list(args)
    @make_method('/muse/elements/alpha_absolute', 'ffff')
    def delta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.delta = list(args)
    @make_method('/muse/elements/beta_absolute', 'ffff')
    def beta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.beta = list(args)
    @make_method('/muse/elements/theta_absolute', 'ffff')
    def theta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.theta = list(args)
    @make_method('/muse/elements/gamma_absolute', 'ffff')
    def gamma_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        self.gamma = list(args)
    alpha = [0]
    delta = [0]
    beta = [0]
    theta = [0]
    gamma = [0]

    
try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()
if __name__ == "__main__":
    while 1:
        
        time.sleep(1)

