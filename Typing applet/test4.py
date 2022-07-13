from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fwww.aliyun.com%2F")
driver.maximize_window()

# 判断有登录文字
login_btn = driver.find_element("xpath", "//div[@class='tabs-item active']/div[@class='tabs-item-text']")
if "账号" in login_btn.text:
    login_btn.click()
else:
    login_btn = driver.find_element("xpath", "//div[@class='tabs-item ']/div[@class='tabs-item-text']")
    login_btn.click()


driver.find_element("xpath", "//*[@id='login-form']/div[6]/button").click()

time.sleep(2)


result = driver.find_element("//*[@id='login-error']/div")
print(result)
