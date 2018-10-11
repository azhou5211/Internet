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

#RS server
def RSserver():
	file = open("PROJI-DNSRS.txt","r")
	reader = file.read().splitlines()
	j=0
	array = []
#Please change the  NS record  in the sample PROJ1-DNSRS.txt file  with the name of the server  on which you are executing  TS server program.
	for i in reader:
		splitted = i.split()
		fullname = splitted[0] + " " + splitted[1] + " " + splitted[2]
		temp = hostobject(splitted[0],splitted[1],splitted[2],fullname)
		array.append(temp)
	
	
	try:
		rssd = mysoc.socket(mysoc.AF_INET,mysoc.SOCK_STREAM)
	except mysoc.error as err:
		print('[RS]{} \n'.format("RSserver socket open error ", err))
	server_binding = ('',50007)
	rssd.bind(server_binding)
	rssd.listen(1)
	host=mysoc.gethostname()
	print("[RS]: Server host name is: ",host)
	localhost_ip=(mysoc.gethostbyname(host))
	print("[RS]: Server IP address is  ",localhost_ip)
	crsd,addr=rssd.accept()
	print ("[RS]: Got a connection request from a client at", addr)
	while(1):
		data = crsd.recv(1024)
		if not data:
			break
		word = data.decode('utf-8')
		print("client word: " + word)
		found = 0;
		for i in range(0,len(array)):
			if(array[i].name==word):
				msg = array[i].fullname
				print("server sent: " + msg)
				word=msg.encode('utf-8')
				crsd.send(word)
				found=1
				break;
		if(found==0):
			k=len(array)-1
			for i in range(len(array)-1,-1,-1):
				if(array[i].flag=="NS"):
					k=i
			msg = array[k].fullname
			print("server sent: " + msg)
			word = msg.encode('utf-8')
			crsd.send(word)
	rssd.close() 
	exit()
	
		
if __name__ == "__main__":
	RSserver()
