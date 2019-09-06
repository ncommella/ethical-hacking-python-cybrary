#!/usr/bin/python3

import nmap
import sys
from pprint import pprint

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-O')

host_status = 'The host is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['status']['state'])
port_status = 'The port 80 is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state'])
scanning_method = 'The scanning method is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'])
try:
    guess_os = 'There is {} percent chance that the host is running {}'.format(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])
except IndexError:
    guess_os = 'No OS info gathered'

#Pretty Print Full Scan
pprint(nm_scanner)

#Summary Print Block
print('Summary: \n')
print(host_status)
print(port_status)
print(scanning_method)
print(guess_os)

#if len(sys.arguments) == 3:
#    with open("%s.txt"%sys.argv[2], 'w') as f:
