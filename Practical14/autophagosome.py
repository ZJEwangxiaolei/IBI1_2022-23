from xml.dom.minidom import parse 
import xml.dom.minidom
import openpyxl
import pandas as pd 
DOMTree = xml.dom.minidom.parse("Practical14/go_obo.xml")
collection = DOMTree.documentElement

terms = collection.getElementsByTagName("term")
data = []
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    if "autophagosome" in defstr.childNodes[0].data:
        id = term.getElementsByTagName('id')[0]
        name = term.getElementsByTagName('name')[0]
        child_nodes = len(term.getElementsByTagName("is_a"))
        data.append([id.childNodes[0].data, name.childNodes[0].data, child_nodes])
df = pd.DataFrame(data, columns=["GO id", "Term name", "Number of child nodes"])
df.to_excel("output.xlsx", index=False)
