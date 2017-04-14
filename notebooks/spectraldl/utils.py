import urllib.request


def retrieve_url(url):
    with urllib.request.urlopen(url) as f:
        data = f.read()
    return data
