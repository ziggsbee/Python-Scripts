'''
A basic port scanner in python. Used to test out knowledge for security
'''

import socket
import sys

'''
The min and max is the range of ports you want to test on the given host (The host is given as a parameter on the command
line.
'''
min = 1
max = 1024
if len(sys.argv) < 2 or len(sys.argv) >= 5:
    print("Must pass a ip address")
    exit()

'''
If the user provides more than the hostname we check to see if it is a range or not a number.
'''
if 2 < len(sys.argv) < 5:
    if sys.argv[2].isdigit():
        min = int(sys.argv[2])
        if len(sys.argv) == 4:
            max = int(sys.argv[3])
    else:
        '''
        If it is not a number then we think of it as wanting to search for a common ports
        (I will probably change this later to add more parameters
        '''
        common_ports = {80, 443, 20, 21, 22, 23, 25, 69, 110, 995, 143, 902, 993,
                         385, 587, 3306, 2082, 2083, 2086, 2087,
                        2095, 2096, 2077, 2078, 3389}
        print("Scanning: {} for common open ports".format(sys.argv[1]))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in common_ports:
            try:
                s.settimeout(1000)
                s.connect((sys.argv[1], port))

                print("OPEN: {}".format(port))
                s.close()
            except:
                continue
        print("Finished Scan")
        exit()

'''
Perform a normal scan based off of min and max values
'''
print("Scanning: {} from {} to {}".format(sys.argv[1], min, max))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in range(min, max):
    try:
        s.settimeout(1000)
        s.connect((sys.argv[1], port))

        print("OPEN: {}".format(port))
        s.close()
    except:
        continue
print("Finished Scan")
