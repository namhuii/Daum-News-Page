
import requests
from bs4 import BeautifulSoup


url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()
#print('#뉴스 제목: {}'.format(title))

doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('section p')  #section 안에 있는 p태그
contents.pop(-1)  # 기자 정보 삭제 참고로 pop은 인덱스로 remove는 값으로 지우는 거

#print(contents)
#print(len(contents))

content = '' # 본문 총합
for info in contents:
    content += info.get_text()
    #print(info.get_text())

print('##########################')
print('# 뉴스 제목: {}'.format(title))
print('###########################')

print('# 뉴스 본문: {}'.format(content))