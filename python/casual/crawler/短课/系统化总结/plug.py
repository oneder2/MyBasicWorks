# -*-coding = utf-8-*-

# Author:qyan.li
# Date:2022/6/20 11:48
# Topic:借助于python爬取某站视频（某站站资源）
# Reference:https://www.bilibili.com/video/BV1GF411c7dA?p=3&vd_source=98cb4eb5f0c21487fcbd999a5f430af1

import requests
import re
import json
import pprint
import subprocess

def askURL(url):

    head = {
            ## 此处设置防盗链：指明连接的请求来源于B站，合法
            'referer':
            'https://www.bilibili.com/',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
    }
    response = requests.get(url = url,headers = head)
    return response

def getVideoInfo(response):
    ## 正则表达式：用于匹配获取音频和视频地址
    findUrl = re.compile('<script>window.__playinfo__=(.*?)</script>')
    VideoInfo = re.findall(findUrl,response.text)[0]
    ## 字符串转换为python的数据类型，便于后续操作
    jsonData = json.loads(VideoInfo)
    return jsonData

def download(jsonData):
    # print(type(jsonData))
    ## 解析获得音频和视频的url
    audioURL = jsonData['data']['dash']['audio'][0]['baseUrl']
    videoURL = jsonData['data']['dash']['video'][0]['baseUrl']
    print(audioURL)
    print(videoURL)

    ## 用于下载音频和视频信息
    audioContent = askURL(audioURL).content
    with open('./' + 'python教程' + '.mp3',mode = 'wb') as f:
        f.write(audioContent)
    videoContent = askURL(videoURL).content
    with open('./' + 'python教程' + '.mp4',mode = 'wb') as f:
        f.write(videoContent)

## 音视频合成参考：https://blog.csdn.net/weixin_43835542/article/details/109493050
## ffmpeg下载：https://blog.csdn.net/pythonlaodi/article/details/109222790
## 字符串前面加f：https://blog.csdn.net/qq_43463045/article/details/93890436
## (字符串中花括号中的部分可以正常的替换执行)

def audioAndVideo(audioFile,videoFile):
    outfile_name = './output.mp4'
    cmd = fr'F:\CommonApp\ffmpeg\bin\ffmpeg.exe -i {audioFile} -i {videoFile} -acodec copy -vcodec copy {outfile_name}'
    print(cmd)
    subprocess.call(cmd,shell=True)


def main():
    html = askURL(url = 'https://www.bilibili.com/video/BV1GF411c7dA')
    jsonData = getVideoInfo(html)
    ## pprint可以按照标准的方式打印字典，便于查阅
    pprint.pprint(jsonData)
    download(jsonData)
    audioAndVideo(r'C:/Users/腻味/Desktop/VideoClawer/BiliBiliClawer/python教程.mp3',r'C:/Users/腻味/Desktop/VideoClawer/BiliBiliClawer/python教程.mp4')
    pass



if __name__ == '__main__':
    main()
