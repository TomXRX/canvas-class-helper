邮箱="mail@emal.com"
密码="password"











assert 邮箱!="mail@emal.com", "请修改邮箱"
assert 密码!="password","请修改密码"

from selener.base import *
import time
track=["English","Conferences",]
track2=["Join","Microphone"]
with LoginSearcher(r"https://canvas.instructure.com/login/canvas",login=0) as a:
    a.login(邮箱,密码,"电子邮件")
    a.wait_click(track)
    print("all done")
    print("waiting...")
    while 1:
        if a.wait_click(track2,check=2):break


    print("all done")
    print("DO NOT CLOSE THIS TERMINAL")
    while 0:
        try:
            input()
        except:pass
    input()
