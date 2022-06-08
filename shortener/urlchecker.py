import requests


def check_url(url ):
    try:
        response = requests.head(url=url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False