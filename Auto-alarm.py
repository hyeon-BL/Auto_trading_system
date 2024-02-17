import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxp-6468131130481-6452567884821-6440965841111-4498da67d1d82aff22e8e531be1b2163"
 
post_message(myToken,"#주식알림","jocoding")
