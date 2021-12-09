import dbExe


ra='朱元璋'
relationship="辅佐"
rb="刘伯温"
des="刘伯温以辅佐明太祖朱元璋完成帝业、开创明朝并保持国家安定，因而驰名天下，被后人比作为诸葛武侯。刘伯温以辅佐明太祖朱元璋完成帝业、开创明朝并保持国家安定，因而驰名天下，被后人比作为诸葛武侯。"
#
db=dbExe.db()
db.add("relationship",dbExe.combineKey(["RA","RB","relationship","description"]),dbExe.combineData([ra,rb,relationship,des]))
