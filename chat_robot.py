#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

import urllib.request
import urllib.parse

def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定回复，对于非特定问题进行智能回复

    参数描述：
    question 聊天内容
    '''

    if "你叫什么名字" in question:
        answer = "我是Halen"
    elif "我还有多少钱" in question:
        answer = "0.0元"
    elif "你多少岁" in question:
        answer = "18"
    elif "你是GG还是MM" in question:
        answer = "你猜呢"
    else:
        try:
            # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode({'msg':question}).encode()
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",params,method="POST")
            answer = urllib.request.urlopen(req).read().decode()
        except Exception as e:
            answer = "AI机器人出现故障！（原因：%s)" % e
    
    return answer

if __name__ == '__main__':
    print(get_robot_reply("你叫什么名字"))
    print(get_robot_reply("武汉明天天气如何"))
    print(get_robot_reply("你到底是谁"))