邮箱="mail@emal.com"
密码="password"











assert 邮箱!="mail@emal.com", "请修改邮箱"
assert 密码!="password","请修改密码"

from selener.base import *
import time
track=["English"]
with LoginSearcher(r"https://canvas.instructure.com/login/canvas",login=0) as a:
    a.login(邮箱,密码,"电子邮件")
    a.wait_click(track)
    input()
