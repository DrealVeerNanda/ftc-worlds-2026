import urllib.request
import re

for channel in ['FIRSTinspires', 'FIRSTTechChallenge']:
    url = f'https://www.youtube.com/@{channel}/streams'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        matches = re.findall(r'"videoId":"([a-zA-Z0-9_-]+)".*?"title":\{"runs":\[\{"text":"([^"]+)"', html)
        if matches:
            print(f"--- Channel: {channel} ---")
            seen = set()
            for vid, title in matches:
                if vid not in seen and "2026" in title and "Day 1" in title:
                    print(f"{vid}: {title}")
                    seen.add(vid)
    except Exception as e:
        print(f"Error on {channel}: {e}")
