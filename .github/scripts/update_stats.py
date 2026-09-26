import os
import requests
import json
from datetime import datetime

USERNAME = "Nishant052004"

def fetch_user_summary():
    headers = {"User-Agent": "Nishant-Profile-Updater"}
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            repos = response.json()
            total_stars = sum(r.get("stargazers_count", 0) for r in repos)
            total_forks = sum(r.get("forks_count", 0) for r in repos)
            public_repos = len(repos)
            print(f"Stats fetched: {public_repos} repos, {total_stars} stars, {total_forks} forks.")
            return {
                "repos": public_repos,
                "stars": total_stars,
                "forks": total_forks,
                "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
    except Exception as e:
        print(f"Error fetching stats: {e}")
    return None

if __name__ == "__main__":
    stats = fetch_user_summary()
    print("Automated health check finished.")
