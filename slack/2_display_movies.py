# 2_display_movies.py
# 크롤링한 영화 정보를 포맷에 맞춰 슬랙에 보내주는 역할

import json

# pip install Flask
from flask import Flask, request, make_response
from handler import slack_handler

crawling = __import__('1_crawling')

# 플라스크 인스턴스 생성
app = Flask(__name__)

@app.route('/', methods=['POST'])
def default_listener():
	# 슬랙에서 보낸 request 데이터를 json으로 파싱한다.
	slack_event = json.loads(request.data)

	# 인자 중 challenge가 있으면 해당 인자의 값을 반환한다.
	# slack api specification. 참고:https://api.slack.com/
	if "challenge" in slack_event:
		return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

	# slack에서 발생한 event를 통한 request에 대한 핸들링
	if "event" in slack_event:
		event_type = slack_event["event"]["type"]
		# bot_mention일 경우에 대한 핸들링
		if event_type == 'app_mention':
			try:
				# 멘션을 남긴 채널 읽어오기
				channel = slack_event['event']['channel']
				# 유저가 멘션과 함께 남긴 텍스트 읽어오기
				user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']

				if user_query.strip() == '/영화정보':
					movies = crawling.get_current_movies()
					block = build_blocks(movies)
					slack_handler.post_layout_message(blocks=block, channel=channel)

				# 정상적으로 완료했음에 대한 http response
				return make_response("response made :)", 200, )
			except IndexError:
				# 멘션은 했지만 텍스트는 남기지 않은 경우에 대한 에러.
				# do nothing
				pass
		# 그 외 event에 대한 핸들링: 404 error
		msg = f"[{event_type}] cannot find event handler"
		return make_response(msg, 404, {"X-Slack-No-Retry": 1 })


	# 그 외 request 핸들링: 404 error
	return make_response("No Slack request events", 404, {"X-Slack-No-Retry": 1 })

def build_blocks(movies: list):
	# 블록 담을 리스트
	block = []
	# 헤더 블록
	header = {}
	header['type']  = 'header'
	header['text'] = {}
	header['text']['type'] = 'plain_text'
	header['text']['text'] = '현재상영작'
	block.append(header)
	# divider 블록
	divider = {}
	divider['type'] = 'divider'
	block.append(divider)
	# 영화 블록
	for movie in movies:
		temp = {}
		temp['type'] = 'section'
		temp['text'] = {}
		temp['text']['type'] = 'mrkdwn'
		stars = ":star:" * round(movie['score']/2)
		temp['text']['text'] = f"*{movie['title']}*\n \
									{stars} {movie['score']}\n \
									장르: {', '.join(movie['genre'])}\n \
									감독: {', '.join(movie['director'])}\n \
									출연: {', '.join(movie['actors'])}\n"
		block.append(temp)
	return block


# 실행
if __name__ == '__main__':
    app.run(debug=True)