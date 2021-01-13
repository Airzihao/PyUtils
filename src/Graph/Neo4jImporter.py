import os
import sys

neo4jRootPath = ""
databaseName = ""
delimiter = "|"
array_delimiter = ","
skipBadRelationships = False

def abslouteFilePath(path):
    listdir = os.listdir(path)
    filepath = path
    allfile = []
    for file in listdir:
        allfile.append(filepath + '/' + file)
    return allfile

def getAllfilesAsStr(allfile, mode):
    prefix = ""
    if mode=="node":
        prefix = "--nodes="
    if mode== "relation":
        prefix = "--relationships="
    finalResult = ""
    for file in allfile:
        finalResult += (prefix + file + " ")
    finalResult
    return str(finalResult)



# a works cmd:
#neo4j-admin import --database graph-1B.db --nodes "D:\\dataset\\nodes-1k-wrapped-head.csv,D:\\dataset\\nodes-1k-wrapped.csv" --relationships "D:\dataset\edges-1k-wrapped-head.csv,D:\dataset\edges-1k-wrapped.csv"
# neo4j-admin import --database graph-1B.db --nodes "G:\\dataset\\nodes-1k-wrapped-head.csv,G:\\dataset\\nodes-1B-wrapped.csv" --relationships "G:\dataset\edges-1k-wrapped-head.csv,G:\dataset\edges-1B-wrapped.csv"

if __name__ == '__main__':
    targetDir = os.path.abspath(sys.argv[1])
    neo4jRootPath = os.path.abspath(sys.argv[2])
    databaseName = sys.argv[3]
    neo4j_admin_bash = os.path.join(neo4jRootPath, "bin/neo4j-admin")

    targetNodeDir = os.path.join(targetDir, "nodes")
    targetRelDir = os.path.join(targetDir, "relations")

    allNodeFilesStr = getAllfilesAsStr(abslouteFilePath(targetNodeDir), "node")
    allRelFilesStr = getAllfilesAsStr(abslouteFilePath(targetRelDir), "relation")
    cmd = "{} import --database {} {} {} --delimiter \"{}\" --array-delimiter \"{}\"".format(neo4j_admin_bash, databaseName,
                                                                                 allNodeFilesStr, allRelFilesStr, delimiter, array_delimiter)
    print(cmd)