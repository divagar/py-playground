from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=RYifMlvQvMM")

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "ytd-player1"))
    )
    print("element -> ", element)
except NoSuchElementException:
    print("execpt NoSuchElementException")
finally:
    driver.quit()
