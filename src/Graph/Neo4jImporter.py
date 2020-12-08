edgePath = "D:\\dataset\\edges-1k-wrapped.csv"
nodePath = "D:\\dataset\\nodes-1k-wrapped.csv"
nodeHeadPath = "G:\\dataset\\nodes-1k-wrapped-head.csv"
edgeHeadPath = "G:\\dataset\\edges-1k-wrapped-head.csv"
neo4jRootPath = "";

databaseName = "graph-1B.db"


skipBadRelationships = False

neo4j_admin_bash = neo4jRootPath+"bin/neo4j-admin"

cmd = "{} import --database {} --nodes '{}' --nodes '{}' --relationships '{}' --relationships '{}'".format(neo4j_admin_bash, databaseName, nodeHeadPath, nodePath, edgeHeadPath, edgePath)

print(cmd)

# a works cmd:
#neo4j-admin import --database graph-1B.db --nodes "D:\\dataset\\nodes-1k-wrapped-head.csv,D:\\dataset\\nodes-1k-wrapped.csv" --relationships "D:\dataset\edges-1k-wrapped-head.csv,D:\dataset\edges-1k-wrapped.csv"