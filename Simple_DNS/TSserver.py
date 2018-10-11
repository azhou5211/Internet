import numpy as mypy
import threading
import time
import random
import socket as mysoc

class hostobject(object):
	name=""
	ip=""
	flag=""
	fullname=""
	
	def __init__(self, name, ip, flag, fullname):
		self.name = name
		self.ip = ip
		self.flag = flag
		self.fullname = fullname

#TS server
def TSserver():
    file = open("PROJI-DNSTS.txt","r")
    reader = file.read().splitlines()
    j=0
    array = []
    for i in reader:
    	splitted = i.split()
    	fullname = splitted[0] + " " + splitted[1] + " " + splitted[2]
    	temp = hostobject(splitted[0],splitted[1],splitted[2],fullname)
    	array.append(temp)
    try:
    	tssd = mysoc.socket(mysoc.AF_INET,mysoc.SOCK_STREAM)
    except mysoc.error as err:
    	print('[TS]: {}\n'.format("socket open error ",err))
    server_binding = ('',50008)
    tssd.bind(server_binding)
    tssd.listen(1)
    host=mysoc.gethostname()
    print("[TS]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[TS]: Server IP address is  ",localhost_ip)
    ctsd,addr=tssd.accept()
    print ("[TS]: Got a connection request from a client at", addr)
    while(1):
    	data = ctsd.recv(1024)
    	if not data:
    		break
    	word = data.decode('utf-8')
    	print("client word: " + word)
    	found = 0;
    	for i in range(0,len(array)):
    		if(array[i].name==word):
    			msg = array[i].fullname
    			print("sent message: " + msg)
    			word=msg.encode('utf-8')
    			ctsd.send(word)
    			found=1
    			break
    	if(found==0):
    		msg = word + " - Error:HOST NOT FOUND"
    		word = msg.encode('utf-8')
    		print("sent message: " + msg)
    		ctsd.send(word)
    tssd.close()
    exit()


if __name__ == "__main__":
	TSserver()
	
