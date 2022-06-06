#!/usr/bin/env python3

from lxml import etree
import sys

config_path1 = r"C:\Users\swaroop.diwakar\Documents\Altiostar\EMS OSS\v133_schema\MACRO\v133_AC\MACRO_v133_asn_config.xml"


def sort_config(config_path1):
    config_path = config_path1.replace('\\', '/')
    savepath = 'C:' + config_path[config_path.find('C:') + len('C:'):config_path.rfind('.xml')] + '_sorted.xml'
    data1 = open(config_path, 'r')
    sorted_file = open(savepath, 'w')
    data = data1.read()
    root = etree.parse(config_path)
    # Remove namespace prefixes
    for elem in root.getiterator():
        elem.tag = etree.QName(elem).localname
    # Remove unused namespace declarations
    etree.cleanup_namespaces(root)
    print(etree.tostring(root).decode())
    data = etree.tostring(root)
    doc = etree.XML(data, etree.XMLParser(remove_blank_text=True))

    for parent in doc.xpath('//*[./*]'):  # Search for parent elements
        parent[:] = sorted(parent, key=lambda x: x.tag)

    print(etree.tostring(doc, pretty_print=True))
    etc = str(etree.tostring(doc, pretty_print=True))
    etc1 = etc.replace(r'\n', '\n')
    etc1 = etc1.replace("b'",'')
    etc1 = etc1.replace(">\n'",'>')
    print(etc1)
    sorted_file.write(etc1)
    sorted_file.close()


sort_config(config_path1)
