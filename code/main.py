import requests
import numpy as np
from stockinfo import StocksCodeList
from stockinfo import StockDetail

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

stocknamedict = StocksCodeList.getNameNCode(1) # 1: 코스피 2: 코스닥
#print(stocknamedict[0].keys())

stockname = '삼성전자'

for i,stockdict in enumerate(stocknamedict):
    if(str(stockdict['name']).find(stockname)>-1):
        dicttockdetail = StockDetail.getStockDetail(stockdict['code'])

print(dicttockdetail.keys())


 
myToken = "xoxb-2022660199107-2015678020678-NRPVXdvgvptltm6BfXSGPErO"
 
message = stockname + "의 종가는 " + str(dicttockdetail['종가']) + "입니다."

post_message(myToken,"#stock",message)
