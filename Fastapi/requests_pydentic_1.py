import requests


rating = int(input("Input rating: "))

data = {
    "title": "The Age of AI",
    "context": "The Age of A.I. is an eight-episode American science documentary streaming television series narrated and hosted by American actor Robert Downey Jr. The show covers the applications of artificial intelligence (AI) in various fields, like health, robotics, space-travel, food, disaster-prevention, and others. Each 30-45 minute episode covers several different areas of AI implementation under one broader topic.",
    "rating": rating
}

r = requests.post("http://127.0.0.1:8000/posts", json=data)

print(f"Status Code: {r.status_code}, Response: {r.json()}")