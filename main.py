from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver
service = Service('C:/Users/mitsy/OneDrive/Documentos/work laptop/Professional development/Web Scrapping Project/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("https://www.rente.nl/spaarrente")

# Find all result rows containing the bank information and interest rate
result_rows = driver.find_elements(By.CLASS_NAME, 'result')

# Loop through each row and extract the bank name and interest rate
for row in result_rows:
    # Directly use the `row` element to extract the attributes
    bank_name = row.get_attribute('data-aanbiedernaam')
    interest_rate = row.get_attribute('data-rente')

    print(f"Bank Name: {bank_name}, Interest Rate: {interest_rate}")

# Close the browser
driver.quit()
