import requests

username = "phkhanhtrinh23"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
repos = response.json()

total_forks = sum(repo['forks_count'] for repo in repos)

print(f"Total Forks: {total_forks}")

insert_str = f"\n![Total forks](https://img.shields.io/badge/Total%20forks-{total_forks}-brightgreen)\n"
original_file = open("README.md", "r").readlines()
for idx, line in enumerate(original_file):
    if line.startswith("<img src="):
        break
original_file = original_file[:idx+1] + [insert_str] + original_file[idx+1:]
original_file = "".join(original_file)

with open("README.md", "w") as f:
    f.writelines(original_file)