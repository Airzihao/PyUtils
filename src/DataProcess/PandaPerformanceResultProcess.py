import json
import sys,os
import tablib

resourceDir = "D:\PySpace\PyUtils\DataResource\PandaPerformanceResult"


def getAllFiles(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            getAllFiles(cur_path, all_files)
        else:
            all_files.append(cur_path.replace("\\", "/"))
    return all_files

def extractJsonFile(filePath):
    jsonItemList = []

    with open(filePath, "r", encoding='utf-8') as file:
        i=0
        print(filePath)
        for line in file:
            if i<11:
                jsonItem = json.loads(line)
                jsonItemList.append(jsonItem)
                i+=1
            else:
                totalTime = int(line.split(':')[1])

    return (jsonItemList, totalTime)

def writeToExcel(jsonItemList, totalTime, excelFilePath):
    header1 = tuple([i for i in jsonItemList[0].keys()])
    header2 = ('timeout', "finishTime")
    header = header1 + header2

    data = []
    for json in jsonItemList:
        body = []
        timeout=False
        for v in json.values():
            body.append(v)
            if(v==-1):
                timeout = True
        body.append(timeout)
        body.append(totalTime)
        data.append(tuple(body))

    data = tablib.Dataset(*data, headers=header)

    open(excelFilePath, 'wb+').write(data.xls)

if __name__ == '__main__':
    resourceDir = "D:\PySpace\PyUtils\DataResource\PandaPerformanceResult"

    allRecordFiles = getAllFiles(resourceDir, [])
    neo4jRecordFiles = []
    pandaRecordFiles = []
    for item in allRecordFiles:
        if str(item).__contains__("neo4j"):
            neo4jRecordFiles.append(item)
        if str(item).__contains__("panda"):
            pandaRecordFiles.append(item)

    i = 1
    for neo4j in neo4jRecordFiles:
        result = extractJsonFile(neo4j)
        excelFileName = "D:\PySpace\PyUtils\DataResource\output"+ "/neo4j"+str(i)+".xls"
        writeToExcel(result[0], result[1], excelFileName)
        i += 1
    i = 1
    for panda in pandaRecordFiles:
        result = extractJsonFile(panda)
        excelFileName="D:\PySpace\PyUtils\DataResource\output"+"/panda"+str(i)+".xls"
        writeToExcel(result[0], result[1], excelFileName)
        i += 1
