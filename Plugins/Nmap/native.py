__author__ = 'N05F3R4TU'
import subprocess

# 217.149.143.62
host = input("Enter a host to map: ")
p1 = subprocess.Popen(args=['nmap', '-v', '-sU', host], stdout=subprocess.PIPE)

output = p1.communicate()[0]
print(output)