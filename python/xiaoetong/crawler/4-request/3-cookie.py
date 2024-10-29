import requests

# # 第一种方法：手动从网站请求复制cookie
# url = "https://xueqiu.com/statuses/hot/listV3.json?page=3&last_id=304900631"
# headers = {
#     "Cookie": "acw_tc=1a0c660917266730980843381e0053fdfb029bcc1877184342ce175b838795; xq_a_token=927886df384cbb16c88673ae7f519c76650c54b9; xqat=927886df384cbb16c88673ae7f519c76650c54b9; xq_r_token=1d46f0ed628506486164e5055a4993f9b54b2f4c; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyOTIxMjc4NCwiY3RtIjoxNzI2NjczMDU1MTM3LCJjaWQiOiJkOWQwbjRBWnVwIn0.Y1kAI3cdCu77n-SJBTz-EVvsJAzSm_p3njwQDJziLNKoCYHOxdx4ESC-GETJWzbk2I9hdbTKp2gr0W-erx3yYGZKIIn6l8SBW9_eW-IORs1zZgUuAfLMmXk4BZkodxOPNP_U2kwO3uD9xNQ68JOcc4NkVC2ZHLIVg1wZTHeJ3uIgRd7XL2bamuw2XMSoWtR6ZzlL1rzOaTLc_zaBAmHwQV1065rJcA-E7KSxIhzhyn7MMEZapnxkcOZykpkW3SaePFLuq2hIrP6AhCbdPcg0YzadVE6HNt8YbxRHGrq4UTaOoRLBqRp0coC4bhWiSgT5RrelsEdvhn0S8-NIDsHOfQ; cookiesu=811726673098092; u=811726673098092; device_id=5ab8db83a6a7682152efe19c37388bd8; Hm_lvt_1db88642e346389874251b5a1eded6e3=1726673101; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1726673101; HMACCOUNT=1278405926CC50F5; smidV2=2024091811250153d160004b453e173bdc239859a5c34800fa6651eb9bc4c60; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=wMufdfWfSooNzdyUXBeuEK+x+h7INcjdOJHf+0+Lm0x1i+eVJCdbq14qdoxm8zG1JH6v3u4fAGDsdLrn+uXqZQ%3D%3D; ssxmod_itna=eqUxuDBD9AwxcDGxBPiKGd2k1FfjwYGCe5esSiSDBkDPiNDnD8x7YDvjDAhf3fbRw5Lm7ATPerFr0HL3Kfjb54qLW9k4GLDmKDyGtrPGGUxBYDQxAYDGDDPDocPD1D3qDkD7O1lS9kqi3DbONDmkdDIq0xxDdSFLQ4xYQDGdI6D7jq1d4D0d+N5rQ1eOiDY8d4EMbgQAnxK7=DjMiD/Sx8w76oLZ9YnLnFs=0a3qGy3KGuju2BUl4yBMUDyOp3nO+zWOY5KDxrB2DPU/wYF0Gql2+v32GHoG+x0UqjxD3rj744eD; ssxmod_itna2=eqUxuDBD9AwxcDGxBPiKGd2k1FfjwYGCe5esSiD8TPEDGNP4eGaKzA1ozofjo0aE+wHD8gxU+qEO0GrP+AanG4INQFiSGYQL7nHrDnQGFp0+zplQu1tm/hFBLIja10gaDKwfA0X9bw4aGqxQxpsqiIGeFFe3D08DYFeXmGY3lbPMWreYtD4OKxphhGDD",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
# }

# res = requests.get(url, headers=headers)    
# res.encoding = "UTF-8"

# print(res.text)

# # 第二种方法：半自动获取cookie

# # 访问首页，获取cookie
# target_url = "https://xueqiu.com/statuses/hot/listV3.json?page=3&last_id=304900631"
# cookie_url = 
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
# }
# res = requests.get(cookie_url, headers=headers)
# res.encoding = "UTF-8"
# cookie = res.cookies.get_dict()

# # 使用cookie访问目标页面
# target_res = requests.get(target_url, headers=headers, cookies=cookie)
# target_res.encoding = "UTF-8"

# print(target_res.text)

# 第三种方法：自动获取cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
session = requests.session()

url = "https://xueqiu.com/"
target_url = "https://xueqiu.com/statuses/hot/listV3.json?page=3&last_id=304900631"

session.get(url, headers=headers) # 访问首页，获取cookie

target_res = session.get(target_url, headers=headers)
target_res.encoding = "UTF-8"

print(target_res.text)

