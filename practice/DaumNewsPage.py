# Daum News에서 페이지를 돌면서 뉴스 기사의 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup
# https://news.daum.net/breakingnews/digital # 실제 URL 주소
# ? 기준 ~ 오는 값: 주소 X
# page 반복~
i = 0
for page_number in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_number)
    result = requests.get(url)

    doc = BeautifulSoup(result.text, 'html.parser')
    url_list = doc.select('ul.list_news2 a.link_txt')

    # page 내에서 뉴스 목록 반복(in page)
    for url in url_list:
        i += 1 # News Count
        print('## NEWS -> {}번 #####################'.format(i))
        new_url = url['href']
        print('# URL:'.format(new_url))
        result = requests.get(new_url)
        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()
        contents = doc.select('section p')
        contents.pop(-1)

        content = ''
        for info in contents:
            content += info.get_text()

        print('# 뉴스 제목: {}'.format(title))
        print('# 뉴스 본문: {}'.format(content))