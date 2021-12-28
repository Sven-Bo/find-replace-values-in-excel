import openpyxl

replacement_pair = {"Small Business": "Small Market", "Midmarket": "Midsize Market"}  # !!! Change this !!!

wb = openpyxl.load_workbook("Canada.xlsx")  # !!! Adjust file name !!!
for ws in wb.worksheets:
    # Iterate over the columns and rows, search for the text and replace
    for row in ws.iter_rows():
        for cell in row:
            if cell.value in replacement_pair.keys():
                cell.value = replacement_pair.get(cell.value)
wb.save("Canada_NEW.xlsx")