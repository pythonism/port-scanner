#!/usr/bin/env python3

import socket

ports = [ 20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 
				  15, 123, 137, 137, 138, 139, 143, 161, 179, 443, 
				  445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 
				  1723, 3128, 3268, 3306, 3389, 4899, 5432, 5060, 
				  5900, 5938, 8080, 10000, 20000 ]

target = input('Domain or ip-adress: ')

for port in ports:
  s = socket.socket()
  s.settimeout(1)
  try:
    s.connect((target, port))
  except socket.error:
    pass
  else:
    s.close
    print (target + ': port ' + str(port) + ' opened')
