import requests
from send_email import send_email

api_key="8ce61b8f73a54dc294de806dc5b348e5"
url ="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2023-12-10&sortBy=publishedAt&apiKey=" \
     "8ce61b8f73a54dc294de806dc5b348e5"

request=requests.get(url)

content=request.json()

body= ""
for article in content["articles"]:
     if article["title"] is not None:
         body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)





