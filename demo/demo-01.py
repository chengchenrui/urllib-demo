import urllib2

respones = urllib2.urlopen("http://www.baidu.com")
print respones.read()