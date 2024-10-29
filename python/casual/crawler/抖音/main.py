import requests
from moviepy.editor import *

url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAADx_uCWYqTt6acf-kEokMP6Gn664K86al-zt_FW64Gak&max_cursor=0&locate_item_id=7378091464707853620&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7384029947876673058&verifyFp=verify_lxsw8v3d_898f01cc_febc_9768_e367_34e1663e858b&fp=verify_lxsw8v3d_898f01cc_febc_9768_e367_34e1663e858b&msToken=14cQ31QoOyiO60wiOxsWTV8dLDMsKsgDtOEZGqxFyz--5aadfEx0nuScbYmj0K0D7FdeTnuXR0VUG5HZNFdIx7nuMBLDf28TgOeL-HL3_FFg8wGp5wAU&a_bogus=QvR0MdgvDEIivDS65WcLfY3q6RN3YmtX0trEMD2f9dfV1g39HMYm9exoH17vwm6jNs%2FDIeYjy4hCT3rMx5%2FbA3vRHuDKUIcgmESkKl5Q5xSSs1Xce6UgrUkE-wsACFrQsv1lxOfkww5CSY8hWnAJ5kIlO62-zo0%2F95E%3D"

header = {
    "cookie": 
    "ttwid=1%7CUWa--qPuaqTLf9-M_ZVtriIfgs7fiTByq9Bx8odWF5Q%7C1719228467%7C44a311e01e07234e4d23700382b351450d3473fb373e220fadc119d45b76071b; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e385280347c0bcf46ebb3a19fc2e07d67b4a581b0549a8fa0acd5083aeb1b3e31ab57622217b8744750bff7c51924fb3bd03f07cc5db0ea647010c21d756b3ed0fd8c01684b4003d580a303c6817d87932f249a; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; csrf_session_id=9f94238e28b58225ea082f09c1ab9b2a; strategyABtestKey=%221719228470.646%22; xgplayer_user_id=972968842194; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=c194ac60a11c8a1f7f3cff104116e73b; passport_csrf_token_default=c194ac60a11c8a1f7f3cff104116e73b; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; fpk1=U2FsdGVkX1/LpOTBjvTLX3GiAah8f7ZcrrHpxIwrfDQmW0imxqDKZdJ8+QShlIKDiQ91PExZuwJZHk8zEvSFfw==; fpk2=5f4591689f71924dbd1e95e47aec4ed7; bd_ticket_guard_client_web_domain=2; s_v_web_id=verify_lxsw8v3d_898f01cc_febc_9768_e367_34e1663e858b; d_ticket=1896d844559242aa5537cfde73d91b40e24d8; passport_assist_user=Cj1ZoTPPpS4bBy6YHNvg6pq4FspEPnGfN93RqKK8Cj_vCc92aVUQqns7hj0xz_9tw_3-OrNN2a9sbBq1kYOmGkoKPI-CTpEFwb-5k4nqBzp_teGC2MK_-qM3OSV-4LeGVox0o66x5SmHCEC0mBbhLG9tFfDyrew-X5CWb6o4wxDk8NQNGImv1lQgASIBA4unKzY%3D; n_mh=slvfWiGvw4ZeXqZmkM2dxXItlIJyDMd8ilb6T6Cq3CY; sso_auth_status=c6910fbebc546ef5cb52f6351be28244; sso_auth_status_ss=c6910fbebc546ef5cb52f6351be28244; sso_uid_tt=4948cac1ba587d1d5616924770965519; sso_uid_tt_ss=4948cac1ba587d1d5616924770965519; toutiao_sso_user=6895c4130be0dfc34a2798fe1f6865e8; toutiao_sso_user_ss=6895c4130be0dfc34a2798fe1f6865e8; sid_ucp_sso_v1=1.0.0-KDdmY2RhN2M0NzE4MmNmYzEyMTJhMzQ2OWIzMGQ0ZDUyNjBjMzk2ZWEKHwiFiOXY-AIQgbHlswYY7zEgDDDb8-HZBTgCQPEHSAYaAmxmIiA2ODk1YzQxMzBiZTBkZmMzNGEyNzk4ZmUxZjY4NjVlOA; ssid_ucp_sso_v1=1.0.0-KDdmY2RhN2M0NzE4MmNmYzEyMTJhMzQ2OWIzMGQ0ZDUyNjBjMzk2ZWEKHwiFiOXY-AIQgbHlswYY7zEgDDDb8-HZBTgCQPEHSAYaAmxmIiA2ODk1YzQxMzBiZTBkZmMzNGEyNzk4ZmUxZjY4NjVlOA; passport_auth_status=7981836611408ce3c4f629aa72441bd1%2Caae6eb8b821b49a611407b38fa2e6f41; passport_auth_status_ss=7981836611408ce3c4f629aa72441bd1%2Caae6eb8b821b49a611407b38fa2e6f41; uid_tt=63d85e262143ec6666b45ccee377d1c0; uid_tt_ss=63d85e262143ec6666b45ccee377d1c0; sid_tt=149eba6362b93bdaaa2f8f1deb29ec0f; sessionid=149eba6362b93bdaaa2f8f1deb29ec0f; sessionid_ss=149eba6362b93bdaaa2f8f1deb29ec0f; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e385280347c0bcf46ebb3a19fc2e07d67b4a581b0549a8fa0acd5083aeb1b3e31ab5762425c93e8b535914f10f8f5423284be2d9b6ecd00676af36b21e6bae62878cb67917e7cc571927b6966d24450882b7ffd09d56a84d7e37dedd5bb1eeee71332fdac248be9e155d3e5ab28655ecc31eb806bca92ddd9016d8a48c6244ffdde42134061badd7c9e8615de2fcd9e65169286; publish_badge_show_info=%220%2C0%2C0%2C1719228558052%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=0509e37971a0b627dd389aa369b52bde; __security_server_data_status=1; sid_guard=149eba6362b93bdaaa2f8f1deb29ec0f%7C1719228558%7C5183990%7CFri%2C+23-Aug-2024+11%3A29%3A08+GMT; sid_ucp_v1=1.0.0-KDEzYmI0NTk5Mzk3MzJjMDRhYzY1NDA1OWQ1N2UzNzk2MDlmZTk5OTAKGQiFiOXY-AIQjrHlswYY7zEgDDgCQPEHSAQaAmxmIiAxNDllYmE2MzYyYjkzYmRhYWEyZjhmMWRlYjI5ZWMwZg; ssid_ucp_v1=1.0.0-KDEzYmI0NTk5Mzk3MzJjMDRhYzY1NDA1OWQ1N2UzNzk2MDlmZTk5OTAKGQiFiOXY-AIQjrHlswYY7zEgDDgCQPEHSAQaAmxmIiAxNDllYmE2MzYyYjkzYmRhYWEyZjhmMWRlYjI5ZWMwZg; store-region=cn-tj; store-region-src=uid; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAArxfSbm9Wb_Yu2aJJ1YKB8jKFaMrviX-isMKEf9zH5lk%2F1719244800000%2F1719228561789%2F1719228558281%2F0%22; xg_device_score=7.4245193832548715; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; SEARCH_RESULT_LIST_TYPE=%22single%22; x-web-secsdk-uid=c26154c6-7570-4e32-babb-06292ec0230c; download_guide=%223%2F20240624%2F0%22; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=0667960850059beedcb54; dy_swidth=1920; dy_sheight=1080; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; my_rd=2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTTlRb1c5MGpoVDc3NjdXaDlLK05DTkM5SEpKVFUrekxFWVIvVXRlR25JbEt5dlJDOUJWYmtqbW9GblZiSjAweUhwMFMzVUowQzZLZklhckxaWWVidUU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=0f6ee6f4e6c594ca6be7fd43532a94213a6973926a4ed6bd0a1de230978ed96c4f67f1203f2deceb5efd44b06acee5015ce82dc759f7eb6f22d1165f1ffb008a; WallpaperGuide=%7B%22showTime%22%3A1719228628182%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A28%2C%22cursor2%22%3A0%7D; msToken=hnzk0gsVWCQbGUuahDJ3sqgq17XqjL1_p1fwZSXxlm9eLp0KhYTuWeXBHFnP5cb7Bz-vhTPYp23M4PTYw4BkOM1SQbNHgXuEiVrLEjvFuheV2Xk33Dy-; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22",
    "referer":
    "https://www.douyin.com/user/MS4wLjABAAAADx_uCWYqTt6acf-kEokMP6Gn664K86al-zt_FW64Gak?vid=7378091464707853620",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

res = requests.get(url, headers = header)

JSON = res.json()

id_list = JSON["aweme_list"]

print(len(id_list))

for id in id_list:

    vedio_url = id["video"]["play_addr"]["url_list"][2]
    vedio_res = requests.get(vedio_url, headers = header)
    vedio_name = id["desc"] + ".mp4"
    open(vedio_name, "wb").write(res.content)
    vedio = VideoFileClip(vedio_name)

    music_url = id["music"]["play_url"]["uri"]
    music_res = requests.get(music_url, headers = header)
    music_name = id["desc"] + ".mp3"
    open(music_name, "wb").write(res.content)
    music = AudioFileClip(music_name)

    print(vedio, music, url)

    altimate = vedio.set_audio(music)

    altimate.write_viedofile("完整视频.mp4")


# open("name.mp4", "wb").write(res.content)
