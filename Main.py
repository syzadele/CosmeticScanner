import requests
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getWebpage():
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

def openFile(path):
    f = codecs.open(path, 'r', 'utf-8')
    #f.write(htmlSource)
    #print (htmlSource)
    sourceCode = f.read()
    f.close()
    return sourceCode

def getPrice(content):
    i = 1
    soup = BeautifulSoup(content, "lxml")
    for product in soup.find_all(attrs={'class' : 'searchClassique'}):
        libelle = product.find("p", class_="libelle").text
        price = product.find("p", class_="prix").text
        print(str(i) + libelle + price)
        i = i+1

def main():
    getPrice(openFile("sourceCode.html"))
if __name__ == "__main__": main()
