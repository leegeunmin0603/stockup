## 중요 공지 사항 기입

slack bot auth : xoxb-2022660199107-2015678020678-OD6UkrmJof6bAk1xSSlDOwuu

slack bot에 대한 keyword 명령 예시(2월 업데이트 후 변동):

import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2022660199107-2015678020678-OD6UkrmJof6bAk1xSSlDOwuu"
 
post_message(myToken,"#stock","test")

