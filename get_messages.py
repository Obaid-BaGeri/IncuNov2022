import requests

roomId = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzMzNWY4YTAtYWUzNC0xMWVkLTgxMjgtMTUzNTk3MzRmZDNm'
token = 'MDUwZDZhN2YtY2JlYy00MzJkLWFkODYtNWVkMTUzN2M5Y2VkZTI1Y2Y2NzYtYzRi_P0A1_4e89776b-1220-469b-b659-124204c7b3aa'

url = "https://webexapis.com/v1/webhooks/v1/messages" + roomId

header = {"content-type": "application/json; charset=utf-8", 
         "authorization": "Bearer " + token}

response = requests.get(url, headers = header, verify = True)

print(response.json())
