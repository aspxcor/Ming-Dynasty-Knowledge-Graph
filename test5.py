import dbExe
import urllib.request
import urllib.parse
import time
from lxml import etree

def query(content):
    # 请求地址
    url = 'https://baike.baidu.com/item/' + urllib.parse.quote(content)
    # 请求头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 利用请求地址和请求头部构造请求对象
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    # 发送请求，获得响应
    response = urllib.request.urlopen(req)
    # 读取响应，获得文本
    text = response.read().decode('utf-8')
    # 构造 _Element 对象
    html = etree.HTML(text)
    # 使用 xpath 匹配数据，得到匹配字符串列表
    sen_list = html.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
    # 过滤数据，去掉空白
    sen_list_after_filter = [item.strip('\n') for item in sen_list]
    # 将字符串列表连成字符串并返回
    return ''.join(sen_list_after_filter)

if __name__ == '__main__':
    db = dbExe.db()
    tmpList=list(db.select("item","toSearch"))
    toSearchItemList=[]
    for item in tmpList:
        toSearchItemList.append(item[0])
    # print(toSearchItemList)
    for item in toSearchItemList:
        time.sleep(10)
        result = query(item)
        keyWordForMingDynasty=['明朝','明代','明末','明初','洪武','建文','永乐','洪熙','宣德','正统','景泰','天顺','成化','弘治','正德','嘉靖','隆庆','万历','泰昌','天启','崇祯']
        if(any(keyWord in result for keyWord in keyWordForMingDynasty)):
            #匹配到明朝信息
            print(item + " is things in Ming dynasty.")
        else:
            db.delete("toSearch","item",str(item))
            print(item+" has been deleted since it's not things in Ming dynasty. The description of "+item+" is just here:\n"+result)