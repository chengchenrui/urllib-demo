# -*- coding:utf-8 -*-
import urllib2
import re

page = 2
url = 'http://www.qiushibaike.com/hot/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?'
                         '<div.*?content">(.*?)</div>(.*?)'
                         '<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print item[0], item[1], item[3]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
