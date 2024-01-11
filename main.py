import requests
from send_email import send_email

topic="tesla"

api_key="8ce61b8f73a54dc294de806dc5b348e5"
url ="https://newsapi.org/v2/everything?" \
     f"q={topic}&" \
     "sortBy=publishedAt&" \
     "apiKey=8ce61b8f73a54dc294de806dc5b348e5" \
     "language=en"
request=requests.get(url)

content=request.json()

body= ""
for article in content["articles"][0:20]:
     if article["title"] is not None:
         body = "subject: Today's news" \
                + "\n" + body + article["title"] + "\n" \
                + article["description"] \
                +"\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)





