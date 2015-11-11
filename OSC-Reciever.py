from liblo import *

import sys 
import time


class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive EEG data
    @make_method('/muse/elements/alpha_absolute', 'ffff')
    def alpha_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
    @make_method('/muse/elements/beta_absolute', 'ffff')
    def beta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
    @make_method('/muse/elements/theta_absolute', 'ffff')
    def theta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
    @make_method('/muse/elements/gamma_absolute', 'ffff')
    def gamma_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        gamma = list(args)
        print gamma
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()
if __name__ == "__main__":
    while 1:
        time.sleep(1)
