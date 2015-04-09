"""
This script is to be run after using Datajetway to tranform the UN PDF files
into DRXML
"""
from lxml import etree
import os
IN_DIR = '/path/to/datajetway/output'
OUT_DIR = '/path/for/this/to/output/to'
UN_URL = "http://www.un.org/News/dh/pdf/english/"

for file in os.listdir(IN_DIR):
    tree = etree.ElementTree()
    root = tree.parse(os.path.join(IN_DIR,file))
    message = root.find('message')
    name = message.get('name')
    print "Enhancing {0}".format(name)
    date = name.split('.')[0]
    (month,day,year) = date.split('-')
    source = "{3}{0}/{1}{2}{0}.pdf".format(year,day,month,UN_URL)
    message.set('sourceId',source)
    doc_date = message.get('documentDate')
    tail = doc_date.split('T')[1]
    new_doc_date = "{0}-{1}-{2}T{3}".format(year,month,day,tail)
    message.set('documentDate',new_doc_date)
    message.set('lastModifiedDate',new_doc_date)
    with open(os.path.join(OUT_DIR,message.get('name')), 'w') as f:
        tree.write(f,pretty_print=True,encoding="UTF-8",standalone=True)
