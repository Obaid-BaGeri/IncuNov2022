from flask import Flask, request
import requests
import json
############## Bot details ##############
bot_name = 'OBG@webex.bot'
#roomId = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzMzNWY4YTAtYWUzNC0xMWVkLTgxMjgtMTUzNTk3MzRmZDNm'
token = 'MzdmYzY2NDctNzgzNy00YTY4LTk5MTItZTU1MmQzZjU0ZDAzN2Q1NGJlYzctMTg2_P0A1_4e89776b-1220-469b-b659-124204c7b3aa'
header = {"content-type": "application/json; charset=utf-8", 
          "authorization": "Bearer " + token}
############## Flask Application ##############
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def sendMessage():
  webhook = request.json
  url = 'https://webexapis.com/v1/messages'
  msg = {"roomId": webhook["data"]["roomId"]}
  sender = webhook["data"]["personEmail"]
  message = getMessage()

  if (sender != bot_name):
      if (message == "help"):
          msg["markdown"] = "Welcome to **Grads Bot**!  \n List of available commands: \n- grads \n- help"
      elif (message == "grads"):
        msg["markdown"] = "Python Masters!"
      else:
        msg["markdown"] = "Sorry! I didn't recognize that command. Type **help** to see the list of available commands."
      requests.post(url,data=json.dumps(msg), headers=header, verify=True)
def getMessage():
  webhook = request.json
  url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
  get_msgs = requests.get(url, headers=header, verify=True)
  message = get_msgs.json()['text']
  return message
  app.run(debug = True)
