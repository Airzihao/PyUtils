confFilePath = "./conf.conf"
confDict = {}
def init(confDict):
    with open(confFilePath, "r", encoding='utf-8') as conf:
        for line in conf:
            (key, value) = line.replace(" ", "").split("=")
            confDict[key] = value

init(confDict)
print(confDict['modelDirPath'])
