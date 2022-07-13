from appium import webdriver
import time

desired_cap = {}

# 必须参数，定义被测脚本的平台属性.android.ios
desired_cap["platformName"] = "android"
# 必须参数，定义被测手机的安卓手机版本号(大版本不能错，小版本可以不写)
desired_cap["platformVersion"] = "6.0.1"
# 可以写任意的值，但不能为空
desired_cap["deviceName"] = "127.0.0.1:7555"
# 必须参数，指定被测软件的包名
desired_cap["appPackage"] = "mobi.appplus.calculator.plus"
# 必须参数，指定要打开的app的页面是哪个？
desired_cap["appActivity"] = "appplus.mobi.calcflat.MainActivity"
# 不是必须的，但一般需要指定
desired_cap["automationName"] = "Uiautomator2"
# 设置App的重置策略
desired_cap["noReset"] = True
# 设置命令的超时时间
desired_cap["newCommandTimeout"] = 6000
# 用于设置中文输入
desired_cap["unicodeKeyboard"] = True
desired_cap["resetKeyboard"] = True


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

driver.find_element("id", "mobi.appplus.calculator.plus:id/btn1").click()
driver.find_element("id", "mobi.appplus.calculator.plus:id/btnAdd").click()
driver.find_element("id", "mobi.appplus.calculator.plus:id/btn2").click()
driver.find_element("id", "mobi.appplus.calculator.plus:id/btnEqual").click()
time.sleep(1)
a = driver.find_element("xpath", "//android.widget.TextView[@bounds='[444,40][470,70]']").text
print(a)






