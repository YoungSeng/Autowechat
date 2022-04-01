#%% 找微信开了没，微信的位置

def wechat_init():

    pos1 = 'pos1.png'
    pos2 = 'pos2.png'
    send = 'send.png'
    standby = 'block2.png'
    while True:
        location1 = pyautogui.locateCenterOnScreen(pos1, confidence=0.9)
        # location2 = pyautogui.locateCenterOnScreen(pos2, confidence=0.9)
        location3 = pyautogui.locateCenterOnScreen(send, confidence=0.9)
        location4 = pyautogui.locateCenterOnScreen(standby, confidence=0.9)
        if location1 and location3 and location4:
            break
        else:
            print("未打开微信,1秒后重试")
            time.sleep(1)
    print(location1)
    return location1, location3, location4

#%% 找有没有新消息

def mainWork():
    red = 'red.png'
    while True:
        location = pyautogui.locateCenterOnScreen(red, confidence=0.9)
        if location:
            break
        else:
            print("没有新消息,1秒后重试")
            time.sleep(1)
    return location


def find_txt():
    chat = 'pos3.png'
    while True:
        locations = pyautogui.locateAllOnScreen(chat)       # , confidence=0.9
        if locations:
            break
        else:
            print("没有消息,1秒后重试")
            time.sleep(1)
    time.sleep(0.2)
    txt = list(locations)
    if txt != []:
        pos = sorted(txt, key=lambda x:x[1], reverse=True)[0]
        print(pos)
        pyautogui.doubleClick([pos[0]+25, pos[1], pos[2], pos[3]])
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        txt = pyperclip.paste()
        # print(str(txt))
    return str(txt)


def send_response(location1, location3, response):
    pyautogui.click([location1[0]+50, location1[1]+50])
    pyperclip.copy(response)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(location3)


def send_emoji(location1):
    pyautogui.click(location1)
    time.sleep(0.2)
    like = 'like.png'
    location2 = pyautogui.locateCenterOnScreen(like, confidence=0.9)
    pyautogui.click(location2)
    time.sleep(0.2)
    emoji = 'emoji.png'
    location3 = pyautogui.locateCenterOnScreen(emoji, confidence=0.9)
    pyautogui.click(location3)
    time.sleep(0.2)


if __name__ == '__main__':
    import pyautogui
    import time
    import pyperclip
    import CHAT

    location1, location3, location4 = wechat_init()
    access_token = CHAT.CHAT_init()
    pyautogui.click(location4)
    time.sleep(0.1)
    while True:
        red = mainWork()
        time.sleep(0.5)
        pyautogui.click(red)
        time.sleep(0.5)
        txt = find_txt()
        time.sleep(0.5)
        print(txt)
        if txt == '':
            send_emoji(location1)
            pyautogui.click(location4)
            time.sleep(0.5)
            continue
        response = CHAT.txtTotxt(access_token, txt)
        # time.sleep(0.5)
        print(response)
        send_response(location1, location3, response)
        time.sleep(1)
        pyautogui.click(location4)
        time.sleep(1)



