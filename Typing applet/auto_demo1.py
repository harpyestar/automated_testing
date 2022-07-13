from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

def AliyunChoose():
    driver.get("https://www.aliyun.com/")
    driver.maximize_window()
    link = driver.find_element("partial link text", "登录").get_attribute("href")
    # driver.find_element("partial link text", "登录").click()
    driver.get(link)
    driver.maximize_window()

    # 判断有登录文字
    login_btn = driver.find_element("xpath", "//div[@class='tabs-item active']/div[@class='tabs-item-text']")
    if "账号" in login_btn.text:
        login_btn.click()
    else:
        login_btn = driver.find_element("xpath", "//div[@class='tabs-item ']/div[@class='tabs-item-text']")
        login_btn.click()

    # ---- 模拟登录 -----
    driver.implicitly_wait(3)
    # time.sleep(2)

    # WebDriverWait(driver, 5).until(
    #     EC.text_to_be_present_in_element(
    #         ("xpath", "/html/body/div[3]/div[2]/div[1]"),
    #         "password不能为空")
    # )

    # ---- 切换成iframe---
    driver.switch_to.frame(driver.find_element("id", "alibaba-login-box"))

    driver.find_element("id", "fm-login-id").send_keys("harpyestar")
    driver.find_element("id", "fm-login-password").send_keys("guanggao521")

    time.sleep(5) # 手动拖动条
    # ---- 滑动条
    ele_button = driver.find_element("id", "nc_1_n1z") # 滑动块
    # ele = driver.find_element("id", "nc_1__scale_text") # 滑动条
    ele = driver.find_element("xpath", "//div[@id='nc_1__scale_text']/span")  # 滑动条
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop_by_offset(ele_button, ele.size['width'], ele.size['height']).perform()



    driver.find_element("tag name", "button").click()

    # driver.implicitly_wait(3)
    WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable(("id", "J_GetCode"))
        EC.visibility_of_element_located(("id", "J_GetCode"))
    )


    # time.sleep(5)

    driver.find_element("id", "J_GetCode").click()

    time.sleep(15)  # 手机验证码

    driver.find_element("id", "btn-submit").click()



if __name__ == '__main__':
    AliyunChoose()