edgePath = "D:\\dataset\\graph500-22-wrapped.csv"
nodePath = "D:\\dataset\\graph500-22_unique_node-wrapped.csv"
neo4jRootPath = "";

databaseName = "graph-501.db"


skipBadRelationships = False

neo4j_admin_bash = neo4jRootPath+"bin/neo4j-admin"

cmd = "{} import --database {} --nodes {} --relationships {}".format(neo4j_admin_bash, databaseName, nodePath, edgePath)

print(cmd)
# " bin/neo4j-admin import --nodes import/movies_header.csv,import/movies.csv \
# --nodes import/actors_header.csv,import/actors.csv \
# --relationships import/roles_header.csv,import/roles.csv"

# .\bin\neo4j-import
# --into data\databases\graph.db
# --nodes .\import\practice\actors.csv
# --nodes .\import\practice\movies.csv
# --relationships:ACTED_IN .\import\practice\roles.csv \--skip-duplicate-nodes=true --skip-bad-relationships= --stacktrace --bad-tolerance=500000