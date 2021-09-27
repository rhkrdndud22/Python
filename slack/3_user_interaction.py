# 2_display_movies.py
# 크롤링한 영화 정보를 포맷에 맞춰 슬랙에 보내주는 역할

import json
import os

# pip install Flask
from flask import Flask, request, make_response
from handler import slack_handler

import datetime

crawling = __import__('1_crawling')

areaCode = ''
theaterCode = ''

# 플라스크 인스턴스 생성
app = Flask(__name__)

@app.route('/user-select', methods=['POST', 'GET'])
def handle_interaction():
	slack_event = json.loads(request.form['payload'])
	print(slack_event)
	# 만약 지역 선택 블록에서 interaction request가 온 경우
	if slack_event['actions'][0]['placeholder']['text'] == '지역을 선택해주세요.':
		area = slack_event['actions'][0]['selected_option']['text']['text']
		global areaCode
		areaCode = slack_event['actions'][0]['selected_option']['value']
		block = build_theater_block(area)
		slack_handler.post_layout_message(blocks=block, channel=slack_event['channel']['id'])

	# 만약 극장 선택 블록에서 interaction request가 온 경우
	if slack_event['actions'][0]['placeholder']['text'] == '극장을 선택해주세요.':
		date = datetime.datetime.now().strftime("%Y%m%d")
		global theaterCode
		theaterCode = slack_event['actions'][0]['selected_option']['value']
		slack_handler.post_slack_message(channel=slack_event['channel']['id'], message=f'http://www.cgv.co.kr/reserve/show-times/?areacode={areaCode}&theaterCode={theaterCode}&date={date}')

	return make_response("response made :)", 200, )

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

				if user_query.strip() == '/상영정보':
					block = build_select_block()
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
									{stars}\n \
									장르: {', '.join(movie['genre'])}\n \
									감독: {', '.join(movie['director'])}\n \
									출연: {', '.join(movie['actors'])}\n"
		block.append(temp)
	return block

def build_select_block():
	# 블록 담을 리스트
	block = []
	# 헤더 블록
	header = {}
	header['type']  = 'header'
	header['text'] = {}
	header['text']['type'] = 'plain_text'
	header['text']['text'] = '지역을 선택해주세요.'
	block.append(header)
	# divider 블록
	divider = {}
	divider['type'] = 'divider'
	block.append(divider)
	# 지역 블록
	options = json.load(open('./slack/info.json', 'rb'))
	input_block = {}
	input_block['type'] = "input"
	input_block['element'] = {}
	input_block['element']['type'] = 'static_select'
	input_block['element']['placeholder'] = {}
	input_block['element']['placeholder']['type'] = "plain_text"
	input_block['element']['placeholder']['text'] = '지역을 선택해주세요.'
	input_block['element']['options'] = []
	for area in options:
		temp = {}
		temp['text'] = {}
		temp['text']['type'] = "plain_text"
		temp['text']['text'] = area
		temp['value'] = options[area]['code']
		input_block['element']['options'].append(temp)
	input_block['element']['action_id'] = 'static_select-action'
	input_block['label'] = {}
	input_block['label']['type'] = 'plain_text'
	input_block['label']['text'] = "지역"
	block.append(input_block)
	return block

def build_theater_block(area):
	# 블록 담을 리스트
	block = []
	# 헤더 블록
	header = {}
	header['type']  = 'header'
	header['text'] = {}
	header['text']['type'] = 'plain_text'
	header['text']['text'] = '극장을 선택해주세요.'
	block.append(header)
	# divider 블록
	divider = {}
	divider['type'] = 'divider'
	block.append(divider)
	# 영화관 블록
	options = json.load(open('info.json', 'rb'))

	input_block = {}
	input_block['type'] = "input"
	input_block['element'] = {}
	input_block['element']['type'] = 'static_select'
	input_block['element']['placeholder'] = {}
	input_block['element']['placeholder']['type'] = "plain_text"
	input_block['element']['placeholder']['text'] = '극장을 선택해주세요.'
	input_block['element']['options'] = []
	for theater, value in options[area]['theaters'].items():
		temp = {}
		temp['text'] = {}
		temp['text']['type'] = "plain_text"
		temp['text']['text'] = theater
		temp['value'] = value
		input_block['element']['options'].append(temp)
	input_block['element']['action_id'] = 'static_select-action'
	input_block['label'] = {}
	input_block['label']['type'] = 'plain_text'
	input_block['label']['text'] = "극장"
	block.append(input_block)
	return block



# 실행
if __name__ == '__main__':
    app.run(debug=True)