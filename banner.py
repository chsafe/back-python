import re,sys,os
import pexpect

def banner(ip):
    child = pexpect.spawn('telnet %s' % ip)
    index = child.expect (['ame', 'nter','ccount','ogin',pexpect.TIMEOUT,pexpect.EOF],timeout=3) 
    if index > 2 :  
        print ip + ":" +"someting is wrong"
    else:
        ip=str(ip)
        print ip + "@" + child.before
        os.system("echo %s >> ip.txt " %(ip) )
    return 1;
	
host = open('host.txt')
for line in host:
    ip = line.strip('\n')
    banner(ip)
