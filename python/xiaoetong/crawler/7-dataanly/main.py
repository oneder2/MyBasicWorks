"""
https://www.so.com/

(1)anti-crawler method:
    issue: web deny requests from crawler
    1. infinate_debugger: skip the debug command
    2. asynchronous loading: 

(2)string replace
    issue: some reaction have unexpected format such s = "qwert123456789_23456789({});", yet we just want to have "{}"
    1.string replace:
        example code: 
            s.replace("qwert123456789_23456789(", "").replace("})", "") 
        replace the left & right frame to empty respectively

    2.regular expression extract:
        example code: 
            /* - import re - */
            ls = re.findall('qwert123456789_23456789\((.*?)\)', s) 
            # or more flexiable
            ls = re.findall('qwert\d+_\d+\((.*?)\)', s)
        notice that if there is "(" ")" in string, "\" is required.
"""
#import re
#s = 'qwert123456789_23456789({});'
#ls = re.findall('qwert\d+_\d+\((.*?)\);', s)
#print(ls)


import requests
import re


myurl = "https://image.so.com/"

res = requests.get(url = myurl)
print(res.text)

#print(ls[0])

