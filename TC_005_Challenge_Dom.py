from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elementos.elementos import enlace
from elementos.funciones import click, esperar

#iniciar driver

driver = webdriver.Chrome()
driver.get(enlace)
driver.maximize_window()

#Esperamos que cargue al enlace requerido

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > ul > li:nth-child(5) > a')))

#accedemos al enlace
challenging_dom_link = driver.find_element(By.CSS_SELECTOR,'#content > ul > li:nth-child(5) > a')
click(challenging_dom_link)
esperar(1)
#luego generamos las pruebas para este site

#tomamos el valor del elemento Answer que conmuta cada vez que el boton es clicked

WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CLASS_NAME,'button')))
boton_azul = driver.find_element(By.CLASS_NAME,'button')
boton_rojo = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/a[2]')
boton_verde = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/a[3]')
print('debajo de mi viene el text del boton azul')
print(boton_azul.text)
print(boton_rojo.text)
print(boton_verde.text)
boton_azul.click()
esperar(3)
boton_azul_after_click = driver.find_element(By.CLASS_NAME,'button')
boton_rojo_after_click= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/a[2]')
boton_verde_after_click= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/a[3]')
print("soy el boton despues del click")
print(boton_azul_after_click.text)
print(boton_rojo_after_click.text)
print(boton_verde_after_click.text)
assert boton_verde != boton_verde_after_click and boton_azul != boton_azul_after_click and boton_rojo != boton_rojo_after_click , 'prueba fallo'


