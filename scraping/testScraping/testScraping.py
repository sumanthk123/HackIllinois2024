from bs4 import BeautifulSoup

with open("test.html") as fp:
    content = fp.read()
    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        print(course.h5.text)
        print(course.a.text)
        #print(course.a['href'])
        print()