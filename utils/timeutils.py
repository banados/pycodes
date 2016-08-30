#!/usr/bin/env python
import time


    
def print_elapsed_time(start_time):
    '''
    Receive the initial time of a process
    and print the elapsed time in a nice manner.
    
    The input time must be in seconds (e.g  time.time())
    '''
    print "*"*50
    stop_time = time.time()
    hh = int( (stop_time - start_time) / 3600.0 )
    mm = int( (stop_time - start_time) / 60 - hh*60)
    ss = (stop_time - start_time) - 60*mm - 3600*hh
    print "Elapsed time: %dh %dm %2.2fs" % ( hh,mm,ss)
