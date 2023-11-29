import nmap

scanner = nmap.PortScanner()
print('Welcome! We Have the Nmap Automation Tool Ready Right Here.')
print('------------------------------------------------------------')

ip_add = input('Enter IP address for scan: ')
print('You entered: ', ip_add)

respo = input('''\nSelect scan type:
              1) SYN ACK Scan
              2) UDP Scan
              3) Comprehensive Scan
              Your choice: ''')

print('You chose: ', respo)

if respo == '1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_add, '1-9999', '-v -sS')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_add].state())
    
    if 'tcp' in scanner[ip_add]:
        print(scanner[ip_add].all_protocols())
        print('Open Ports: ', scanner[ip_add]['tcp'].keys())
    else:
        print('No open TCP ports found.')
elif respo == '2':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_add, '1-9999', '-v -sU')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_add].state())
    
    if 'udp' in scanner[ip_add]:
        print(scanner[ip_add].all_protocols())
        print('Open Ports: ', scanner[ip_add]['udp'].keys())
    else:
        print('No open UDP ports found.')
elif respo == '3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_add, '1-9999', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_add].state())
    
    if 'tcp' in scanner[ip_add]:
        print(scanner[ip_add].all_protocols())
        print('Open Ports: ', scanner[ip_add]['tcp'].keys())
    else:
        print('No open TCP ports found.')
else:
    print('Invalid selection. Please try again.')