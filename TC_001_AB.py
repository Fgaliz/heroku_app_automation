
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elementos.elementos import enlace, a_b_testing_selector
from elementos.funciones import click, esperar

# se declara e inicializa el webdrive y vamos al primer enlace

driver = webdriver.Chrome()
driver.get(enlace)
driver.maximize_window()

# esperamos que los elementos de la pagina esten presentes (en nuestro caso sera el enlace de A/B Testing)


WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, a_b_testing_selector)))

# Asignamos el enlace al selector

ab_testing_link = driver.find_element(By.CSS_SELECTOR,a_b_testing_selector)

# ingresamos al enlace

click(ab_testing_link)

# esperamos de manera explicita que cargue el elemento a validar

WebDriverWait(driver,2).until(EC.text_to_be_present_in_element((By.TAG_NAME,'h3'),('A/B')))

# tomamos el elemento a validar

ab_testing_site = driver.find_element(By.TAG_NAME,'h3')

# se realiza la asercion del elemento

if (ab_testing_site.text== 'A/B Test Control'):
    assert ab_testing_site.text == 'A/B Test Control','Fallo la prueba de A/B testing'
else:
    assert ab_testing_site.text == 'A/B Test Variation 1','Fallo la prueba de A/B testing'



driver.quit()





