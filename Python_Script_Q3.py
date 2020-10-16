#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.dom.minidom import *
import re

blocklist = parse('blocklist.xml')

elements = blocklist.documentElement

item_list = elements.getElementsByTagName('emItem')

print('All the text lines with the “blockID” values that start with the letter “i” or “g”, and end with digits:')
for item in item_list:
    attr = item.getAttribute('blockID')
    ID = item.getAttribute('id')
    if (attr[0]=='i' or attr[0]=='g') and (attr[-1].isdigit()):
        print('blockID="%s" id="%s"'%(attr, ID))

print('\n'*5)
print('All the text lines where the “ID” values are email addresses:')       
for item in item_list:
    attr = item.getAttribute('blockID')
    ID = item.getAttribute('id')
    if re.match(r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$',ID):
        print('blockID="%s" id="%s"'%(attr, ID))