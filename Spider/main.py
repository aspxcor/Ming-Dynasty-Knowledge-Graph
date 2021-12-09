import time

from selenium import webdriver
import re
import Utils

URL = r'https://www.allhistory.com/relation?id=57c3ce8c0bd1beaa7ca0bda6'
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(12)  # 设置隐式时间等待
driver.get(URL)
# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=options)


time.sleep(3)


pages=driver.page_source.replace('\n',' ')
print(pages)
n,r,ra,rb,d=Utils.Phrase(pages)
print(n)
for i in range(n):
    print(ra[i], '--', r[i], '--', rb[i], ':', d[i])
# print(pages)
# print("-------------------------------------------------------")
# relation =re.findall(r'<div class="relation-name">(.*?)</div>',pages)
# details=re.findall(r'<div class="detail">(.*?)<div class="c"></div>',pages)
# ra=[]
# rb=[]
# des=[]
# for ss in details:
#     a=re.findall(r'<div class="relation-a">(.*?)</div>',ss)[0]
#     ra.append(a)
#     rb.append(re.findall(r'<div class="relation-b">(.*?)</div>',ss)[0])
#     des.append(re.sub(r'[A-Za-z0-9\!\%\[\]\,\=\<\>\"\/\_\:\.\&\;]',"",ss).replace(" ",""))
# print(len(relation),len(ra),len(rb),len(des))
# for i in range(len(relation)):
#     print(ra[i],'--',relation[i],'--',rb[i],':',des[i])

driver.quit()