import urllib3
from bs4 import BeautifulSoup
def download_context(url):
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    response_data = response.data
    html_content = response_data.decode()
    return html_content


def save_to_file(filename,content):
    fo = open(filename,'w',encoding='utf-8')
    fo.write(content)
    fo.close()


def main():
    url = "https://knifefire.cn/2022/09/14/termux/"
    result = download_context(url)
    save_to_file("tips.html",result)


if __name__=='__main__':
    main()


def create_doc_from_filename(filenname):
    with open(filename,'r',encoding='utf-8') as f:
        html_content = f.read()
        doc = BeautifulSoup(html_content)
    return doc


def parse(doc):
    post_list = doc.find_all("a")[1]
    print(link.text.strip())
    print(link["href"])


def main():
    filename = "tips1.html"
    doc = create_doc_from_filename(filename)
    parse(doc)


if __name__=='__main__':
    main




