from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://aws.amazon.com/sagemaker/pricing/').text
soup = BeautifulSoup(html_text, 'lxml')
tableApis = soup.find_all('div', class_='aws-controls')
#apis = tableApis.find_all('tr')
# for api in apis: 
#     price = api.find('td')
#     print(price)
print(tableApis)

