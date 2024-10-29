import requests


headers = {
    # "Host": "join.qq.com",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    # "Accept": "application/json, text/plain, */*",
    # "Accept-Language": "en-US,en;q=0.5",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Content-Type": "application/json;charset=utf-8",
    # "Content-Length": "154",
    # "Origin": "https://join.qq.com",
    # "Connection": "keep-alive",
    # "Referer": "https://join.qq.com/post.html?query=p_1",
    # "Cookie": "pac_uid=0_66fee5dc44a16; iip=0; _qimei_uuid42=17b0c102623100ac7ca6a577e6a76f0a1ae1c4a933; _qimei_fingerprint=ed3ebf411bfae200a32ac7b6c71a7321; _qimei_q36=; _qimei_h38=defb557e7ca6a577e6a76f0a0200000a817b0c; RK=Uq8MJEVDU7; ptcz=743f8c74ce528b80208d1fda5c2c924d057b384eff28e01b1bdac8d0b529eeb4; qq_domain_video_guid_verify=9b15e4d09bf708d6; fqm_pvqid=a52a5de4-103f-4d9f-a522-ec1f214de0f7; wwo_token=WedriveToken-eUXbOQlYffhIm2bD7rynLoK2Mj4mbkF9AB5LlGY1Im6B0chRHsv_-GLF6weNZYi4h6-waP4CJaQvnAUfHTHYYSJquau2PmizMD-TRjECVU9zld0cSZmgjthpoOatPmI-tNXrqdCDohwSUZ2FMlGq5nWtuhoaed1AbGf1r6NKRcU",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-origin",
    # "Sec-GPC": "1",
    # "Priority": "u=0",
    # "TE": "trailers"
}

url = "https://join.qq.com/api/v1/position/searchPosition?timestamp=1727631805355"


for i in range(1, 11):
    data = {"projectIdList":[1],
        "keyword":"",
        "bgList":[],
        "workCountryType":0,
        "workCityList":[],
        "recruitCityList":[],
        "positionFidList":[],
        "pageIndex":i,
        "pageSize":10
        }
    
    res = requests.post(url, headers=headers, json = data)
    
    resJson = res.json()
    # print(res.text)

    for pos in resJson["data"]["positionList"]:
        print(f'{pos["positionTitle"]}, {pos["workCities"]}, {pos["projectName"]}')
