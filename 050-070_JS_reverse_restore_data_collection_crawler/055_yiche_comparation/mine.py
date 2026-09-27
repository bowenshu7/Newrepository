#name: yiche comparison between different cars
#author: Bowen
#goal: to get the information about the comparison between different cars
#date: 2026/9/27
#stage: finished

import requests
import time
import execjs

stamptime = int(time.time()*1000)
data = {
    "carIds": "189010,187033,187034",
    "cityId": "1301"
}
with open('x-sign.js','r',encoding='utf-8') as f:
    js_code = f.read()
xsign = execjs.compile(js_code).call('s',data,stamptime)
print(xsign)
#define headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cid": "508",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://car.yiche.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://car.yiche.com/chexingduibi",
    "reqid": "8d226e41b0cf34a90dd272e253125770",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
    "x-city-id": "1301",
    "x-ip-address": "222.247.197.227",
    "x-platform": "pc",
    "x-sign": xsign,
    "x-timestamp": str(stamptime),
    "x-user-guid": "e17dc2150c4f88ef224b444d6b28b1bb"
}
#define cookies
cookies = {
    "CIGUID": "e17dc2150c4f88ef224b444d6b28b1bb",
    "suid": "zqs0fhae8jaufxnykfcwkg7kwodbeoa6",
    "auto_id": "8724b4ec28bf3ce288d0b611fe0e2b7c",
    "CIGDCID": "rFjYHHkm8QyE7fHmsMieX4tTMrf6Yn5Z",
    "UserGuid": "e17dc2150c4f88ef224b444d6b28b1bb",
    "selectcity": "430100",
    "selectcityid": "1301",
    "selectcityName": "%E9%95%BF%E6%B2%99",
    "selectcityPinyin": "changsha",
    "hao_weight": "2",
    "isWebP": "true",
    "locatecity": "430100",
    "bitauto_ipregion": "222.247.197.227%3A%E6%B9%96%E5%8D%97%E7%9C%81%E9%95%BF%E6%B2%99%E5%B8%82%3B1301%2C%E9%95%BF%E6%B2%99%E5%B8%82%2Cchangsha",
    "Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44": "1788578435,1788585296,1790472910",
    "HMACCOUNT": "876958FB013481E3",
    "Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44": "1790474743"
}
#define web's url
url = 'https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details'
#define params
params = {
    "cid": "508",
    "param": "{\"carIds\":\"189010,187033,187034\",\"cityId\":\"1301\"}"
}
# get the response
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)