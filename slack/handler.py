import os


from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackHandler:
	token:str
	client: WebClient

	def __init__(self):
            load_dotenv(verbose=True)  # .env 파일에서 환경변수 읽어옴
            self.token = os.getenv('SLACK_TOKEN')  # SLACK_TOKEN이라는 환경변수를 token으로 지정
            self.client = WebClient(self.token)  # 해당 토큰으로 slack과 통신하는 웹클라이언트 생성

	def post_layout_message(self, channel: str, blocks: list):
		try:
			response = self.client.chat_postMessage(channel=channel, blocks=blocks)
			print(response)
		except SlackApiError as e:
			assert e.response["ok"] is False
			assert e.response["error"]
			print(f"ERROR: {e.response['error']}")


	def post_layout_message(self, channel: str, blocks: list):
		try:
			response = self.client.chat_postMessage(channel=channel, blocks=blocks)
			print(response)
		except SlackApiError as e:
			assert e.response["ok"] is False
			assert e.response["error"]
			print(f"ERROR: {e.response['error']}")


slack_handler =SlackHandler()