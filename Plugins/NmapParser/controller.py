__author__ = 'N05F3R4TU'
import xml.sax
from pymongo import MongoClient

def db(doc):
    database = MongoClient("localhost", 27017, connect=True)
    print(database["nmap"]["scan17"].insert_one(doc))


class Nmap2Mongo(xml.sax.ContentHandler):

    def __init__(self):
        self.id = id(self)
        self.curr_portid = ""
        self.curr_port = {}
        self.nmap_output = {
            "nmaprun": {"args":"", "start":"", "start_str":""},
            "scaninfo": [],
            "debug": {"level":""},
            "verbose":{"level":""},
            "host": {
                "status": {"state":"", "proto":"", "portid":""},
                "address": {"addr":"", "addr_type":""},
                "hostnames": [],
                "ports": {},
                "os": {
                    "portused": [],
                    "osclass": {"type":"", "vendor":"", "osfamily":"", "osgeh":"", "accurancy":"", "cpe":""},
                    "osmatch": {"name": "", "accuracy":"", "line":""}
                },
                "uptime": {"seconds":"", "lastboot":""}
            },
            "runstats": {
                "finished": {"time":"", "timestr":"", "elapsed":"", "summary":"", "exit":""},
                "hosts": {"up":"", "down":"", "total":""}
            }
        }


    def startElement(self, tag, attributes):

        try:
            if tag == "nmaprun":
                self.nmap_output[tag]["args"] = attributes["args"]
                self.nmap_output[tag]["start"] = attributes["start"]
                self.nmap_output[tag]["start_str"] = attributes["startstr"]

            elif tag == "scaninfo":
                self.nmap_output["scaninfo"].append({"type":attributes["type"], "protocol":attributes["protocol"], "numservices":attributes["numservices"], "services":attributes["services"]})

            elif tag in ["debugging"]:
                self.nmap_output["debug"]["level"] = attributes["level"]

            elif tag in ["verbose"]:
                self.nmap_output["verbose"]["level"] = attributes["level"]


            elif tag == "status":
                self.nmap_output["host"]["status"]["state"] = attributes["state"]
                self.nmap_output["host"]["status"]["reason"] = attributes["reason"]
                self.nmap_output["host"]["status"]["portid"] = attributes["reason_ttl"]

            elif tag == "address":
                self.nmap_output["host"]["address"]["addr"] = attributes["addr"]
                self.nmap_output["host"]["address"]["addr_type"] = attributes["addrtype"]

            elif tag == "hostname":
                self.nmap_output["host"]["hostnames"].append({"name":attributes["name"], "type":attributes["type"]})


            elif tag == "portused":
                self.nmap_output["host"]["os"]["portused"].append({"state": attributes["state"], "proto":attributes["proto"], "portid":attributes["portid"]})

            elif tag == "osclass":
                self.nmap_output["host"]["os"]["osclass"]["type"] = attributes["type"]
                self.nmap_output["host"]["os"]["osclass"]["vendor"] = attributes["vendor"]
                self.nmap_output["host"]["os"]["osclass"]["osfamily"] = attributes["osfamily"]
                self.nmap_output["host"]["os"]["osclass"]["osgen"] = attributes["osgen"]
                self.nmap_output["host"]["os"]["osclass"]["accuracy"] = attributes["accuracy"]
                self.nmap_output["host"]["os"]["osclass"]["cpe"] = 'temp_empty'
                # find: <cpe>cpe:/o:linux:linux_kernel:2.6.39</cpe>

            elif tag == "osmatch":
                self.nmap_output["host"]["os"]["osmatch"]["name"] = attributes["name"]
                self.nmap_output["host"]["os"]["osmatch"]["accuracy"] = attributes["accuracy"]
                self.nmap_output["host"]["os"]["osmatch"]["line"] = attributes["line"]

            elif tag == "finished":
                self.nmap_output["runstats"]["finished"]["time"] = attributes["time"]
                self.nmap_output["runstats"]["finished"]["timestr"] = attributes["timestr"]
                self.nmap_output["runstats"]["finished"]["elapsed"] = attributes["elapsed"]
                self.nmap_output["runstats"]["finished"]["summary"] = attributes["summary"]
                self.nmap_output["runstats"]["finished"]["exit"] = attributes["exit"]

            elif tag == "hosts":
                self.nmap_output["runstats"][tag]["up"] = attributes["up"]
                self.nmap_output["runstats"][tag]["down"] = attributes["down"]
                self.nmap_output["runstats"][tag]["total"] = attributes["total"]


            if tag == "port":
                self.curr_portid = attributes["portid"]
                self.curr_port.update({
                    self.curr_portid: {
                        "port": {"protocol":attributes["protocol"], "portid":attributes["portid"]},
                        "state": {"state":"", "reason":"", "reason_ttl":""},
                        "service": {"name":"", "method":"", "conf":"", "tunnel":"", "product":"", "version":"", "extrainfo":"", "ostype":''}
                    }
                })
            if tag == "state":
                for attr in ["state", "reason", "reason_ttl"]:
                    try:
                        self.curr_port[self.curr_portid][tag].update({attr:attributes[attr]})
                    except:
                        self.curr_port[self.curr_portid][tag].update({attr:"None"})

            if tag == "service":
                for attr in ["name", "method", "conf", "product", "version", "ostype", "tunnel", "extrainfo"]:
                    try:
                        self.curr_port[self.curr_portid][tag].update({attr: attributes[attr]})
                    except:
                        self.curr_port[self.curr_portid][tag].update({attr:"None"})


                # try:
                #     self.curr_port[self.curr_portid][tag].update({"product":attributes["product"]})
                # except Exception as e:
                #     self.curr_port[self.curr_portid][tag].update({"product":"None"})
                #
                # try:
                #     self.curr_port[self.curr_portid][tag].update({"version":attributes["version"]})
                # except Exception as e:
                #     self.curr_port[self.curr_portid][tag].update({"version":"None"})
                #
                # try:
                #     self.curr_port[self.curr_portid][tag].update({"ostype":attributes["ostype"]})
                # except Exception as e:
                #     self.curr_port[self.curr_portid][tag].update({"ostype":"None"})
                #
                # try:
                #     self.curr_port[self.curr_portid][tag].update({"tunnel":attributes["tunnel"]})
                # except Exception as e:
                #     self.curr_port[self.curr_portid][tag].update({"tunnel":"None"})
                #
                # try:
                #     self.curr_port[self.curr_portid][tag].update({"extrainfo":attributes["extrainfo"]})
                # except Exception as e:
                #     self.curr_port[self.curr_portid][tag].update({"extrainfo":"None"})
                #

                # elif tag == "script":
                #     print("[ SCRIPT.ID     ]", attributes["id"])
                #     print("[ SCRIPT.OUTPUT ]", "".join(attributes["output"]))
                # elif tag == "uptime":
                #     self._dict_uptime.update({"seconds": attributes["seconds"], "lastboot": attributes["lastboot"]})
        except Exception as e:
            print("[ EXCEPTION ] @", tag, e)

    def endElement(self, tag):
        if tag == "ports": self.nmap_output["host"]["ports"].update(self.curr_port)

    # def characters(self, content):
    #     print("%%%%%%%%%%%%%%%%%%%%%%% >>")
    #     print(content)





if __name__ == '__main__':


    n = Nmap2Mongo()
    xml.sax.parse(open("new/budo-sV.xml"), n)
    print("DONE")
    # db(doc=n.nmap_output)
    # print("DB Done")
    print(n.nmap_output)