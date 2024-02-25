from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
company_name = jobs[1].find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
skills = jobs[1].find('span', class_ = 'srp-skills').text.replace(' ', '')
time_frame = jobs[1].find('span', class_ = 'sim-posted').text
print(jobs)