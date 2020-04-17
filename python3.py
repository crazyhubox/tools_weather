#!/usr/local/bin/python3
# encoding:utf-8
import requests
import json
import re,json,random

prog = re.compile(r'[0-9]+')
test = 'hzh19981019130e2db9852010eesdasxzc'
a = prog.search(test,20)[0]
print(a)
