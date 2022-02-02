from selenium import webdriver
#traemos el driver de chrome
driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
#traemos una direccion
driver.get("http://www.gacetaoficialdebolivia.gob.bo/")
# driver.close()