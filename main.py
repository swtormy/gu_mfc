from bs4 import BeautifulSoup
import requests, json


comments = []


for i in range(1, 3015):
    print(f'Закгрузка комментов с {i} страницы')
    if i == 1:
        url = 'https://gu.spb.ru/mfc/comment/list/'
        page =requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        comm_list = soup.find_all('div', class_='userText')
        for comm in comm_list:
            comments.append(comm.get_text())

    url = 'https://gu.spb.ru/mfc/comment/list/?PAGEN_1=' + str(i)
    page =requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    comm_list = soup.find_all('div', class_='userText')
    
    for comm in comm_list:
        comments.append(comm.get_text())

with open('temp.json', 'w') as file:
    json.dump(comments, file)

