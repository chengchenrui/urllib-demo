import urllib
import urllib2

values = {"username":"chengchenrui","password":"XXXXXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)

print response.read()