import json

from flask import Flask, request, make_response

from handler import slack_handler

# 플라스크 인스턴스 생성
app = Flask(__name__)


@app.route('/', methods=['POST'])
def default_listener():
    # 슬랙에서 보낸 request 데이터를 json으로 파싱한다.
    slack_event = json.loads(request.data)
    print(slack_event)

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

                ####################################################################################

                #								여기에 전처리 등 추가!								   #

                ####################################################################################

                slack_handler.post_slack_message(message=user_query, channel=channel)

                # 정상적으로 완료했음에 대한 http response
                return make_response("response made :)", 200, )
            except IndexError:
                # 멘션은 했지만 텍스트는 남기지 않은 경우에 대한 에러.
                # do nothing
                pass
        # 그 외 event에 대한 핸들링: 404 error
        msg = f"[{event_type}] cannot find event handler"
        return make_response(msg, 404, {"X-Slack-No-Retry": 1})

    # 그 외 request 핸들링: 404 error
    return make_response("No Slack request events", 404, {"X-Slack-No-Retry": 1})


# 실행
if __name__ == '__main__':
    app.run(debug=True)