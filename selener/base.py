import selenium
from selenium.common import exceptions
class Searcher:
    def __init__(self,link,debug=True,wait=10):
        self.driver=self.drive(headless=not debug)
        self.driver.get("http://127.0.0.1")
        # self.driver.implicitly_wait(wait)
        self.driver.set_page_load_timeout(wait)
        try:
            self.driver.get(link)
        except Exception as e:
            if e==exceptions.TimeoutException:pass
            else:
                print(e)
                print("invalid argument? forget http://  ?")
    def drive(self,drive="C",headless=False):
        import re
        from selenium import webdriver
        if re.match(drive,"Chrome",re.IGNORECASE):
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        if re.match(drive, "Chrome", re.IGNORECASE):
            return webdriver.Chrome(options=options)
        else:
            return webdriver.Firefox(options=options)

    def finder(self, search,ret=False,strict=False,inside=None):
        if not inside:inside=self.driver
        if strict:q = inside.find_elements_by_xpath("//*[text()='" + search + "']")
        else:q = inside.find_elements_by_xpath("//*[contains(text(),'" + search + "')]")
        for k in q:
            if not k.is_displayed(): continue
            if ret:
                yield k
                continue
            print(k.text, end="    ")
            print(k.get_attribute("href"))

    def attr_finder(self,search,ret=True,inside=None):
        if not inside:inside=self.driver
        for k in inside.find_elements_by_xpath('//*[@*="' + search + '"]'):
            if not k.is_displayed(): continue
            yield k

    def close(self):
        self.driver.close()
        self.driver.quit()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class AdvancedSearcher(Searcher):
    def switcher(self,excute,*list,**args):
        yield excute(*list,**args)
        if len(self.driver.find_elements_by_tag_name("iframe")):
            for k in self.driver.find_elements_by_tag_name("iframe"):
                self.driver.switch_to.frame(k)
                yield from self.switcher(excute,*list,**args)
                self.driver.switch_to.parent_frame()

    def brother_finder(self,element,need,needparm=None,tr=5):
        for k in range(tr):
            element=element.find_element_by_xpath("..")
            try:
                if needparm==None:return need(element)
                return need(element,needparm)
            except Exception as e:
                pass
                # print(e)
            
            # try:
                # if need
            #↓↓
    def brother_text_finder(self,element,tr=5):
        A=element.text
        for k in range(tr):
            element=element.find_element_by_xpath("..")
            if A!=element.text:break
        else:return False
        return element
            
from selenium import webdriver



class AdvancedSearcherer(AdvancedSearcher):
    def finder(self,*list,inside=None,**dict):
        if inside:return super().finder(list)
        return self.switcher(super().finder,*list,**dict)
    def attr_finder(self,*list,old=False,**dict):
        if old:
            return super().attr_finder(*list,**dict)
        return self.switcher(super().attr_finder,*list,**dict)
    
    
    def advanced_finder(self,*args,typ="input",tr=2,**kwargs):
        if len(args)==2:typ=args[1]
        N=self.advanced_finder_(*args,**kwargs)
        if N:
            return self.brother_finder(N,webdriver.Chrome.find_element_by_tag_name,typ,tr)

    def advanced_finder_(self,*args,**kwargs):
        need=args[0]
        if type(need)==list:
            for k in need:
                i=self.advanced_finder_(k,**kwargs)
                if i:return i
        else:
            B=None
            if not kwargs:
                for k in self.finder(need,True,True):
                    for a in k:
                        B=a
                        break
                    if B: break
            if not B:
                for k in self.attr_finder(need,**kwargs):
                    for a in k:
                        B = a
                        break
                    if B: break
            if not B:
                for k in self.finder(need, True):
                    for a in k:
                        B = a
                        break
                    if B: break

            return B

import time
from selenium.common.exceptions import *
import selenium.webdriver.remote.webelement as webelement
class Performer(Searcher):

    def scroll_down_click(self, get, scrolls=5):
        if type(get)==list:
            for k in get:
                self.scroll_down_click(k)
            return
        assert type(get) == str
        get = self.advanced_finder_(get)
        for i in range(scrolls):
            try:
                get.click()
            except:
                self.driver.execute_script("window.scrollBy(0,300)")
    def wait_click(self,get,timeout=5,check=0.5):
        if type(get)==list:
            ret=None
            for k in get:
                if self.wait_click(k):ret=True
            return ret
        assert type(get) == str
        for k in range(int(timeout/check)):
            g = self.advanced_finder_(get)
            try:
                self.advance_click(g)
                break
            except Exception as e:
                pass
                # print(e)
            print(".",end="")
            time.sleep(check)
        else:return 
        return True
    def advance_click(self,element):
        try:element.click()
        except ElementClickInterceptedException:
            self.brother_finder(element,webelement.WebElement.click)

class LoginSearcher(AdvancedSearcherer,Performer):
    def __init__(self,*lis,login=1,usr=None,password=None,**dic):
        super().__init__(*lis,**dic)
        if login:self.login(usr,password)
    def drive(self,drive="C",user_profile=False,headless=False):
        if not user_profile:return super().drive(drive,headless)
        import re
        from selenium import webdriver
        if re.match(drive,"Chrome",re.IGNORECASE):
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        options.add_argument(r"user-data-dir=C:\Program Files (x86)\Google\Chrome\User Data")
        options.binary_location=r"C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
        if re.match(drive, "Chrome", re.IGNORECASE):
            return webdriver.Chrome(chrome_options=options)
        else:
            return webdriver.Firefox(options=options)
    
    def login(self,usr=None,password=None,usr_find=list()):
        from selenium.webdriver.common.keys import Keys
        if usr:
            if type(usr_find)==str:usr_find=[usr_find]
            usr_find.extend(["用户名","username"])
            B=self.advanced_finder(usr_find[::-1])
            if not B:return False
            B.send_keys(Keys.CONTROL, "a")
            B.send_keys(usr)
        if password:
            B =self.advanced_finder(["密码","password"][::-1])
            if not B: return False
            B.send_keys(password)
        # N=self.attr_finder("登录",old=True)
        # if not N:N=self.attr_finder("login",old=True)
        # N[0].click()
        N=self.advanced_finder(["login","登录","Log In"],"button")
        if N:
            try:N.click()
            except TimeoutException:pass


if __name__ == '__main__':

    pass
    # from selenium.webdriver.common.action_chains import ActionChains
