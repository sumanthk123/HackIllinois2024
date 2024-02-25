from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://openai.com/pricing').text
soup = BeautifulSoup(html_text, 'lxml')

all_model_labels = soup.find_all('tr', class_="border-b border-secondary")
all_model_values = []
for models in all_model_labels:
    if models.span.text != 'Input' and models.span.text != 'Output' and models.span.text != 'Model' and models.span.text != 'Training' and models.span.text != 'Input usage' and models.span.text != 'Output usage' and models.span.text != 'Price' and models.span.text != 'Quality' and models.span.text != 'Resolution':
        #print(models.span.text)
        model = models.find_all('span', class_='f-body-1')
        #print(model)
        if len(model) > 0:
            all_model_values.append(model)
for i in all_model_values:
    print(i)

# all_model_labels = soup.find_all('td', class_='pt-8 pb-8')

# model_values = []
# print(all_model_labels[5].text)
# for models in all_model_labels:
#     print(all_model_labels[6])
#     input()
#     if models.text != 'Input' and models.text != 'Output' and models.text != 'Model' and models.text != 'Training' and models.text != 'Input usage' and models.text != 'Output usage' and models.text != 'Price' and models.text != 'Quality' and models.text != 'Resolution':
#         model_values.append(models.text)
#print(model_values)
# for models in all_model_labels:
#     model = models.find_all('span', class_='f-body-1')
#     print(model[1])
    # for attribute in model:
    #     model_values.append(attribute.span.text)
#print(model_values)
