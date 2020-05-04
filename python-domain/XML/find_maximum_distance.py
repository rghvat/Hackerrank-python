import xml.etree.ElementTree as etree

maxdepth = 0
def depth(ele, level):
    global maxdepth
    maxdepth = max(maxdepth, level+1)
    # your code goes here
    for child in ele.getchildren():
        depth(child, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
