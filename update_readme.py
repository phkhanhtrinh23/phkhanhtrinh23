import requests

username = "phkhanhtrinh23"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
repos = response.json()

total_forks = sum(repo['forks_count'] for repo in repos)

print(f"Total Forks: {total_forks}")

# Save the result in README format
with open("README.md", "w") as f:
    f.write(f"![Total Forks](https://img.shields.io/badge/Total%20Forks-{total_forks}-brightgreen)\n")
