import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    attributes = len(node.attrib)
    for child in node.getchildren():
        attributes += get_attr_number(child)
    return attributes

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
