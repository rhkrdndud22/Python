# 1_crawling.py
# 네이버 실시간 영화 정보를 불러오는 코드를 작성한다.

# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com/movie/running/current.nhn#"

# 영화 정보를 불러와 딕셔너리 형태에 맞춰 리스트로 return 해주는 함수
def get_current_movies():
	# 1. URL로부터 html을 파싱해오기
	req = requests.get(URL)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	# 2. 영화 부분 추출하기
	lis = soup.select('#content > div.article > div:nth-of-type(1) > div.lst_wrap > ul > li')
	# 3. 필요한 정보만 추출
	movies = []
	for idx, li in enumerate(lis):
		temp = {}
		temp['title'] = li.select('dl > dt > a')[0].text
		temp['score'] = float(li.select('dl > dd.star > dl.info_star > dd > div > a > span.num')[0].text)
		detail = li.select('.link_txt') # 개요, 감독, 출연
		temp['genre'] = [x.text for x in detail[0].select('a')]
		temp['director'] = [x.text for x in detail[1].select('a')]
		# 애니메이션처럼 배우 정보가 없는 경우가 있음
		if len(detail) > 2:
			temp['actors'] = [x.text for x in detail[2].select('a')]
		movies.append(temp)
		if idx > 10:
			break
	return movies

# 메인함수
if __name__ == "__main__":
	# movies = get_current_movies()
	# print(movies[0])
	print("ERROR:No direct call allowed.")