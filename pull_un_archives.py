"""
This python script is used for retrieving all the UN news archives in a given
date range.
"""

from datetime import date, timedelta as td
import os
import urllib2


DIR = os.path.dirname(os.path.realpath(__file__))
UN_URL = "http://www.un.org/News/dh/pdf/english/"

#Set the date range
d1 = date(2005,1,1)
d2 = date(2015,1,16)

delta = d2 - d1
cur_dir = str(2000)
for i in range(delta.days + 1):
    tmp = d1 + td(days=i)
    f = tmp.strftime("%d%m%Y")
    curl_str = UN_URL+str(tmp.year)+"/"+f+".pdf"
    if not str(tmp.year) == cur_dir:
        cur_dir = str(tmp.year)
        os.mkdir(os.path.join(DIR,cur_dir))
    o = tmp.strftime("%m-%d-%Y.pdf")
    try:
        response = urllib2.urlopen(curl_str)
        if response.code == 200:
            with open(os.path.join(DIR,os.path.join(cur_dir,o)),'w') as f:
                f.write(response.read())
        else:
            print "FAILED: {0} on {1}".format(response.code, curl_str)
    except:
        print "FAILED: {0}".format(curl_str)