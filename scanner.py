import pyfiglet
import sys
import socket
from datetime import datetime

roman = pyfiglet.figlet_format("Port Scanner")
print(roman)

#Define the target

if len(sys.argv) == 2:

# Translate hostname to IPv4 

    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")

#Add banner

print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

#Scan ports

try:
    for port in range (1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)

     #Returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {}:      Open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()







