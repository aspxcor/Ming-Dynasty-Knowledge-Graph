import re
import time
WAITTIME=5
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class QHistory:
    def __init__(self,waitTime=22):
        self.Driver=Init(waitTime)

    def phrase(self):
        return Phrase(self.Driver.page_source.replace('\n',''))

    def Search(self,KeyWord):
        input_box = self.Driver.find_element_by_xpath(r"/html/body/div[1]/div/span/div/input")
        input_box.send_keys(KeyWord)
        time.sleep(WAITTIME)
        input_box.send_keys(Keys.ENTER)
        # search = self.Driver.find_element_by_xpath(r'/html/body/div[5]/div/div[1]/div/div')
        # search.click()
        time.sleep(WAITTIME)
        # print(self.Driver.page_source)
        return self.phrase()


def Init(waitTime):
    URL = r'https://www.allhistory.com/relationindex'
    #driver = webdriver.Chrome()
    #driver.maximize_window()  # 最大化浏览器
    #driver.implicitly_wait(waitTime)  # 设置隐式时间等待
    ####
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(waitTime)  # 设置隐式时间等待
    ####
    driver.get(URL)

    return driver

def Phrase(pages):
    relation = re.findall(r'<div class="relation-name">(.*?)</div>', pages)
    details = re.findall(r'<div class="detail">(.*?)<div class="c"></div>', pages)

    ra = []
    rb = []
    des = []
    for ss in details:
        a = re.findall(r'<div class="relation-a">(.*?)</div>', ss)[0]
        ra.append(a)
        b=re.findall(r'<div class="relation-b">(.*?)</div>', ss)[0]
        rb.append(b)
        des.append(FormatDescription(ss,a,b))
    if (len(relation)==len(ra)==len(rb)==len(des)):
        return len(relation),relation,ra,rb,des
    else:
        return 0,[],[],[],[]


def FormatDescription(ss,a,b):
    ss=ss.replace(' ', "")
    sublist = re.findall(r'<.*?>', ss)
    for s in sublist:
        ss = re.sub(s, "", ss)
    d = ss[len(a) + len(b):]
    d = re.sub("&nbsp;", "", d)
    return d

def getNames():
    ans=[]
    with open("names","r", encoding="utf-8") as f:
        fs=f.readlines()
        for s in fs:
            ans.append(s.split("，")[0])
    return ans