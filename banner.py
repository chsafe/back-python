import re,sys,os
import pexpect
import threading
import time

def banner(ip):
    child = pexpect.spawn('telnet %s' % ip)
    index = child.expect (['ame', 'nter','ccount','ogin',pexpect.TIMEOUT,pexpect.EOF],timeout=5) 
    if index > 3 :  
        print ip + ":" +"someting is wrong"
    else:
        ip=str(ip)
        print ip + "@" + child.before
        os.system("echo %s >> ip.txt " %(ip) )
    return 1;
	
host = open('host.txt')
for line in host:
    ip = line.strip('\n')
    t=threading.Thread(target=banner,args=(ip,))
    t.start()
