from config import PROPERTIES_TO_KEEP_IN_EXCEL_FILE, SKIP_COMPANIES
from helpers import truncate_string, insert_at_first_position


def parse_data(data: list) -> list:
    pass

    not_filtered_data = [insert_at_first_position(d, 'applied', 'Nie') for i, d in enumerate(data)]

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
        item['jobTitle'] = truncate_string(str(item['jobTitle']), 30).upper() + '...' if len(
            str(item['jobTitle'])) >= 30 else str(item['jobTitle']).upper()
        item['companyName'] = truncate_string(str(item['companyName']), 15).upper() + '...' if len(
            str(item['companyName'])) >= 15 else str(item['companyName']).upper()

    return filtered_data
