import httpx

def send():

    while True:

        url = httpx.get(api).json()['url']

        data = {

            "content": "",

            "embeds": [

                {

                "title": "Hypre Gen Anime 18+",

                "tts": "true",

                "description": "",

                "url": url,

                "color": "{randcolor}",

                "timestamp": "{time}",

                "image": {

                    "url": url

                }

                }

            ],

            "username": "Nahee",

            "avatar_url": url

            }

        httpx.post(webhook, json=data)

        print(url)

if __name__ == "__main__":

    api = 'https://api.waifu.pics/nsfw/waifu'

    webhook = input("Webhook Url >> ")

    send()
