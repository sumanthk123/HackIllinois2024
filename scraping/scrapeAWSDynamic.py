from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options)
 
url = 'https://aws.amazon.com/sagemaker/pricing/' 
 
driver.get(url) 
 
elements = driver.find_elements(By.ID, 'aws-element-4d300e82-7c31-4937-82be-917e2f8270a2') 
for i in elements:
    print(i.text)
# for title in elements: 
# 	# select H2s, within element, by tag name 
# 	heading = title.find_elements(By.TAG_NAME, 'tr')
# 	print(heading)
# 	for api in heading:
# 		print(api.text)
# 	# print H2s 
# 	#print(heading)