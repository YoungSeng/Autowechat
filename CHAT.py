# coding=UTF-8
# encoding:utf-8
# -*- coding:utf-8 -*-

import requests

def CHAT_init():

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=H7k1dCKWGVsGWrAdkp9vX4D7&client_secret=CxGN9MoU6HmcFfGvKVwnHTHffm1YVbos'
    response = requests.get(host)
    if response:
        print(response.json())

    access_token = response.json()
    '#####调用鉴权接口获取的token#####'
    return access_token

def txtTotxt(access_token, A):
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token['access_token']
    post_data = ("{\"version\":\"3.0\","
                 "\"service_id\":\"S66974\","
                 "\"session_id\":\"\","
                 "\"log_id\":\"7758521\","
                 "\"request\":"
                 "{"
                 "\"terminal_id\":\"88888\","
                 "\"query\":\""+A+"\"""}}").encode("utf-8")        # .decode("latin1")

    # print(post_data)

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=post_data, headers=headers)
    if response:
        try:
            result = response.json()['result']['context']["SYS_PRESUMED_HIST"]
            # print(result[-1])
            return result[-1]
        except:
            return '？'

