from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from elementos.elementos import enlace
from elementos.funciones import esperar

#inicializamos el driver
driver = webdriver.Chrome()

#dirigirse al enlace
driver.get(enlace)

driver.maximize_window()

#esperamos se cargue el elemento en pagina
WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > ul > li:nth-child(4) > a')))

#vamos al enlace de broken images
broken_images_link = driver.find_element(By.CSS_SELECTOR,'#content > ul > li:nth-child(4) > a')
broken_images_link.click()
broken_images_list = []
images = driver.find_elements(By.TAG_NAME,'img')
for image in images:
    src = image.get_attribute('src')
    try:
       response=requests.get(src)
       if response.status_code != 200:
        broken_images_list.append(src)


    except requests.exceptions.RequestException as e: 
        print(f"Image {src} is broken. Error: {e}")

if broken_images_list:

    for broken_image in broken_images_list:
        print(f'la siguiente imagen esta rota: {broken_image}')  
else:
    print('test passed succesfully')  
driver.quit()



