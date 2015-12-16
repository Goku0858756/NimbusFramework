__author__ = 'N05F3R4TU'
# import subprocess

# # 217.149.143.62
# host = input("Enter a host to map: ")
# p1 = subprocess.Popen(args=['nmap', '-v', '-sU', host], stdout=subprocess.PIPE)
#
# output = p1.communicate()[0]
# print(output)

#!/usr/bin/env python
from subprocess import Popen, PIPE

sudo_password = 'FrEaKi12'
# command = 'nmap -Pn -sS -sV -A 217.149.143.62 -oX file-output.xml --reason --packet-trace'.split()
command = 'nmap -Pn -sS -sV -sU 217.149.143.62 -oX file-output2.xml'.split()

p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')[1]
print(sudo_prompt)