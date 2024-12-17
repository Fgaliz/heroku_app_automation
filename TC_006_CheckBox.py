from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elementos.funciones import click, esperar
from elementos.elementos import enlace

#iniciamos el driver
driver = webdriver.Chrome()
driver.get(enlace)
driver.maximize_window()

#esperamos  que cargue el elemento a seleccionar

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > ul > li:nth-child(6) > a')))

#sleecionamos el elemento y accedemos al enlace

checkbox_enlace = driver.find_element(By.CSS_SELECTOR,'#content > ul > li:nth-child(6) > a')
click(checkbox_enlace)
#esperamos que cargue los checkboxes
WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#checkboxes > input[type=checkbox]:nth-child(1)')))
checkbox_1_elemento = driver.find_element(By.CSS_SELECTOR,'#checkboxes > input[type=checkbox]:nth-child(1)')
checkbox_1_elemento_before_click = checkbox_1_elemento.is_selected()
checkbox_2_elemento = driver.find_element(By.CSS_SELECTOR,'#checkboxes > input[type=checkbox]:nth-child(3)')
checkbox_2_elemento_before_click = checkbox_2_elemento.is_selected()
print(checkbox_1_elemento_before_click)
print(checkbox_2_elemento_before_click)
click(checkbox_1_elemento)
click(checkbox_2_elemento)
checkbox_1_elemento_after_click = checkbox_1_elemento.is_selected()
checkbox_2_elemento_after_click = checkbox_2_elemento.is_selected()
assert checkbox_1_elemento_before_click != checkbox_1_elemento_after_click and checkbox_2_elemento_before_click != checkbox_2_elemento_after_click, 'prueba fallo'
esperar(2)



