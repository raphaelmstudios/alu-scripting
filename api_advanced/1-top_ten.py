#!/usr/bin/python3
"""
1-top_ten
Queries Reddit API and prints titles of first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-api-advanced:v1.0 (by /u/alu_student)"
    }
    params = {"limit": 10}

    r = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False,
        timeout=10
    )

    if r.status_code != 200:
        print(None)
        return

    data = r.json().get("data", {})
    children = data.get("children", [])

    for post in children[:10]:
        title = post.get("data", {}).get("title")
        print(title)
