import openpyxl
from openpyxl import workbook
def get_excel_data(sheetName,startRow,endRow,bodyColumn,expColumn):
    fileDir = r"../data/pytestApi.xlsx"
    wb = openpyxl.load_workbook(fileDir)
    sheet = wb.get_sheet_by_name(sheetName)
    dataList = []
    for i in range(startRow,endRow):
        bodyCell = sheet.cell(row=startRow,column =bodyColumn ).value
        expCell = sheet.cell(row=startRow,column =expColumn).value
        dataList.append([bodyCell.strip(),expCell.strip()])
    return dataList

get_excel_data("user",2,5,7,8)
