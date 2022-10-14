from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException




driver = webdriver.Chrome("F:/Documentos/PHP/TESTEDBO/chromedriver.exe")
driver.get("https://github.com/")

delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/dl/dd/input')))
    myElem.clear()
    myElem.send_keys("thiagohenrique166@gmail.com")
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button')))
    button.click()

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


driver.get("https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/table")

try:
    myElem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/dl/dd/input')))
    myElem.clear()
    myElem.send_keys("thiagohenrique166@gmail.com")
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button')))
    button.click()
    
    
    rows = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/main/article/section[3]/div/dl/dd[2]/div/table/tbody/tr[1]")))
    
    cols = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/main/article/section[3]/div/dl/dd[2]/div/table/tbody/tr[1]/td[1]")))
    
    print(rows)
    print(cols)
    
    print("Locators           "+"             Description")
    
    for r in range(2, rows+1):
        for p in range(1, cols+1):
            
            value = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[3]/main/article/section[3]/div/dl/dd[2]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
            print(value, end='       ')
        print()

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


