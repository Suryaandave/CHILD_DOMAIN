import requests
import re
from urllib.parse import urljoin


target_url = "<target_url>"


def externel_link(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))


href_link = externel_link(target_url)
for l in href_link:
    l = urljoin(target_url, l)
    print(l)
