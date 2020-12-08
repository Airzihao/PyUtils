edgePath = "D://dataset//edges-1k-wrapped.csv"
nodePath = "D://dataset//nodes-1k-wrapped.csv"
nodeHeadPath = "G://dataset//nodes-1k-wrapped-head.csv"
edgeHeadPath = "G://dataset//edges-1k-wrapped-head.csv"
neo4jRootPath = "";

databaseName = "graph-1B.db"


skipBadRelationships = False

neo4j_admin_bash = neo4jRootPath+"bin/neo4j-admin"

cmd = "{} import --database {} --nodes '{}' --nodes '{}' --relationships '{}' --relationships '{}'".format(neo4j_admin_bash, databaseName, nodeHeadPath, nodePath, edgeHeadPath, edgePath)

print(cmd)
# " bin/neo4j-admin import --nodes import/movies_header.csv,import/movies.csv \
# --nodes import/actors_header.csv,import/actors.csv \
# --relationships import/roles_header.csv,import/roles.csv"

# .\bin\neo4j-import
# --into data\databases\graph.db
# --nodes .\import\practice\actors.csv
# --nodes .\import\practice\movies.csv
# --relationships:ACTED_IN .\import\practice\roles.csv \--skip-duplicate-nodes=true --skip-bad-relationships= --stacktrace --bad-tolerance=500000