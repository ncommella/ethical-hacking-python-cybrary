#!/usr/bin/python3

import nmap
import sys
import time
from pprint import pprint

nm_scan = nmap.PortScanner()

#Check to ensure user entered arguments
if len(sys.argv) == 1:
    print('ERROR! No Arguments!\nProper usage is "./active_info.py <Target IP> <Name of Output File>"\n Leave Output File blank to print scan info to CLI')
    sys.exit()
print('Running...')

#Begin Scan
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-O')

#Assign Scan info to variables
host_status = 'The host is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['status']['state'])
port_status = 'The port 80 is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state'])
scanning_method = 'The scanning method is: {}\n'.format(nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'])
try:
    guess_os = 'There is {} percent chance that the host is running {}'.format(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])
except IndexError:
    guess_os = 'No OS info gathered'

#Check for Output File name
if len(sys.argv) == 3:
    with open("%s.txt"%sys.argv[2], 'w') as f:
        f.write("Full Scan: \n"+str(nm_scanner))
        f.write("\n\nSummary: \n"+host_status+port_status+scanning_method+guess_os)
        f.write("\nReport Generated: "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))
    print('Finished!')
#Print scan info to CLI for no output file
else:
    #Pretty Print Full Scan
    pprint(nm_scanner)

    #Summary Print Block
    print('Summary: \n')
    print(host_status)
    print(port_status)
    print(scanning_method)
    print(guess_os)
