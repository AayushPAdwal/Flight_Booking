from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

driver.get("http://react-app")

assert "Air Routes" in driver.title

# Example login elements (update IDs based on your UI)
email = driver.find_element(By.ID, "email")
email.send_keys("test@example.com")

password = driver.find_element(By.ID, "password")
password.send_keys("password")
password.send_keys(Keys.RETURN)

print("Page title is:", driver.title)

driver.quit()
