import jieba.posseg as psg
import dbExe

db = dbExe.db() 
tmpList=list(db.select("item","allItem"," where type is null"))
toSearchItemList=[]
for item in tmpList:
    toSearchItemList.append(item[0])
for item in toSearchItemList:
    analyse=psg.cut(item)
    for i in analyse:
        if(i.flag=='nr'):
            db.update("allItem","item","'"+str(item)+"'","type","'历史人物'")
            print(item+"为历史人物，已更新！")
        if(i.flag=='ns'):
            db.update("allItem","item","'"+str(item)+"'","type","'地点'")
            print(item+"为地点，已更新！")
    # print("\n")