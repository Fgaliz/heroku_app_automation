
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elementos.elementos import enlace, basic_auth_element, basic_auth_enlace

#inicializamos el driver

driver = webdriver.Chrome()
driver.maximize_window()

#vamos al landing page

driver.get(enlace)

#esperamos por el enlace a validar

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,basic_auth_element)))



#aca enviammos user y password directamente al modal

driver.get(basic_auth_enlace)

#validamos el ingredo

WebDriverWait(driver,2).until(EC.text_to_be_present_in_element((By.TAG_NAME,'p'),('Congratulations! You must have the proper credentials.')))

basic_auth_text = driver.find_element(By.TAG_NAME,'p')

assert basic_auth_text.text ==  'Congratulations! You must have the proper credentials.','fallo la prueba de basic auth'

driver.quit()
