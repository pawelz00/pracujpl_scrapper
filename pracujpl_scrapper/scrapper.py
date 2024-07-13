import requests

from config import SITE_URL, WEB_AGENT


def scrap_data() -> str:
    pass
    try:
        response = requests.get(SITE_URL, headers={'User-Agent': WEB_AGENT})
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return ""


def main():
    pass
    data = scrap_data()
    print(data)


if __name__ == '__main__':
    main()
