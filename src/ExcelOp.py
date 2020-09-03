import pandas as pd
import collections

resourceDir = "./DataResources"


def getSheetByName(name: str):
    return pd.read_excel(resourceDir+'/input template.xlsx', sheet_name=name)

# row counts without the head row
def getSheetRowsNum(df):
    return df.shape[0]
def getSheetColsNum(df):
    return df.shape[1]

def getSpecRow(sheet, num: int):
    return sheet.ix[num].values
def getSpecCol(sheet, colName: str):
    return sheet[colName].values

Refer2_BP_User = getSheetByName('Refer2_BP User')
Step_1_SoD_Remediation_Review = getSheetByName('Step 1 SoD Remediation Review')
Refer3_Tcode_usage = getSheetByName('Refer3_Tcode usage')

rows = getSheetRowsNum(Step_1_SoD_Remediation_Review)

cols = getSheetColsNum(Step_1_SoD_Remediation_Review)

userList = getSpecCol(Step_1_SoD_Remediation_Review, 'User Name')
positionRoleList = getSpecCol(Step_1_SoD_Remediation_Review, 'Position role')


def step1():
    sheet1 = Step_1_SoD_Remediation_Review
    sheet1['step1Key'] = sheet1['User Name']+sheet1['Tcode']
    sheet2 = Refer3_Tcode_usage
    sheet2['step1Key'] = sheet2['User Name']+sheet2['Transaction Code']
    merged = pd.merge(sheet1, sheet2, left_on=['User Name', 'Tcode'], right_on=['User Name', 'Transaction Code'])
    tempSheet=
    finalMerged = pd.merge(sheet1, tempSheet)

    return finalMerged


print(step1())

# def wrapDict(col1, col2):
#     dictionary = collections.OrderedDict()
#     length = len(col1)
#     i = 0
#     if i < length:
#         dictionary[col1[i]] = col2[i]
#         i += 1
#
