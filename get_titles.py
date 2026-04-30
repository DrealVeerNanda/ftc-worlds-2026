import urllib.request
import re

ids = ['MeaiooVeA70', 'KbMURIWFcMg', 'ZEzRZXUkgEI', 'Yd5q_PokJ0Y', 'oTLneTQGnsM', 'v_KlA02le9g']
for vid in ids:
    url = f'https://www.youtube.com/watch?v={vid}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<title>(.*?)</title>', html)
        if match:
            print(f"{vid}: {match.group(1)}")
    except Exception as e:
        print(f"Error on {vid}: {e}")
