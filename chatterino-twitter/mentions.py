import os
import time
import binascii

def getlog(path):
    logfile = os.listdir(path)[-1]
    logpath = path+logfile
    return logpath

def recentmention(path):
    log = open(getlog(path), 'rb')
    recent = log.readlines()[-1]
    recentascii = recent.decode()
    log.close()
    return recentascii
