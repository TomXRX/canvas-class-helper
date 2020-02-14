from selener.base import *


Time="7:59"
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

track2=["No"]
with LoginSearcher(r"https://ke.qq.com/",login=0) as a:
    a.wait_click(["登录","QQ登录"])
    a.wait_click("link",text="账号密码登录")
    a.login(账号,密码)
    a.wait_click("btn",id="login_button")
    a.wait_click("下次再选",check=0.5,timeout=2)
    a.wait_click("门课程",type="a")
    a.wait_click("门课程")#不太懂但是两个都要
    a.driver.switch_to.window(a.driver.window_handles[0])
    a.driver.close()
    a.driver.switch_to.window(a.driver.window_handles[0])
    a.wait_click("我知道了",check=0.5,timeout=2)
    "进入直播"
    while 0:
        if a.wait_click(track2,check=2,timeout=30):break
        a.driver.refresh()

    print("all done")
    print("DO NOT CLOSE THIS TERMINAL")
    while 0:
        try:
            input()
        except:pass
    input()
