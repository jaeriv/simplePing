import subprocess
from multiprocessing import Pool
import multiprocessing
import os

#<Start---opens and reads ip address file--->
ipList = open('IP_List.txt','r')   #This is a text file that includes the IP addresses.
result = ipList.read()
sepList = result.split()
ip = sepList
#<End---opens and reads ip address file--->

#<Start---ping function--->
def ping(ip):
	p = subprocess.Popen(["ping", "-n", "2",ip],stdout = subprocess.PIPE).communicate()[0]
	if b"TTL" in p:
		print("Ping to " + ip + " was successful!")
	else:
		print("Ping to " + ip + " failed!")
	ipList.close()
#<End---ping function--->

#<Start---multiprocessing code--->
if __name__ == '__main__':
	pool = Pool()
	pool.map(ping,ip)
#<End---multiprocessing code--->
