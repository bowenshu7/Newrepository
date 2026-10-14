#name: taobao search result
#author: Bowen
#goal: to get the information about the taobao goods
#date: 2026/10/11
#stage: finished

import requests
import execjs
import time
from jsonpath import jsonpath
import json

def get_page_data(url, params, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    result = response.text[12:-1]

    try:
        #select nodes
        elements = jsonpath(json.loads(result), '$..itemsArray[*]')
        for element in elements:
            #select title
            title = jsonpath(element,'$.title')[0]
            title_etl = title.replace('<span class=H>', '').replace('</span>', '')
            #select price
            price = jsonpath(element,'$.price')[0]
            #select city
            procity = jsonpath(element,'$.procity')[0]

            # data_list.append({'标题':title_etl, '价格':price, '地区':procity})
            data_list.append([title_etl, price, procity])
    except:
        print(result)


if __name__ == '__main__':
    data_list = []
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://uland.taobao.com/sem/tbsearch?bc_fl_src=tbsite_NOX36458&channelSrp=baiduSomama&clk1=2d28446771bdba364fbb585da8244ae6&commend=all&ie=utf8&initiative_id=tbindexz_20170306&keyword=%E6%B3%95%E6%8B%8D%E6%88%BF&localImgKey=&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E6%B3%95%E6%8B%8D%E6%88%BF&refpid=mm_26632258_3504122_32538762&search_type=item&sourceId=tb.index&spm=tbpc.pc_sem_alimama%2Fa.search_manual.0&ssid=s5-e&tab=all",
        "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
    }
    #define cookies
    #_m_h5_tk and _m_h5_tk_enc need to be updated
    #tfstk needs to be updated
    #isg needs to be updated
    cookies = {
        "thw": "xx",
        "cna": "LG5TIrBARG4BASQMzgR+/3Yh",
        "t": "30ffe2abac2902a0b336496d8fc797d7",
        "xlly_s": "1",
        "3PcFlag": "1791792252924",
        "sgcookie": "E100CXk8JViKKUKTMlgeYzAw0eh6%2BUWQrWuJBatqFMdnmgpDjqilLpOQ%2FoMiYuHqiDGgygy7ysfvVJxhljZa%2FA0m%2FLB%2FoUn46hrmnzV7l9BbbMY%3D",
        "wk_cookie2": "162d2188280d350c47e22d801a46c895",
        "wk_unb": "UUpgTsH6b5RXgv56XA%3D%3D",
        "uc3": "vt3=F8dD1fNWXvey4ZOev10%3D&id2=UUpgTsH6b5RXgv56XA%3D%3D&nk2=F5RDLj3DM3fwx6S%2F4IY%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
        "lgc": "tb620488453960",
        "dnk": "tb620488453960",
        "uc4": "nk4=0%40FY4I7WNC2l5tKg4nO9CoMUGHBXLod%2BlgBw%3D%3D&id4=0%40U2gqwYgnB5KNbBsuPdYm7ROhHP5RbHva",
        "tracknick": "tb620488453960",
        "_cc_": "URm48syIZQ%3D%3D",
        "_tb_token_": "e85431eeee7ee",
        "mtop_partitioned_detect": "1",
        "_m_h5_tk": "9b93ebbbb89caba17d300771fbe0c25c_1791963748237",
        "_m_h5_tk_enc": "c8cd0544aed6caab61b63be65e9ca4a0",
        "tfstk": "hGVogZsA2dWOsZBAnER9hg_xEtC9ie4_7DdJLbrDToZnpWUEvXq3xkm-LgG8to4UjYnrv9ietkULwkBA6zTwYUQ7qDkEuwuK54897jWbPXGFDEdFB1XHgvLBT2oFojuE8QleTLzVo20iYXorLnJq7moETXrEgIuZ8URrLLz20mgETDrETZ4qc2cEYklFor77Hzf2zmXhpZfYhmAeTS0VAD_-Vqg4g4Du1zo0yzn6yKguozIk1rhSil0T2sRujyz_LxVH0GmQirPzLrtlYUpHKYujocHPQdlkr03b2ZbDQwMrl4iOoZvBdYujocQcod5IUqgSX",
        "isg": "BOXl1qnd4ytB6gT011E5h_5H9KEfIpm0Rlp-rufKoZwr_gVwr3KphHOYiGKIfrFs"
    }
    # define url
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'

    # current page
    page = 1
    keyword = "法拍房"

    t = str(int(time.time()*1000))
    with open('decode.js','r',encoding='utf-8') as f:
        jscode = f.read()
    r = cookies["_m_h5_tk"].split('_')[0]
    data = "{\"appId\":\"43356\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc_sem\\\",\\\"page\\\":\\\""+f"{page}"+"\\\",\\\"n\\\":48,\\\"q\\\":\\\""+f"{keyword}"+"\\\",\\\"qSource\\\":\\\"url\\\",\\\"pageSource\\\":\\\"tbpc.pc_sem_alimama/a.search_manual.0\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"categoryp\\\":\\\"\\\",\\\"myCNA\\\":\\\"LG5TIrBARG4BASQMzgR+/3Yh\\\",\\\"clk1\\\":\\\"2d28446771bdba364fbb585da8244ae6\\\",\\\"refpid\\\":\\\"mm_26632258_3504122_32538762\\\"}\"}"

    sign = execjs.compile(jscode).call('decode',t,r,data)

    # while len(data_list)<50 and page<3:
    #     page+=1

    #define params
    params = {
        "jsv": "2.7.2",
        "appKey": "12574478",
        "t": t,
        "sign": sign,
        "api": "mtop.relationrecommend.wirelessrecommend.recommend",
        "v": "2.0",
        "type": "jsonp",
        "dataType": "jsonp",
        "callback": "mtopjsonp3",
        "data": data
    }
    print(page)
    get_page_data(url, params, data_list)
    time.sleep(5)
    print(data_list)
    print(len(data_list))