from seleniumwire import webdriver
import json

options = {
    'enable_har': True  # Capture HAR data, retrieve with driver.har
}

driver = webdriver.Chrome(seleniumwire_options=options)

driver.get('https://dog.ceo/api/breeds/image/random')

values = json.loads(driver.har)

print(values["log"]["entries"][1]["request"]["method"], values["log"]["entries"][1]["response"]['content']['text'], values["log"]["entries"][1]["request"]["url"])

# Access and print requests via the `requests` attribute  
for request in driver.requests:  
	if request.response:  
		print(  
			request.url,  
			request.response.status_code,  
			request.body) 