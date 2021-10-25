import pymysql

import dbExe

a="*"
b="kg.validRelationship"
db=dbExe.db()
# db.add(Table="validRelationship",names="(valid)",values=r'("父子4")')
# db.delete(Table="validRelationship",name="valid",value=r'"父子4"')
print(db.select(a,b))