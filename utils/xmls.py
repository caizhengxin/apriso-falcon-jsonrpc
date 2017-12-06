# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-12-05 14:39:33
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-05 16:21:01
import xml.dom.minidom as Dom


class XMLparse(object):
    def __init__(self, text=''):
        self.doc = text
        if isinstance(text, str):
            self.doc = Dom.parseString(text)

    def getTagName(self, value=''):
        if not value:
            value = 'root'

        _d = self.doc.getElementsByTagName(value)

        for v in _d:
            yield XMLparse(v)

    @property
    def getchildNodes(self):
        for v in self.doc.childNodes:
            if v.nodeType == v.ELEMENT_NODE:
                yield XMLparse(v)

    @property
    def getNodeName(self):
        return self.doc.nodeName

    @property
    def getNodeValue(self):
        node = self.doc.childNodes
        return '' if not node else node[0].data

    def getNodeAttr(self, attr):
        return self.doc.getAttribute(attr)


def parse_xml(text=''):
    item_list = []
    vitem = []
    keys = []
    doc = XMLparse(text)
    for pitem in doc.getTagName('PropertyBagItem'):
        key = pitem.getNodeAttr('Key')
        keys.append(key)
        for v in pitem.getTagName('Value'):
            vList = [n.getNodeValue for n in v.getchildNodes]
            vitem.append(vList)

    for i in range(len(vitem[0])):
        items = {}
        for j in range(len(vitem)):
            items[keys[j]] = vitem[j][i]
        item_list.append(items)
    return item_list


if __name__ == '__main__':
    pass
