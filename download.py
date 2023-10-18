import redgifs
import requests


def download_redgifs(url, path):
    api = redgifs.API()
    api.login()
    if "//i." in url: # check if url uses short identifier and resolve to watch/ link
        response = requests.head(url, allow_redirects=True)
        url = response.url
    api.download(url, path)

def download_standard(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)

def download_universal(url, path):
    if "redgifs" in url:
        download_redgifs(url, path)
    else:
        download_standard(url, path)