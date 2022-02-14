#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2022/2/14 6:04 下午
# Author: Jianing
# FileDesc: 

import json
import logging
import re

import requests
from pyquery import PyQuery as pq



def robot_message(value):
    """
    This function aim at sending daily flight information by your own Dingding robot.
    Do not forget to add your own robot into a group first!
    Please input your own Dingding phone number into PHONE and Webhook into ROBOT_URL below,

    In the settings of this robot, please input 'flight' in 'custom keywords' part so that you can receive the message.
    :param value: The message that you want to send.
    :return:
    """
    logging.info(value)
    #
    PHONE = '*****'
    data = {
        "msgtype": "text",
        "text": {
            "content": "Flight Notification：{}, @{}".format(value, PHONE)
        },
        "at": {
            "atMobiles": [
                "{}".format(PHONE)
            ],
            "isAtAll": False
        }
    }
    try:
        ROBOT_URL = '*******'
        requests.post(url=ROBOT_URL, json=data)
        logging.info("Dingding robot: {}".format(value))
    except Exception as e:
        logging.error("Failed to send meaage by robot: {}, content: {}".format(e, value))

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'QN1=00008d8030683e057d68bdfd; QN48=6c419c04-1639-4fe3-9c9c-e7c4466d3ff3; QN300=organic; QN99=488; QN205=organic; QN277=organic; _i=DFiEuYKdjSewzgWw-znOX0KiV3yw; QN601=8cdbefd8edaa788afa3539aac005ea53; QN269=D1EAD7E08D7D11EC8097FA163E9C4675; quinn=8ddf87c62eddb1816b9a34957c26bd26380bc4365f411d92ac78192fe0cc93a6d58527104bc1be97226985556663a15b; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=tvLB2Vw7waoxWvoaqsjSKtIWNmYjYjXA; fid=93ee4b97-afe7-490e-83ff-aa600e1f0d10; ariaDefaultTheme=undefined; QN271=536176ba-7f89-4470-95a5-dce7f1c417e6; RT=s=1644848225742&r=https%3A%2F%2Fflight.qunar.com%2F; QN267=0166113199117ad63ce; _vi=QxvpgRSifpzfpW7SqPd1_z5J5xaasEcs2lw1_Rq6pVFvQKmOr3BcFn4ItgB1kfNc6_-4nTYkQGuxo6mMoCpIM-1DuxsABLYydotAvDE5ekRozNZfSN21bA3_fMpFqkAKRFGPV93XRUMlaFzodIfi5z6mT8HgB_Fhunc0SqOqnQuv',
    'referer': 'https://flight.qunar.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}


if __name__ == '__main__':
    main_url = 'https://ws.qunar.com/lowerPrice.jcp?&callback=DomesticLowPriceHome.showLowPrice'
    flight_info = []
    html = requests.get(main_url, headers=headers,  timeout=10)
    if html.status_code == 200:
        content = re.sub('^DomesticLowPriceHome\.showLowPrice\(|\)$', '', html.text)
        # print(content)
        data = json.loads(content)['data']
        log_str = 'Hi! I found the most affordable Hangzhou take-off ticket price here!!!!!\n'
        for city_name, info in data.items():
            if city_name != '杭州':
                continue
            records = info['records']
            records.sort(key=lambda x: int(x['price']), reverse=False)
            for record in records:
                log_str += '{},fly to {}，only need {}yuan\n'.format(record['date'],record['arrCity'],record['price'])
            robot_message(log_str)
    else:
        print('experied')



