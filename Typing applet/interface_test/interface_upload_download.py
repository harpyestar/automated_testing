import requests


def test_file():
    """
    上传文件不带参数
    :return:
    """
    files = {
        "file": open("testxxxx.txt", "rb")
    }
    resp = requests.post("http://www.fanyunedu.com:5000/general/api/upload", files=files)
    print(resp.text)

def test_file2():
    """
        上传带参数的文件
    :return:
    """
    data = {
        "batchname":"GB0210707"
    }
    files = {
        "batchfile":"XXX.xls"
    }
    resp = requests.post("XXX", data=data, files=files)
    print(resp.text)

def test_download():
    resp = requests.get("http://120.76.206.144:8080/mms/mms/images/back.png")

    with open("pic.png", "wb") as f:
        f.write(resp.content)

def test_security_interface():
    """
        加密接口进行请求
    :return:
    """
    uid, username, password, salt = '30', 'fanyunedu', '1234', 'yi1ROS5U8KZdMsNP'
    import hashlib
    hl = hashlib.md5()
    hl.update("{}-{}-{}-{}".format())


if __name__ == '__main__':
    test_download()
