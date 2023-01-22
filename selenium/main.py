from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")  
driver.find_element_by_name("search_query").send_keys("Purple Melody Bahana")
driver.find_element_by_id("search-icon-legacy").click()

try:
    video = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))
    wait = WebDriverWait(driver, 600) 
except TimeoutError:
    print("Not finished")

driver.close()