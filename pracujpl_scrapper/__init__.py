import os

from pracujpl_scrapper.data_parser import parse_data
from pracujpl_scrapper.excel_functions import save_new_data, new_excel_file_save, adjust_column_width, \
    apply_row_color_pattern
from pracujpl_scrapper.scrapper import scrap_data


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

    try:
        if file_exists:
            pass
            res = save_new_data(file_path, parsed_data)

            if not res:
                return

            print("New data saved successfully!")
        else:
            pass
            new_excel_file_save(parsed_data, file_path)
            print("Data saved successfully!")
    except Exception as e:
        print(f"Error: {e}")
        return

    apply_row_color_pattern(file_path)
    adjust_column_width(file_path)

    return 0


if __name__ == '__main__':
    main()
