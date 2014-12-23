#!/usr/bin/python

#print "This line will be printed.cfggfg"

import shutil
import os
import time

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

with open('toberead3.txt','r') as file:
    for line in file:
    	#print line                
    	srcDst = line.split(':');        
    	srcUrl = srcDst[0].strip()    	 
        dstUrl = srcDst[2].strip()               
        dstPath =srcDst[1].strip()                       
    	#dstUrl = dstUrl.replace('"', '');
        srcfullUrl = '/var/www/html/python/'+srcUrl          
        #srcfullUrl = srcfullUrl.replace('"', '');
    	chkpath = '/var/www/html/python_out/'+dstPath
        dstfullpath = chkpath+dstUrl
        
    	if not os.path.exists(chkpath):
    		os.makedirs(chkpath)
    	shutil.copy2(srcfullUrl, dstfullpath)        

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime
#with open('toberead.txt') as f: s = f.readline()
#fo = open("toberead.txt", "rw+")
#fo.seek(0,0)
#last_pos = fo.tell()
#fo.seek(last_pos)
#line = fo.readline()
#print line
#print '=================='
#last_pos = fo.tell()
#fo.seek(last_pos)
#line3 = fo.readline()
#print line3
#fo.close()
#seeking = s.seek(1);
#print seeking
#exit