from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://deliverind.com.ar/consulta-tu-pedido/")
element1 = driver.find_element_by_css_selector("#orderid")
element1.send_keys("129062")
element2 = driver.find_element_by_css_selector("#order_email")
element2.send_keys("gastonvecch@gmail.com")
element3 = driver.find_element_by_css_selector("body > div.container-fluid > div > div > div > div > div > form > p:nth-child(5) > button")
element3.click()
