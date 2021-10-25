import pymysql

class db:
    def __init__(self):
        self.db = pymysql.connect(host="10.214.131.232", user="eagle", password="eagle402", database="kg")


    def add(self,Table,names,values):
        sql= "insert into "+Table+names+" values"+values
        self.exe(sql)

    def delete(self,Table,name,value):
        sql="delete from "+Table+" where "+name+"="+value
        self.exe(sql)

    def update(self,Table,key,keyValue,name,value):
        sql = "update "+Table+" set "+name+"="+value+" where "+key+"="+keyValue
        self.exe(sql)
    def select(self,value,table):
        cursor = self.db.cursor()
        sql="select "+value+" from "+table+";"
        cursor.execute(sql)
        return cursor.fetchall()

    def exe(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
