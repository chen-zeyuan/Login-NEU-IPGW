from urllib import request

def login_ipgw (username, password):
    textmod="action=login&username="+username+"&password="+password+"&ac_id=3&user_ip=&nas_ip=&user_mac=&url=&save_me=&ajax=1"
    textmod=textmod.encode()
    print(textmod)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/text"}
    url='http://ipgw.neu.edu.cn/include/auth_action.php'
    req = request.Request(method="POST", url=url, data=textmod, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    print("登录结果："+res.decode())



# 你的学号
username=""

# 改为你的密码
password=""

login_ipgw(username, password)
