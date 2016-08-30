#!/usr/bin/env python
from __future__ import print_function, division
import ftplib
import os


def upload_dir(server, user, psswd, folder):
    '''
    Upload a directory to a ftp server.
    '''
    ftp = ftplib.FTP(server)
    ftp.login(user, psswd)
    print(ftp.getwelcome())
    if server == 'www2.mpia.de' and user in ['banados', 'PS1_QSO']:
        ftp.cwd("public_html")
    file_list = ftp.nlst()
    #print(file_list)

    print("Uploading files ...")
    for root, dirs, files in os.walk(folder):
        print('root', root)
        if root not in file_list:
            print('mkdir' , root, ' in server')
            ftp.mkd(root)
            file_list.append(root)
        
        for fname in files:
            print(os.path.join(root, fname))
            upload_file(ftp, os.path.join(root, fname))
    
    ftp.quit()
    print("Uploaded to {0:s}/{1:s}/{2:s}".format(server, user, folder))
    
    
def upload_file(ftp, file):
    '''
    upload a file to a ftp server
    '''
    
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
