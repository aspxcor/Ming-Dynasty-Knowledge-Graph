import Utils
import dbExe
output=[]
name="朱元璋"
def traversal(name):
    qh=Utils.QHistory(10)
    n,r,ra,rb,des=qh.Search(name)
    for i in range(n):
        output.append([ra[i],rb[i],r[i],des[i]])
        print(ra[i],'--',r[i],'--',rb[i],':',des[i])
def init():
    traversal(name)
    output_copy=output
    for i in range(len(output_copy)):
        traversal(output_copy[i][1])
        print(output)
    db = dbExe.db()

    insert_relationship(db)
    insert_toSearch(db)
def insert_relationship(db):
    for i in range(len(output)):
        add_values="("+output[i][0]+","+output[i][1]+","+output[i][2]+","+output[i][3]+")"
        db.add("relationship","(ra,rb,relationship.description)",add_values)
def insert_toSearch(db):
    for i in range(len(output)):
        try:
            add_values =output[i][0]
            db.add("toSearch", "(item)", add_values)
        except:
            print(0)
        try:
            add_values =output[i][1]
            db.add("toSearch", "(item)", add_values)
        except:
            print(0)
init()
