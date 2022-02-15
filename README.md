# flight_discount_info_push
This tiny project is aimed at using your own robot to send the most affordable price of ticket by app.       



## Table of Contents

- [Background](#background)
- [Install](#install)
- [Use](#use)
- [API](#api)
- [Version](#version)



## Background
Hi there, have you ever worried about whether you'll be able to get a low-cost ticket in time?        
Have you ever picked a specific destination but waited for the best price to come along and you miss the best price in the end?     
And I have to admit that it always happens!   
So, in order to solve this problem, I write a tiny program to send the affordable price of ticket to you guys!  

## Install

See requirements.txt, it contains all of the required dependencies and their version numbers.
## Use
If you want this program to run periodically, you can put the python file into your server and let it run on the server automatically.
- Upload python file into server.
- Create a sh file under the same directory of python file, and write some shell scripts as below into sh file. Dont't forget to change your own path and name of file.
```
#!/bin/bash
cd /home/python_project/jianing/message_flight_push
ps -ef | grep flight_monitor_qn.py |grep -v grep | awk '{print $2}'| xargs kill -9

sleep 1s

nohup python -u flight_monitor_qn.py > flight_monitor_qn.log 2>&1 &
```
- Create crontab timed tasks, for more information about crontab, please see [here](https://www.computerhope.com/unix/ucrontab.htm)
```
crontab -e
```


## API
For V1.0: https://ws.qunar.com/lowerPrice.jcp?&callback=DomesticLowPriceHome.showLowPrice  btw, thank you Quna:)


## Version
### V1.0 (2022.02.15)
I choose Dingding is because it has open Webhook for free, you can change it into other app which has the similar function as you want.    
I choose Quna web is because it is almost the only one OTA Website that its data can be crawled, frankly speaking, I also tried Xiecheng, Feizhu ant etc. Finally, I found Quna is the most friendly one to me.  
According to what I said before, this program is for Chinese airline. But I just want to say, maybe I will enlarge my program to overseas website in some day:)




