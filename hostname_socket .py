# My hotnmae code 
import socket

hostname = socket.gethostname()
print (hostname)
getIpAddress = socket.gethostbyname(hostname)
print (getIpAddress)
if '168' in getIpAddress:
    print ("Ip is in the static range")
else:
    print ("Ip is not in the static range")
