__author__ = 'N05F3R4TU'
__all__ = ["SpiderData"]

from pymongo import MongoClient

mongo = MongoClient("localhost", port=27017, connect=True)
db = mongo["nimbus"]["targets"]


class SpiderData:
    """
    Spider Database Connection per Session
    """

    def __init__(self):
        self.name = "Crawler Database Connection"
        self.object_id = ""
        self.target_ip = ""
        self.target_name = ""
        self.target_url = ""
        self.target_state = ""
        self.target_note = ""

        # save to
        self.save_to_database = True
        self.save_to_file = True

        # notify
        self.notify_by_email = True
        self.notify_by_slack = True
        self.notify_by_hipchat = True


    def __str__(self):
        return str(self.__dict__)

    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
        return self

    def dump_to_file(self, x):
        from time import sleep
        import os

        print("Dumping Session To File ... one moment please")
        sleep(2)

        sess_path = "Sessions/Crawler/"
        full_path = os.path.dirname(os.path.realpath(__file__))


        # with open("{}/dumpfile.txt".format(full_path), mode="w+") as dumpfile:
        with open("{}{}.txt".format(sess_path, str(self.convert_ip_to_decimal(ip=self.target_ip))), mode="w+") as dumpfile:

            for link in x:
                dumpfile.write("{}\n".format(link))

            print("Done! Dumped!")

    def get_ip_by_url(self, url):
        import socket
        self.target_ip = socket.gethostbyname(url)

    def convert_ip_to_decimal(self, ip):
        from Plugins.IPConversion.controller import ip_to_int
        dec = ip_to_int(ip=ip)
        return dec

    def save(self):
        # first find target-document and add crawler-section to document
        print(db.find_one_and_update({"target_id":"1124545334"},
                                     {"$set": {"crawler": [
                                         {"12-456-789-00" : {"_id": "Object(decimal)","url": { "full":"http://www.fullurl.com", "base":"", "scheme":"http", "netloc":"www.url.com", "path":"/%7Eguido/Python.html", "params":"", "query":"", "fragment":"" },"geo": {"latitude": "43.2344", "longitude": "4.2342", "country": ["nl", "Netherlands"], "city": "Rotterdam"},"charset": "utf-8","banner_grab": "base64(w3rf34t543gf35yt45hg34gwf34g5-45gr4e-434g343g34+g334gewf3)","robots": {"state": True, "file": "base64(w3rf34t543gf35yt45hg34gwf34g5)"},"session": "session_id","cookie": "cookie_id","php": {"state": True, "version": "5.4"},"sitemap": {"state": True, "url": "url_sitemap.xml"},"cms_discovery": {"is_wordpress": {"state": True, "version": "4.2.3", "theme":"", "plugin":["plugin1", "plugin2", " etc... "]}},"links": [{"url": "http://www.example.com", "tag": ["has_form", "has_dork", "is_redirect"]},{"url": "http://www.example.com", "tag": ["has_form", "has_dork", "is_redirect"]},{"url": "http://www.example.com", "tag": ["has_form", "has_dork", "is_redirect"]}]}}
                                                           ]
                                               }
                                      }
                                     )
              )