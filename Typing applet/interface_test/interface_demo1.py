import requests



def test5():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }

    resp = requests.get("http://www.fanyunedu.com:5000", headers=headers)

    # resp = requests.get("http://httpbin.org/headers") # 这个网站是可以拿到请求回来的信息作为返回值
    print(resp.text)

def test6():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Cookie":"JSESSIONID=3F745928E7C11E31DE128369F1BF7C38"
    }

    resp = requests.get("http://120.76.206.144:8080/mms/Login/GetLoginName", headers=headers)
    print(resp.text)

def test7():
    sess = requests.Session() # 创建一个session会话，保存客户端的会话信息

    data = {
        "username": "admin",
        "password": "123"
    }

    sess.post("http://120.76.206.144:8080/mms/Login/loginUser", data=data)
    resp = sess.get("http://120.76.206.144:8080/mms/Login/GetLoginName")
    print(resp.text)




if __name__ == '__main__':
    test7()