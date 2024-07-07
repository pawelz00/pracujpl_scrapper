import json
import re

from helpers import truncate_string

PROPERTIES_TO_KEEP_IN_EXCEL_FILE = ['offers', 'lastPublicated', 'jobTitle', 'companyName',
                                    'salaryDisplayText', 'positionLevels']
SKIP_COMPANIES = ['MindPal']


def parse_data(data: str) -> list:
    pass
    regex_pattern = r'<script\s+id="__NEXT_DATA__"\s+type="application/json">(.*?)</script>'
    match = re.search(regex_pattern, data)
    not_filtered_data = json.loads(match.group(1))[
        'props']['pageProps']['data']['jobOffers']['groupedOffers']

    filtered_data = [{key: offer[key] for key in PROPERTIES_TO_KEEP_IN_EXCEL_FILE}
                     for offer in not_filtered_data]

    # Filtering out companies
    filtered_data = [offer for offer in filtered_data if offer['companyName'] not in SKIP_COMPANIES]

    for item in filtered_data:
        item['lastPublicated'] = str(item['lastPublicated']).split('T')[0]
        item['positionLevels'] = str(item['positionLevels']).replace(
            '[', '').replace(']', '').replace("'", '')
        item['url'] = item['offers'][0]['offerAbsoluteUri']
        item['offers'] = item['offers'][0]['partitionId']
        item['jobTitle'] = truncate_string(str(item['jobTitle']), 20).upper() + '...' if len(
            str(item['jobTitle'])) >= 20 else str(item['jobTitle']).upper()
        item['companyName'] = truncate_string(str(item['companyName']), 15).upper() + '...' if len(
            str(item['companyName'])) >= 15 else str(item['companyName']).upper()

    return filtered_data
