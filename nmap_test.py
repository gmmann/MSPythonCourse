import sys
import os
import nmap                         # import nmap.py module
# nm = nmap.PortScanner
nm_test = nmap.PortScanner()

# print(nm_test('192.168.69.9')

#try:
#    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
#except nm.PortScannerError:
#    print('Nmap not found', sys.exc_info()[0])
#    sys.exit(1)
#except:
#    print("Unexpected error:", sys.exc_info()[0])
#    sys.exit(1)

# # # nm.scan('68.171.170.0/24', '20,21,22,23,25,80,443,8080,8443,9443,61612-61619') # scan host
# # # for host in nm.all_hosts():
# # #      #print('Host : %s ' % (host, ))
# # #      #print('State : %s' % nm[host].state())
# # #      for proto in nm[host].all_protocols():
# # #          #print('B----------')
# # #          #print('Protocol : %s' % proto)
 
# # #          lport = nm[host][proto].keys()
# # #          #lport.sort()
# # #          for port in lport:
# # #              #print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
# # #              if 'open' in nm[host][proto][port]['state']:
# # #                  print('Host : %s ' % (host, ))
# # #                  print('State : %s' % nm[host].state())
# # #                  print('Protocol : %s' % proto)
# # #                  print ('   port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
# # #                  print('------------------')



