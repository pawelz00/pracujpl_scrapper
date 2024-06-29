import os
from openpyxl import load_workbook
from pracujpl_scrapper.excel_functions import save_new_data, new_excel_file_save, adjust_column_width
from pracujpl_scrapper.scrapper import scrap_data
from pracujpl_scrapper.data_parser import parse_data


def main():
    data_from_site = scrap_data()

    if data_from_site == "":
        return "Error: No data from site!"

    parsed_data = parse_data(data_from_site)

    # Checking
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    excel_file_name = 'OfertyPracy.xlsx'
    file_path = os.path.join(folder_path, excel_file_name)
    file_exists = os.path.exists(file_path)

    # Saving data to excel file
    try:
        if file_exists:
            pass
            save_new_data(file_path, parsed_data)
            print("New data saved successfully!")
        else:
            pass
            new_excel_file_save(parsed_data, file_path)
            print("Data saved successfully!")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Adjusting column width
    workbook = load_workbook(file_path)
    adjust_column_width(workbook, file_path)

    return 0


if __name__ == '__main__':
    main()
