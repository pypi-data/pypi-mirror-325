import urllib3
import requests
from ..spider_toolbox.requests_tools import retry_on_exception

# from spider_toolbox.requests_tools import retry_on_exception


# 禁用所有警告
urllib3.disable_warnings()
headers = {
    "Host": "pc.xn--pxt92gb0ku1kjqwf9h3sm.cn:11457",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) cyc-desktop/1.0.8 Chrome/128.0.6613.36 Electron/32.0.1 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"24\", \"Chromium\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "zh-CN",
    "priority": "u=1, i"
}

retry_time: int = 5


@retry_on_exception(retry_time)
def get_name(anime_url: str) -> str:
    url = f'https://pc.陕西省报废汽车.cn:11457/video/info/{anime_url}'
    resp = requests.get(url, verify=False, headers=headers).json()
    anime_name = resp['data']['vod_name']
    return anime_name


@retry_on_exception(retry_time)
def get_play_line(anime_url: str) -> str:  # 获取播放线路
    url = f'https://pc.陕西省报废汽车.cn:11457/video/info/{anime_url}'
    resp = requests.get(url, verify=False, headers=headers).json()
    play_line = resp['data']['vod_play_from'][0]['code']
    return play_line


@retry_on_exception(retry_time)
def get_chapter_title_url(anime_url: str) -> list[dict]:
    url = "https://pc.陕西省报废汽车.cn:11457/video/play_url"
    params = {
        "id": anime_url,
        "from": get_play_line(anime_url)
    }
    response = requests.get(url, params=params, headers=headers, verify=False)
    title_url_items = response.json()['data']
    return title_url_items


@retry_on_exception(retry_time)
def get_video_url(chapter_item):
    if chapter_item['needParse']:
        headers_ = {
            "authority": "json.xn--pxt92gb0ku1kjqwf9h3sm.cn",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        resp = requests.get(chapter_item['url'], headers=headers_, verify=False).json()
        chapter_video_links = resp['url']
    else:
        chapter_video_links = chapter_item['url']
    return chapter_video_links


@retry_on_exception(retry_time)
def search(keyword: str):
    url = "https://pc.陕西省报废汽车.cn:11457/video/search"
    params = {
        "text": keyword,
        "pg": "1",
        "limit": "30"
    }
    response = requests.get(url, headers=headers, params=params, verify=False).json()
    # print(response)
    return response['data']


if __name__ == '__main__':
    url = '660'
    # title_url_items, chapter_titles, chapter_urls = get_chapter_title_url(url)
    search('你好')
