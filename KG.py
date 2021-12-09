import pymysql

from py2neo import Graph, Node, Relationship



def read_mysql(sql):
    '''
       从mysql数据库中数据
       :param sql: sql查询语句
       :return: rows 查询结果
       '''
    #打开数据库连接
    dbconn = pymysql.connect(
        host="yourhost",
        database='yourdatabase',
        user='yourusername',
        password='yourpassword'
    )
    #创建游标对象
    cur=dbconn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取查询内容
    rows = cur.fetchall()
    print(rows)
    # 关闭数据库连接
    cur.close()
    dbconn.close()
    return rows

# sql = 'select * from relationship'
# read_mysql(sql)


# 从MySQL数据库中的types节点导入到neo4j
def get_nodes():
   name_type = dict()
   
   rows = read_mysql("SELECT distinct item,type FROM allItem")
   for row in rows:
      subject = process_string(row[0])
      subject_type = process_string(row[1])
      name_type[subject] = subject_type 

#    rows = read_mysql("SELECT distinct RB FROM relationship")
#    for row in rows:
#       subject = process_string(row[0])
#       subject_type = process_string(row[1])
#       name_type[subject] = subject_type 

   return name_type

def process_string(s):
    if s is None:
        return ""
    return  s.replace("-", "").replace("…", "").replace(" ", "")

# 连接Neo4j
graph = Graph('http://localhost:7474',auth=('neo4j','111'))
# 清除节点
graph.delete_all()

########################## 插入节点到Neo4j中 ##################################
node_name_type = get_nodes()
nodes = dict()   
for (node_name, node_type) in  node_name_type.items(): 
   node = Node(node_type, name=node_name)
   nodes[node_name] = node
   # print ke_node
   graph.create(node)

triples = read_mysql("SELECT RA, relationship, RB FROM relationship")
for triple in triples:
    # print network_row
    # 获取节点
    subject_node = nodes[process_string(triple[0])]
    object_node = nodes[process_string(triple[2])]
    relation_type = process_string(triple[1])
    properties = dict()
    
    print (subject_node)
    print (relation_type)
    print (object_node)
  
    print ("")
    # 关系创建
    subject_relation_object = Relationship(subject_node, relation_type, object_node, **properties)
    graph.create(subject_relation_object)

print ('关系创建完成')

