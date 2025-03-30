from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://www.sciencedirect.com/journal/computers-and-graphics/about/editorial-board"
driver.get(URL)

driver.implicitly_wait(10)


editors = driver.find_elements(By.CLASS_NAME, 'js-editor-name')

for editor in editors:

    name = editor.text.strip() if editor else 'No name found'


    try:
        university_info = editor.find_element(By.XPATH, "following-sibling::p").text.strip()
    except:
        university_info = 'No university found'


    print(f"Name: {name}")
    print(f"University: {university_info}")
    print("-" * 40)

driver.quit()