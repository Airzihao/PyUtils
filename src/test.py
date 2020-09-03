import pandas as pd

resourceDir = "./DataResources"

def getSheetByName(name: str):
    return pd.read_excel(resourceDir+'/test.xlsx', sheet_name=name)

# row counts without the head row
def getSheetRowsNum(df):
    return df.shape[0]
def getSheetColsNum(df):
    return df.shape[1]

def getSpecRow(sheet, num: int):
    return sheet.ix[num].values
def getSpecCol(sheet, colName: str):
    return sheet[colName].values


s1 = getSheetByName('s1')
q_q = getSpecCol(s1, 'aa')
