import random

import random
import base64


iplists=[
'222.75.208.166:28510',
'222.78.253.68:57812',
'115.220.147.209:808',
'113.231.186.60:17813',
'220.161.120.42:56301',
'175.155.209.175:59735',
'115.220.151.173:808',
'119.5.36.131:808',
'171.13.36.207:808',
'115.220.148.164:808',
'175.155.25.36:808',
'171.111.158.113:808',
'60.189.143.82:808',
'183.46.219.210:19420',
'202.121.96.33:8086',
'175.155.25.53:808',
'175.155.24.22:808',
'121.25.72.255:59843',
'111.76.129.212:808',
'115.29.2.139:80',
'221.216.94.77:808',
'139.196.105.154:9000',
'111.76.129.204:808',
'183.130.85.10:10407',
'221.229.47.221:808',
'175.155.25.51:808',
'114.239.145.210:808',
'59.63.123.184:808',
'111.76.129.220:808',
'182.35.127.68:808',
'175.155.25.14:808',
'119.5.0.9:808',
'1.48.65.187:46604',
'183.135.255.24:31162',
'115.215.71.143:808',
'101.53.101.172:9999',
'114.239.1.36:808',
'113.123.78.111:808',
'182.87.68.149:808',
'222.169.138.134:8998',
'111.72.127.19:808',
'111.76.133.21:808',
'111.76.129.104:808',
'125.89.120.192:808',
'115.220.147.140:808',
'123.169.91.3:808',
'111.76.129.40:808',
'111.76.129.64:808',
'59.63.123.27:808',
'125.89.122.249:808',
'222.85.50.88:33960',
'119.5.1.43:808',
'175.155.25.12:808',
'115.220.148.209:808',
'121.226.166.114:808',
'121.226.5.93:808',
'111.76.133.94:808',
'113.121.254.164:808',
'111.76.129.123:808',
'60.178.84.167:808',
'111.76.133.117:808',
'121.61.109.185:808',
'115.220.2.171:808',
'123.163.162.207:25549',
'115.220.0.142:808',
'27.153.128.155:45905',
'59.63.123.17:808',
'115.220.147.60:808',
'115.220.5.241:808',
'175.155.25.48:808',
'115.192.58.196:8118',
'175.155.24.43:808',
'119.5.1.22:808',
'110.246.149.199:41395',
'221.238.67.231:8081',
'59.58.211.49:20436',
'125.89.122.227:808',
'171.13.36.34:808',
'115.215.68.106:808',
'114.239.147.99:808',
'111.76.129.81:808',
'113.58.234.49:808',
'114.239.3.249:808',
'122.241.195.215:808',
'115.220.6.178:808',
'121.61.102.110:808',
'175.155.25.55:808',
'60.178.87.116:808',
'112.82.232.93:808',
'171.13.36.86:808',
'221.229.47.85:808',
'115.220.151.237:808',
'175.155.24.80:808',
'222.94.147.52:808',
'122.228.179.178:80',
'111.76.129.52:808',
'111.76.129.88:808',
'183.32.88.23:808',
'115.220.5.198:808',
'111.72.127.169:808',

]


class ProxyMiddleware(object):
    def process_request(self,request,spider):
        proxy = random.choice(iplists)
        # if 'proxy' in request.meta:
        #    return
        request.meta['http_proxy'] = 'http://{}'.format(proxy)

        #request.meta['proxy'] = "http://{}:{}".format('124.88.67.24', '843')
        #proxy_user_pass = "1:2"
    # setup basic authentication for the proxy
        #encoded_user_pass = base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        #print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))