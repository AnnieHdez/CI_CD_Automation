import json
import requests
import argparse
import os

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments

parser.add_argument('--repo_slug', type= str)
parser.add_argument('--head_branch', type= str)
parser.add_argument('--auth_token', type= str)


args = parser.parse_args()

#example_to_env_vars = os.environ("NAME_OF_VAR")

REPO_SLUG = args.repo_slug
SOURCE_BRANCH = args.head_branch
AUTH_TOKEN = args.auth_token

print(REPO_SLUG)

api_url = f"https://api.github.com/repos/{REPO_SLUG}/"

api_action = "commits"

url = api_url + api_action


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {AUTH_TOKEN}"
    }

response = requests.get(
    url=url,
    headers=headers
)

if response.status_code==200:
    print(json.dumps(response.json(),indent=4))

print("response:", response.status_code)