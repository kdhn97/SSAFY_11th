import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 동적인 페이지는 가져올 수 없다
    # response = requests.get(url)
    # print(response.text)

    # 크롬 브라우저가 열리고 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 파일로 저장하여 확인
    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    # 검색 결과 개수
    # result-stats id를 사용
    # result_stats = soup.select_one('#result-stats')
    # print(result_stats) # 검색결과 약 7,410,000개

    # 각 게시물 가져오기
    # 공통적으로 div 태그 + g 클래스
    g_list = soup.select('div.g')
    for g in g_list:
        # 요소 안에서 LC20ib MBeuO DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one('.LC20lb.MBeuO.DKV0Md')
        # 요소가 존재한다면
        if title is not None:
            print('제목 = ', title.text)

keyword = '탕수육'
get_data(keyword)