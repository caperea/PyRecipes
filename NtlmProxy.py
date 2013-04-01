##################### Simple example ####################

import urllib2
from ntlm import HTTPNtlmAuthHandler

user = 'DOMAIN\User'
password = "Password"
url = "http://ntlmprotectedserver/securedfile.html"

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, user, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# create and install the opener
opener = urllib2.build_opener(auth_NTLM)
urllib2.install_opener(opener)

# retrieve the result
response = urllib2.urlopen(url)
print(response.read())


################## Extended Example ##################
import urllib2
from urlparse import urlparse, urlunparse
from ntlm import HTTPNtlmAuthHandler

user = 'DOMAIN\User'
password = "Password"
url = "http://ntlmprotectedserver/securedfile.html"
# determine a base_uri for which the username and password can be used
parsed_url = urlparse(self.href)
base_uri = urlunparse((parsed_url[0],parsed_url[1],"","","",""))

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, base_uri, user, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# other authentication handlers
auth_basic = urllib2.HTTPBasicAuthHandler(passman)
auth_digest = urllib2.HTTPDigestAuthHandler(passman)

# disable proxies (if you want to stay within the corporate network)
proxy_handler = urllib2.ProxyHandler({})

# create and install the opener
opener = urllib2.build_opener(proxy_handler, auth_NTLM, auth_digest, auth_basic)
urllib2.install_opener(opener)

# retrieve the result    
response = urllib2.urlopen(url)
print(response.read())
