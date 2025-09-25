#!/usr/bin/python3
import numpy as np
import datetime
import sys
import subprocess
import pyperclip  # to the paste buffer!

# logfname = '/home/blake/hashlog.txt'
logfname = '/home/blake/BH_Sync_New/Projects/hashData/hashlog.txt'
av = sys.argv

if len(av) == 1:
    ext = ''
elif len(av) == 3:
    if av[1] == 'lookup':  # look up creation time of a prior hash
         thash = av[2]
         try:
            res = (subprocess.check_output(['grep', thash, logfname])).decode('utf-8').strip()
            print(res)
         except:
             print('[', thash, '] not found')
    quit()
elif len(av) == 2:
    ext = av[1]
else:
    print('Usage: \n   > hashFileName.py  [extension]')
    quit()
al = list('ABCDEFGHIJKLMNPQRSTUV') # delete O to reduce confusion w 0.
nu = list('0123456789')

letters = ''.join(np.random.choice(al, 2))
digits  = ''.join(np.random.choice(nu, 5))
result = letters+digits+ext
hashonly = letters+digits

# log the new hash with its creation date
ofp = open(logfname, 'a')
#  '2011-11-03 18:21:26'
timestr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestr, ', ', hashonly, file=ofp)
ofp.close()

print('Random file hash: ', result)
pyperclip.copy(result)  # put it in the pastebuf!
