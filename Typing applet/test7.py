from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

def func1():
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    set = driver.find_element("id", "s-usersetting-top")
    ac = ActionChains(driver)
    ac.move_to_element(set).perform()

    driver.find_element("link text", "高级搜索").click()

def func2():
    driver.get("https://www.baidu.com/")
    driver.find_element("id", "kw").send_keys("py")
    meaus = driver.find_elements("class name", "bdsug-overflow")
    # for meau in meaus:
    #     print(meau.text)
    # print(meaus[1].text)
    print(len(meaus))

def func3():
    driver.get("https://www.qq.com/")
    item = driver.find_element("class name","more-txt")
    ActionChains(driver).move_to_element(item).perform()
    driver.find_element("link text", "育儿").click()



if __name__ == '__main__':
    func2()
