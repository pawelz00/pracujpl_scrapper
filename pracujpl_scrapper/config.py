# Description: Configuration file for pracujpl_scrapper

# Site URL to scrap data from
BASE_URL = 'https://it.pracuj.pl/praca?et=1%2C17%2C4&itth=33'

# Web agent to use in requests
WEB_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

# Excel file configuration
EXCEL_COLUMNS = {'applied': 'Zaaplikowano', 'offers': 'ID', 'lastPublicated': 'Opublikowane', 'companyName': 'Firma',
                 'jobTitle': 'Stanowisko',
                 'salaryDisplayText': 'Stawka', 'positionLevels': 'Poziom',
                 'url': 'Link'}
SHEET_NAME = 'Oferty pracy'
PROPERTIES_TO_KEEP_IN_EXCEL_FILE = ['applied', 'offers', 'lastPublicated', 'jobTitle', 'companyName',
                                    'salaryDisplayText', 'positionLevels']

# Companies to not include in Excel file
SKIP_COMPANIES = ['MindPal', 'INNPRO ROBERT BŁĘDOWSKI sp. z o.o.']
