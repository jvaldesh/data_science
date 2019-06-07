import requests
import json

def request(url, api_key):
    headers = {
        'cache-control': "no-cache"
    }

    url = url + "?sol={}&api_key={}".format("10", api_key)
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)

def build_web_page(fotos):
    html = "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<ul>"
    for foto in fotos['photos']:
        html += "\n\t\t\t<li><img src='{}'></li>".format(foto["img_src"])
    html += "\n\t\t</ul>\n\t</body>\n</html>"
    with open("fotos.html", "w") as f:
        f.write(html)

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "ziyMb60fKUpP09YPKhGenklqHb6Ouh95h8rDNn2A"
response = request(url, api_key)

build_web_page(response)
