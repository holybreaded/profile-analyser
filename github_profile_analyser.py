import requests
import sys

def get_github_profile(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_profile_summary(profile):
    if profile:
        print(f"Name: {profile['name']}")
        print(f"Username: {profile['login']}")
        print(f"Bio: {profile['bio']}")
        print(f"Repositories: {profile['public_repos']}")
        print(f"Followers: {profile['followers']}")
        print(f"Following: {profile['following']}")
    else:
        print("User not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_profile_analyzer.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    profile = get_github_profile(username)
    display_profile_summary(profile)
