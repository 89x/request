# coding:utf-8
import requests
import json
url1="http://www.cmall.com/memberSite/sso/loginJson"
data1 = {"loginAccount":"苏小谢","password":"xiehengda"}
url="https://www.cmall.com/goodsSite/agentAccount/queryAgentAccountInfo"
data= {'phoneNo': '18697980508'}
url2="https://m.taidu.com/orderPaySite/tude/cart/getCartCount"
cookie = {'User_code': '0', 'User_id': '320187', 'enshrines_key': '0', 'iconUrl': '"http://image.cmall.com/imgsrv/diyrelease/cmall/o_1c53u81ja2mh56d10o0s3vavn9.png"', 'location': '""', 'loginAccount': '%E8%8B%8F%E5%B0%8F%E8%B0%A2', 'mchRoles': '0', 'nickName': '%E8%8B%8F%E5%B0%8F%E8%B0%A2', 'regional': 'CN', 'roleId': '2', 'toKen': 'cb2beaff01522b32fa5164b7e97', 'JSESSIONID': 'FFC1F2880C974BC2780826BD3BA7277B'}
re= requests.get(url1,data1)
res= re.cookies
print(res)
sa = requests.utils.dict_from_cookiejar(res)
print(sa)
res1= requests.post(url2,cookies=sa)
print(res1.text)