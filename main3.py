import requests
from bs4 import BeautifulSoup
from extruct import extract
from newspaper import Article
from w3lib.html import get_base_url
import json

def extract_full_content(url):

    # 使用真實的 User-Agent 來模擬瀏覽器請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    base_url = get_base_url(response.text, response.url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 用 extruct 提取結構化資料
    extracted_data = extract(response.text, base_url=base_url)

    json_ld = extracted_data.get('json-ld', [])
    og_data = extracted_data.get('opengraph', {})
    meta_data = soup.find('meta', attrs={'name': 'description'})
    print(json_ld)
    print(og_data)
    print(meta_data)
    # 用 newspaper 提取內文
    # article = Article(url)
    # article.download()
    # article.parse()

    # # 建立回傳的內容
    # result = {
    #     "title": article.title or og_data.get('og:title') or (json_ld[0].get('headline') if json_ld else None),
    #     "author": article.authors or (json_ld[0].get('author', {}).get('name') if json_ld else None),
    #     "published_date": article.publish_date or (json_ld[0].get('datePublished') if json_ld else None),
    #     "summary": article.summary or (meta_data.get('content') if meta_data else None),
    #     "image": article.top_image or og_data.get('og:image') or (json_ld[0].get('image') if json_ld else None),
    #     "content": article.text[:1000]  # 取前1000個字符
    # }

    return "result"

# 測試網址
url = 'https://tw.news.yahoo.com/%E6%9F%AF%E6%96%87%E5%93%B2%EF%BC%9A%E6%94%BF%E6%B2%BB%E7%8D%BB%E9%87%91%E5%A0%B1%E5%B8%B3%E5%BE%88%E4%BA%82%E4%BD%86%E6%B2%92%E6%9C%89%E6%84%8F%E5%9C%96%E4%BE%B5%E5%8D%A0-%E6%AA%A2%E5%AF%9F%E5%AE%98%E4%BB%A5%E9%9A%A8%E8%BA%AB%E7%A2%9F%E6%9C%89%E4%B8%8D%E9%9B%85%E7%89%87%E5%A8%81%E8%84%85%E6%88%91%E8%AA%8D%E7%BD%AA-003236357.html'
data = extract_full_content(url)
print(json.dumps(data, indent=4, ensure_ascii=False))
