
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elementos.elementos import enlace, add_element_selector, add_element_btn_selector, delete_btn_selector
from elementos.funciones import click


#inicianilizamos el driver

driver = webdriver.Chrome()

#cargamos el enlace principal

driver.get(enlace)

#esperamos por elemento a ser cargado en la pagina

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,add_element_selector)))

#seleccionamos en enlace a ralizar click

add_element_link = driver.find_element(By.CSS_SELECTOR,add_element_selector)

#hacemos click en el enlace

click(add_element_link)

#esperamos por elementos cargados en el DOM
WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,add_element_btn_selector)))

#tomamos el selector del elemento
add_element_btn = driver.find_element(By.CSS_SELECTOR,add_element_btn_selector)

#hacemos click en el boton
click(add_element_btn)

#esperammmos por element de delete btn sea clickable

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,delete_btn_selector)))

#tomamos el selector del delete btn

delete_btn = driver.find_element(By.CSS_SELECTOR,delete_btn_selector)

#primera prueba asercion de la aparicion del delete btn

assert delete_btn.text == 'Delete','Test de boton de delete fallo'


click(delete_btn)

assert WebDriverWait(driver,2).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,delete_btn_selector))),'fallo la prueba de eliminar el delete btn'

driver.quit()