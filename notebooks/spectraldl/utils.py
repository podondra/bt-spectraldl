import urllib.request


def retrieve_url(url):
    with urlib.request.urlopen(url) as f:
        data = f.read()
    return data
