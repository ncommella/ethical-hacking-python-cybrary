#!/usr/bin/python3

import nmap
import sys
from pprint import pprint

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-O')

#Pretty Print Full Scan
pprint(nm_scanner)

#Summary Print Block
print('Summary: \n')
print('The host is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['status']['state']))
print('The port 80 is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']))
print('The scanning method is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']))
try:
    print('There is {} percent chance that the host is running {}'.format(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name']))
except IndexError:
    print('No OS info gathered')
