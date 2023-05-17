from xml.dom.minidom import parse 
import xml.dom.minidom
import openpyxl
DOMTree = xml.dom.minidom.parse("Practical14/go_obo.xml")
collection = DOMTree.documentElement

terms = collection.getElementsByTagName("term")

for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    if "autophagosome" in defstr.childNodes[0].data:
        id = term.getElementsByTagName('id')[0]
        name = term.getElementsByTagName('name')[0]
        print("GO id: %s" % id.childNodes[0].data)
        print("Term name: %s" % name.childNodes[0].data)
        print("Definition string: %s" % defstr.childNodes[0].data)

# the code to finish the second task. To aviod bugs, I input the XML again
dom = xml.dom.minidom.parse("Practical14/go_obo.xml")
terms = dom.getElementsByTagName("term")
for term in terms:
    defstr = term.getElementsByTagName("defstr")[0]
    if "autophagosome" in defstr.childNodes[0].data:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        name = term.getElementsByTagName("name")[0].childNodes[0].data
        child_nodes = len(term.getElementsByTagName("is_a"))
        print("GO id: %s" % id)
        print("Term name: %s" % name)
        print("Number of child nodes: %d" % child_nodes)
