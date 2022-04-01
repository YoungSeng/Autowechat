# encoding:utf-8
import requests
import base64

def OCR_init():

    client_id = ''      # change it to yours!
    client_secret = ""      # change it to yours!
    print("client_id:" + client_id)
    print("client_secret:" + client_secret)

    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"


    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    response = requests.get(host)
    if response:
        print(response.json())
    else:
        print('No response!')

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # f = open('your path', 'rb')       # 二进制方式打开图片文件
    # img = base64.b64encode(f.read())

    return response, request_url

def picTotxt(response, request_url):
    with open(r'E:\Python\SiCheng_Yang\PycharmProjects\wechat\tmp.png', 'rb') as f:
        img = base64.b64encode(f.read())
        params = {"image":img}
        access_token = response.json()['access_token']
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        result = []
        if response:
            # print(response.json()['words_result_num'])
            for i in range(response.json()['words_result_num']):
                result.append(response.json()['words_result'][i]['words'])

        print(result)

        return result

if __name__ == '__main__':
    picTotxt(None, None)
