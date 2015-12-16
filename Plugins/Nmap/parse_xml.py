__author__ = 'N05F3R4TU'
from xml.dom.minidom import Document
import xml.sax

class NmapXMLParser(xml.sax.ContentHandler):
    """
    This Object Parse an Nmap XML Output file
    """
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attr):
        print("start element '"+name+"'")
    def endElement(self, name):
        print("end element: '"+name+"'")
    def characters(self, content):
        print("{}{}".format("characters:", content))

    def read(self):
        pass
    def parse(self):
        pass
    def wright(self):
        pass

def main(xml_file):
    source = open(xml_file)
    xml.sax.parse(source, NmapXMLParser())

# class CreateXML(Document):
#     """
#     This Object is to Create XML Files
#     """
#     def __init__(self, filename):
#         super(CreateXML, self).__init__()
#         self.doc = Document()
#         self.name = "XML Create Object"
#         self.filename = "%s.xml" % filename
#
#     def create_node(self, name):
#         return self.doc.createElement(tagName=name)
#     def append_node(self, node, to_node):
#         return to_node.appenChild(node)
#     def create_text_node(self, text):
#         return self.doc.createTextNode(text)
#     def wright_xml(self):
#         with open(self.filename, mode="rw+") as xml:
#             xml.write(self.doc.toprettyxml(indent="    "))

if __name__ == '__main__':
    # parse = NmapXMLParser()
    # file = open("file-output3.xml")
    # xml.sax.parse(file, NmapXMLParser())
    # main("file-output3.xml")
    xml.sax.parse(open("file-output3.xml"), NmapXMLParser())