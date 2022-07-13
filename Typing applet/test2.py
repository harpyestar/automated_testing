from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://blog.csdn.net/Q0717168/article/details/109839985")


# name = driver.find_element("xpath", "//div[@id='content_views']/p[18]")
# name = driver.find_element("xpath", "//*[@id='content_views']/p[18]")

print(name.text)


