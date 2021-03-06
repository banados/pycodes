#!/usr/bin/env python
from __future__ import print_function, division
import argparse
import time
import os

import numpy as np

from lsdlib import read_input
from astropy.io import ascii
from astropy.table import Table
from astropy.utils.console import human_time
from astropy.coordinates import ICRS
from astropy import units as u

EXAMPLES = '''



            '''
            
            
def parse_arguments():

    parser = argparse.ArgumentParser(
        description='''
        This receives a table (fits or text file) with candidates.
        The table has to contain ps1_name ra(deg) dec(deg).
        If the columns are not named. It will assume that 
        ps1_name is in the first column
        ra(deg) in the second
        dec(deg) in the third.
        
        And creates a list file for JSkycalc
        
        The output file has this form
        name     rah  ram  ras    decd  decm  decs   equinox
        
        
        The equinox for the moment is J2000.
        TODO. Make it an input
                
    
                      ''',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLES)
        
    parser.add_argument('-t', '--table', type=str, required=True,
        help='Table (fits or text file) with candidates')
        
                   
    parser.add_argument('-e', '--ext', default=1, type=int,
        help='the extension to read if  the --table file \
        information is a fits file. (default: %(default)s) ')
                
            
    parser.add_argument('--version', action='version', version='1.0')
    
    return parser.parse_args()
    
    
if __name__ == '__main__':
    start_time=time.time()
    args=parse_arguments()
    
    try:
        table = Table(read_input(args.table))
    except IndexError:
        table = Table(read_input(args.table, ext=args.ext))
        
    try:
        ra=table['ra']
        dec=table['dec']
        name=table['name']
    except Exception as e:
        print(e)
        ra=table['col2']
        dec=table['col3']
        name=table['col1']
    
            
    table_name, table_ext = os.path.splitext(args.table)
    
    c = ICRS(ra=ra, dec=dec, unit=(u.degree, u.degree))
    
    rah = np.int_(c.ra.hms[0])
    ram = np.int_(c.ra.hms[1])
    ras = c.ra.hms[2]
    
    decd = np.int_(c.dec.dms[0])
    decm = np.int_(np.abs(c.dec.dms[1]))
    decs = np.abs(c.dec.dms[2])
    
    #if decd < 0:
    #    decm = decm[1:]
    #    decs = decs[1:]
    
    EQ = ['2000.' for i in decd]
    #print(DEC)
    #out = Table((name, coord_str, EQ),
    #                     names=('name','coord', 'eq'))
    #out = Table((name, RA, DEC, priority),
    #                 names=('name','ra','dec' 'prio'))
    #out = Table((name, RA, DEC, priority),
    #                     names=('name','ra', 'dec', 'prio'))
    #name     rah  ram  ras    decd  decm  decs   equinox
    out = Table((name, rah, ram, ras,
                 decd, decm, decs, EQ),
                 names=('name','rah',  'ram',  'ras', 'decd',  'decm',
                          'decs',   'equinox'))
    print("Test")          
    print(out)           
    out_name= table_name + '.skycalc'
    
                         
    
    #fmts = {'name':'%s', 'coord':'%s', 'prio':'%d'}
    ascii.write(out, out_name, format='no_header')#, formats=fmts)
    
    print("Output: ", out_name)
    
    
    
    print("Elapsed time: {0:s}" .format(human_time(time.time() - start_time)))
