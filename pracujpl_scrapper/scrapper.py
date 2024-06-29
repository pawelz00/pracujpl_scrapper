import requests


def scrap_data() -> str:
    pass
    try:
        url = 'https://it.pracuj.pl/praca?et=1%2C17%2C4&pn=1&itth=33'
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        response = requests.get(url, headers={'User-Agent': agent})
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return ""


if __name__ == '__main__':
    scrap_data()
