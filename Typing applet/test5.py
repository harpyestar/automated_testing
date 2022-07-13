from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.runoob.com/")
# driver.maximize_window()

# for i in range(14):
#     driver.execute_script("window.scrollTo({},{})".format(300*i,300*(i+1)))
#     time.sleep(0.1)



# for i in range(1,11+1):
#     driver.find_element("xpath", "//[@class=codelist codelist-desktop cate{}/]".format(i))

# result = driver.find_elements("class name", "item-top item-1")
result = driver.find_element("partial link text", "HTML")

print(result.text)

# print(len(result))
