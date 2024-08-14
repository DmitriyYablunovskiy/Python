import requests

def download_image2(url, filename=None):
    response = requests.get(url)
    print(response.content)

url = 'https://www.python.org/static/img/python-logo@2x.png'

download_image2(url)


