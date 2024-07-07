import pandas as pd
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter

from pracujpl_scrapper.helpers import object_with_id_exists, format_list

EXCEL_COLUMNS = {'offers': 'ID', 'lastPublicated': 'Opublikowane', 'companyName': 'Firma', 'jobTitle': 'Stanowisko',
                 'salaryDisplayText': 'Stawka', 'positionLevels': 'Poziom',
                 'url': 'Link'}
SHEET_NAME = 'Oferty pracy'


def adjust_column_width(workbook: Workbook, file_path: str) -> None:
    worksheet = workbook.active

    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                cell_length = len(str(cell.value))
                if cell_length > max_length:
                    max_length = cell_length
            except:
                pass
                print(f"Error: {cell.value}")
        worksheet.column_dimensions[column_letter].width = max_length + 1
    workbook.save(file_path)
    workbook.close()


def format_or_create_excel_table(writer: ExcelWriter, df: pd.DataFrame) -> None:
    worksheet = writer.sheets['Oferty pracy']
    (max_row, max_col) = df.shape
    column_settings = []
    for header in df.columns:
        column_settings.append({'header': header})
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
    writer.close()


def insert_rows_with_data(file_path, sheet_name, start_row, num_rows, data) -> None:
    wb = load_workbook(filename=file_path)
    ws = wb[sheet_name]
    ws.insert_rows(start_row, amount=num_rows)

    for row_index, row_data in enumerate(data, start=start_row):
        for col_index, cell_value in enumerate(row_data, start=1):
            ws.cell(row=row_index, column=col_index, value=cell_value)

    wb.save(file_path)


def save_new_data(file_path: str, data: list) -> None:
    pass

    workbook = load_workbook(file_path)
    worksheet = workbook.active
    data_to_pass = data.copy()
    ids_to_retain = set()

    for column in worksheet:
        id = column[0].value
        if id is None or id == 'ID':
            continue
        object_exists = object_with_id_exists(data, id, 'offers')
        if object_exists:
            ids_to_retain.add(int(id))
            continue

    data_to_pass = [obj for obj in data_to_pass if int(obj['offers']) not in ids_to_retain]

    if len(data_to_pass) == 0:
        print("No new data to save!")
        return

    start_row = 2
    number_of_rows = len(data_to_pass)
    data_to_insert = format_list(data_to_pass, list(EXCEL_COLUMNS.keys()))
    insert_rows_with_data(file_path, SHEET_NAME, start_row, number_of_rows, data_to_insert)
    print(f"Successfully saved {len(data_to_pass)} new rows!")


def new_excel_file_save(parsed_data: list, file_path: str) -> None:
    pass
    df = pd.DataFrame(parsed_data)
    df.rename(columns=EXCEL_COLUMNS, inplace=True)
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Oferty pracy", startrow=1, header=False, index=False)
    format_or_create_excel_table(writer, df)
