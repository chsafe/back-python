import re,sys,os
import pexpect

def telnet(ip,user,pwd):
    child = pexpect.spawn('telnet %s' % ip)
    index = child.expect ([['ame', 'nter','ccount',':',pexpect.TIMEOUT,pexpect.EOF],timeout=3) 
    if index == 2 :  
        print "someting is wrong" 
    child.sendline (user)  
    child.expect ('ass')
    child.sendline(pwd)
    index = child.expect (['#','wakaka'])
    print index
    print child.before
    if index == 0:
        print ip + ":" + user +":" + pwd + ":" "success"
    else:
        print "false"
    return 1;
	
host = "192.168.30.1"
user = "admin"
pwd = "haizhinvshen"
telnet(host,user,pwd)
