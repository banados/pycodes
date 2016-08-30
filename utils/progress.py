import sys

def progress(i,total,step=5.):
    '''prints the percentage done in a process
    
    i       number of actual process 
    total   total number of processes
    step    e.g. if step=5.(Default)
            only will be printed the percentages multiples of 5 
            i.e., 0% 5% 10% 15% etc  '''
    p = (i+1.0)/total*100.
    if int(p)%step==0:
        sys.stdout.write("\r%d%%" %p)   
        sys.stdout.flush()
