import json
import re
import time

import requests

from config import WEB_AGENT, BASE_URL


def scrap_data() -> list:
    pass
    try:
        data = []
        page_number = 1
        first_request = True

        while True:
            if first_request is False:
                print("Waiting 2 seconds before next request...")
                time.sleep(2)

            response = requests.get(f"{BASE_URL}&pn={page_number}", headers={'User-Agent': WEB_AGENT})
            regex_pattern = r'<script\s+id="__NEXT_DATA__"\s+type="application/json">(.*?)</script>'
            match = re.search(regex_pattern, response.text)
            array_data = json.loads(match.group(1))[
                'props']['pageProps']['data']['jobOffers']['groupedOffers']

            if len(array_data) == 0:
                break

            data.extend(array_data)
            first_request = False
            print(f"Page {page_number} scrapped successfully!")
            page_number += 1

        print("Data scrapped successfully!")
        return data

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    pass
    data = scrap_data()
    print(data)


if __name__ == '__main__':
    main()
