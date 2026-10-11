import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdrivermanager_cn.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 实例化options操作对象
options = Options()
# 添加 experimental_option，禁用自动化扩展，防止被检测到使用了自动化工具进行操作
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 添加 argument，禁用浏览器自动化特性，防止被检测到使用了自动化工具进行操作
options.add_argument("--disable-blink-features=AutomationControlled")
# 添加 argument，忽略证书错误，防止因证书错误导致的访问失败
options.add_argument("ignore-certificate-errors")

server = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=server)
driver.get("https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=265518063&clazzid=154662454&cpi=493036953&enc=679ce3ff0a9f59d2bec6db8729e68378&t=1790952135288&pageHeader=1&v=2&hideHead=0")

#完成登录
phone = driver.find_element(By.XPATH, "//input[@placeholder='手机号/超星号']")
phone.send_keys("13207412205")
password = driver.find_element(By.XPATH, "//input[@placeholder='学习通密码']")
password.send_keys("Sunshine.#246/")
button = driver.find_element(By.ID, "loginBtn")
button.click()
time.sleep(1)

