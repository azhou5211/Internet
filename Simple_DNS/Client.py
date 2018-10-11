import numpy as mypy
import threading
import time
import random
import socket as mysoc

#Client
def client():
	file_write = open("RESOLVED.txt","w")
	file = open("PROJI-HNS.txt","r")
	reader = file.read().splitlines()
	
	try:
	#[ first socket]
		ctors=mysoc.socket(mysoc.AF_INET,mysoc.SOCK_STREAM)
	except mysoc.error as err:
		print('{} \n'.format("socketopen error ",err))
	#[second socket]
	try:
		ctots=mysoc.socket(mysoc.AF_INET,mysoc.SOCK_STREAM)
	except mysoc.error as err:
		print('{} \n'.format("socketopen error ", err))
#[determine hostname of RS server and port ]
#[bind ctors socket to RS address,rsport]
#REMEMBER TO CHANGE THE RS SERVER CONNECTION HOSTNAME
	rsaddr =mysoc.gethostbyname("python.cs.rutgers.edu")
	server_binding=(rsaddr,50007)
	ctors.connect(server_binding)
	connection = 1
	for i in reader:
		print(i)
		msg = i.encode('utf-8')
		ctors.send(msg)
		data = ctors.recv(1024)
		ans = data.decode('utf-8')
		splitted = ans.split()
		if(splitted[2]=="A"):
			file_write.write(ans)
			file_write.write("\n")
		else:
			if(splitted[2]=="NS"):
				if(connection==1):
					tsaddr =mysoc.gethostbyname(splitted[0])
					server_binding2=(tsaddr,50008)
					ctots.connect(server_binding2)
					connection = 0
				ctots.send(msg)
				data = ctots.recv(1024)
				ans = data.decode('utf-8')
				file_write.write(ans)
				file_write.write("\n")
	ctors.close()
	ctots.close()
	file.close()
	file_write.close()
	
		
if __name__ == "__main__":
	time.sleep(random.random()*5)
	t2 = threading.Thread(name='client', target=client)
	t2.start()
	input("Hit ENTER  to exit")
	print("")
	exit()
