import time

import Utils
import dbExe
output=[]
name=Utils.getNames()
def traversal(name):
    qh=Utils.QHistory(10)
    n,r,ra,rb,des=qh.Search(name)
    db = dbExe.db()
    for i in range(n):
        output.append([ra[i],rb[i],r[i],des[i]])
        add_values="("+ra[i]+","+rb[i]+","+r[i]+","+des[i]+")"
        print(add_values)

        try:
            db.add("relationship", dbExe.combineKey(["RA", "RB", "relationship", "description"]),
                   dbExe.combineData([ra[i], rb[i], r[i], des[i]]))


            db.add("toSearch", dbExe.combineKey(["item"]), dbExe.combineData([ra[i]]))
        except:
            print(0)
        try:

            db.add("toSearch", dbExe.combineKey(["item"]), dbExe.combineData([rb[i]]))
        except:
            print(0)
        
def init():
    for na in name:
        traversal(na)
        output_copy = output
        for i in range(len(output_copy)):
            traversal(output_copy[i][1])
        time.sleep(5)

init()
