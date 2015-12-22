__author__ = 'N05F3R4TU'

class NmapScanner(object):

    def __init__(self, ip=None, name=None, verbose=False, shell=False):

        self.name = "Nmap Scanner"
        self.version = "1.2"
        self.sudo_pwd = "FrEaKi12"
        self.verbose = verbose
        self.host = ""
        self.shell = shell
        self.cmd = ["nmap", "-Pn", "-sU"]
        self.cmd_dict = {"scan":"nmap", "ping":"-Pn", }

        try:
            # Append Host to command-table
            if ip != None and name != None:
                self.host = ip
                self.cmd.append(ip)
            elif ip != None:
                self.host = ip
                self.cmd.append(ip)
            elif name != None:
                self.host = self.hostname_convert(hostname=name)
                self.cmd.append(self.host)
            else:
                print("I dont get this!")

            # Verbose On/Off
            if verbose:
                self.cmd.append("-v")

            # At Output File
            self.cmd.append(self.output_file())
        except Exception as e:
            print(e)


    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
        return self

    def hostname_convert(self, hostname):
        import socket
        from urllib.parse import urlparse
        import re

        if re.findall("http", hostname):
            url = urlparse(url=hostname)
            if not url.netloc:
                print("Netloc is Empty")
            else:
                ip4 = socket.gethostbyname(url.netloc)
                return ip4
        elif re.findall("www.", hostname):
            if str(hostname).find("www.") == 0:
                ip4 = socket.gethostbyname(hostname)
                return ip4
        else:
            try:
                return str(socket.gethostbyname(hostname))
            except Exception as e:
                print(e)


    def scan(self):
        from subprocess import Popen, PIPE
        self.pipe = Popen(['sudo', '-S'] + self.assemble().split(), stdin=PIPE, stderr=PIPE, universal_newlines=True)
        self.prompt = self.pipe.communicate(self.sudo_pwd + '\n')[1]
        print(self.prompt)

    def assemble(self):
        full_command = " ".join(self.cmd)
        return full_command

    def output_file(self):
        from datetime import datetime
        from Plugins.IPConversion.controller import ip_to_int as convert

        d = datetime.now()
        # ip = convert(ip=self.host)

        filename = "{}-{}{}{}-{}-{}-{}.xml".format(convert(ip=self.host), d.year, d.day, d.month, d.hour, d.minute, d.second)

        return "-oX {}".format(filename)


if __name__ == '__main__':
    scan = NmapScanner(name="www.pickupwomen.net", verbose=True)
    scan.scan()
