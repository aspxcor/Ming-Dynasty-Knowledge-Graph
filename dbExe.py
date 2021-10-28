import pymysql

class db:
    def __init__(self):
        self.db = pymysql.connect(host="10.214.131.232", user="eagle", password="eagle402", database="kg")


    def add(self,Table,names,values):
        sql= "insert into "+Table+names+" values"+values
        self.exe(sql)

    def delete(self,Table,name,value):
        sql="delete from "+Table+" where "+name+"="+"'"+value+"'"
        self.exe(sql)

    def update(self,Table,key,keyValue,name,value):
        sql = "update "+Table+" set "+name+"="+value+" where "+key+"="+keyValue
        self.exe(sql)
    def select(self,value,table,where=""):
        cursor = self.db.cursor()
        sql="select "+value+" from "+table+where+";"
        cursor.execute(sql)
        return cursor.fetchall()

    def exe(self,sql):
        print(sql)
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

def encode(ss):
    ss.replace("\\", "\\\\")
    ss.replace("'", "\\'")
    return ss

def decode(ss):
    ss.replace("\\\\", "\\")
    ss.replace("\\'", "'")
    return ss

def combineData(DataList):
    ans=""
    for data in DataList:
        data=encode(data)
        ans+="'"+data+"',"
    return " ("+ans[:-1]+")"

def combineKey(KeyList):
    ans=""
    for key in KeyList:
        key=encode(key)
        ans+=key+","
    return " ("+ans[:-1]+")"