import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe') # 크롬 웹드라이버 파일 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3+%EC%8A%AC%EA%B8%B0") # 다음에 '레드벨벳 슬기' 이미지 검색 링크
time.sleep(5) # 5초 동안 페이지 로딩 대기

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("#imgList > div > a > img")

i=1
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src, f'imgs/{i}.jpg') 
    i+=1

driver.quit() # 끝나면 닫아주기
