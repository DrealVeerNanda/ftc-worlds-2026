import requests
import json

url = "https://api.ftcscout.org/graphql"
query = """
query {
  teamByNumber(number: 16236) {
    name
    quickStats(season: 2023) {
      tot { value }
      auto { value }
      dc { value }
      eg { value }
    }
  }
}
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Content-Type': 'application/json'
}
res = requests.post(url, json={'query': query}, headers=headers, timeout=10)
print(res.status_code)
print(res.text[:1000])
