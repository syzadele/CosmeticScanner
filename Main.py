import requests
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime import image
from test.test_email import openfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getWebPage(productName):
    

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
    return htmlSource

def getWebPageM(productName):
    
    #open Login page
    driver = webdriver.Chrome()
    driver.get("https://www.marionnaud.fr/login")
    #Check title
    assert "Login" in driver.title
    
    #Fill login and password and login
    import InfoLogin
    element = driver.find_element_by_id("j_username")
    element.send_keys(InfoLogin.MARIONNAUD_LOGIN)
    element = driver.find_element_by_id("j_password")
    element.send_keys(InfoLogin.MARIONNAUD_PW)
    element.send_keys(Keys.RETURN)
    #Fill searche bar
    element = driver.find_element_by_name("text")
    element.send_keys(productName)
    element.send_keys(Keys.RETURN)
    
    htmlSource = driver.page_source  
    return htmlSource

def getWebPageN(productName):
    
    #open Login page
    driver = webdriver.Chrome()
    driver.get("https://www.nocibe.fr/nocibe/CustomerConnection?StoreID=1&CatalogueID=1&LangueID=1")
    print(driver.title)
    #Check title
    assert "Nocibé" in driver.title
    
    #Fill login and password and login
    import InfoLogin
    element = driver.find_element_by_xpath("//div[@id='identification-user']//input[@id='email']")
    element.send_keys(InfoLogin.NOCIBE_LOGIN)
    #element = driver.find_element_by_id("email")
    element = driver.find_element_by_id("mdp1")
    element.send_keys(InfoLogin.NOCIBE_PW)
    element.send_keys(Keys.RETURN)
    #Fill searche bar
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-xs-3']/div[@class='menu-compte mb-20 mt-25']")))
    element = driver.find_element_by_id("Rechercher")
    element.click()
    element.send_keys(productName)
    element.send_keys(Keys.RETURN)
    
    htmlSource = driver.page_source  
    return htmlSource
    
def openFile(path):
    f = codecs.open(path, 'r', 'utf-8')
    #f.write(htmlSource)
    #print (htmlSource)
    sourceCode = f.read()
    f.close()
    return sourceCode

def getPrice(content):
    i = 1
    listResult = []
    soup = BeautifulSoup(content, "lxml")
    for product in soup.find_all(attrs={'class' : 'searchClassique'}, limit=6):
        libelle = product.find("p", class_="libelle").text
        price = product.find("p", class_="prix").text
        image = product.find("img", {"class":"lazy"})
        img_link = image['src']
        print(str(i) + libelle + price + str(img_link))
        listResult.insert(i,(i,img_link,libelle,price))
        i = i+1
    return listResult

def getPriceM(content):
    i=1
    listResult = []
    soup = BeautifulSoup(content,"lxml")
    for product in soup.find_all(attrs={'class' : 'col-lg-3 col-md-3 col-sm-4'}, limit=6):
        libelle = product.find("div", class_="product_name").text
        price = product.find("div", class_="price").text
        image = product.find("div", {"class":"product_img"})
        img_link = image.img['src']
        listResult.insert(i,(i,img_link,libelle,price))
        i=i+1
    return listResult

def getPriceN(content):
    i=1
    listResult = []
    soup = BeautifulSoup(content,"lxml")
    for product in soup.find_all(attrs={"class": "pl_produit pl_produit--lowline col-xs-3"}, limit=6):
        libelle = product.find("div", class_="pl_accroche").text
        price = product.find("div", class_="pl_prix").text
        image = product.find("div", class_="pl_image")
        img_link = image.a.img['src']
        listResult.insert(i,(i,img_link,libelle,price))
        i=i+1
    return listResult


