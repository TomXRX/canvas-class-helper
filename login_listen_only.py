邮箱="mail@email.com"
密码="password"
课程="class"
#写部分名称用于匹配即可
系统语言="中文"









assert 邮箱!="mail@email.com", "请修改邮箱"
assert 密码!="password","请修改密码"
assert 课程!="class","请修改课程"

from selener.base import *

Time="8:45"
#使用电脑的系统时间
import time,datetime
def alarm(Time):
                cycle=24*60*60
                assert len(Time) >= 4
                if len(Time) <= 5: Time = Time + time.strftime(":%S")
                if len(Time) < 10: Time = time.strftime('%Y-%m-%d ') + Time
                Time = time.mktime(time.strptime(Time, '%Y-%m-%d %H:%M:%S'))
                Time = Time - time.mktime(datetime.datetime.now().timetuple())
                if Time <= 0: Time += cycle
                return Time
if 0:
    if alarm(Time) - 60 * 10 > 0:

        time.sleep(alarm(Time) - 60 * 10)

        print("start in 10 min")
        time.sleep(60 * 10)
    else:
        time.sleep(alarm(Time) - 60 * 10)

print("start")

track=[课程,"Conferences",]
if 系统语言=="中文":track2=["Join","仅聆听"]
else:track2=["Join","only"]
with LoginSearcher(r"https://canvas.instructure.com/login/canvas",login=0,wait=100) as a:
    a.login(邮箱,密码,"电子邮件")
    a.wait_click(track)
    print("all done")
    print("waiting...",end="")
    while 1:
        if a.wait_click(track2,check=2,timeout=30):break
        a.driver.refresh()
    a.driver.switch_to_window(a.driver.window_handles[1])
    a.wait_click(track2)
    print("all done")
    print("DO NOT CLOSE THIS TERMINAL")
    while 0:
        try:
            input()
        except:pass
    input()
