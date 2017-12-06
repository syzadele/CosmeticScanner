from selenium import webdriver
from selenium.webdriver.common.keys import Keys

productName = "Shiseido mousse nettoyant"

# Open Login page
driver = webdriver.Chrome()
driver.get("https://www.sephora.fr/secure/user/login.jsp")
# Check title
assert "Sephora" in driver.title

# Fill login and password and login
import InfoLogin
element = driver.find_element_by_id("cmail")
element.send_keys(InfoLogin.SEPHORA_LOGIN)
element = driver.find_element_by_id("cpasse")
element.send_keys(InfoLogin.SEPHORA_PW)
element.send_keys(Keys.RETURN)
# Fill searche bar
element = driver.find_element_by_id("champRecherche")
element.send_keys(productName)
element.send_keys(Keys.RETURN)

htmlSource = (driver.page_source).encode('utf-8')
print (htmlSource)
