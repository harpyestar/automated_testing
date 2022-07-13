from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome()

# driver.get("http://120.76.206.144:8080/mms/login.html")

# driver.find_element("id", "username").send_keys("admin")
# driver.find_element("xpath", "/html/body/div[1]/div[1]/div/input").click()
#
# # time.sleep(5)
#
# # driver.implicitly_wait(5)
#
# WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element(
#         ("xpath", "/html/body/div[3]/div[2]/div[1]"),
#         "password不能为空")
# )
#
# result = driver.find_element("xpath", "/html/body/div[3]/div[2]/div[1]")
# print(result.text)

# driver.find_element("id", "username").send_keys("admin")
#
# name = driver.find_element("id", "username").get_attribute("placeholder")
# print(name)

# def fun4():
#     driver.get("https://www.baidu.com/")
#     driver.find_element("id","kw").send_keys(Keys.SHIFT, "false")

# def fun5():
#     driver.get("https://www.baidu.com/")
#     driver.find_element("id","kw").send_keys("false"*2)
#     driver.find_element("id", "kw").send_keys(Keys.CONTROL + 'a')
#     driver.find_element("id", "kw").send_keys(Keys.CONTROL+'c')
#     driver.find_element("id", "kw")
#     driver.find_element("id", "kw").send_keys(Keys.CONTROL + 'v')

def func6():
    driver.get(r"D:\Typing applet\下拉框.html")
    # Select(driver.find_element("tag name", "select")).select_by_index(1)
    # Select(driver.find_element("tag name", "select")).select_by_value("audi")
    Select(driver.find_element("tag name", "select")).select_by_visible_text("Audi")


if __name__ == '__main__':
    func6()