import json
import requests
import argparse
import os

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments

parser.add_argument('--repo_slug', type= str)
parser.add_argument('--head_branch', type= str)
parser.add_argument('--base_branch', type= str)
parser.add_argument('--auth_token', type= str)


args = parser.parse_args()

#example_to_env_vars = os.environ("NAME_OF_VAR")

REPO_SLUG = args.repo_slug
SOURCE_BRANCH = args.head_branch
TARGET_BRANCH = args.base_branch
AUTH_TOKEN = args.auth_token

def createPullRequest(url):

    params = {
        "title": f"Pull request from {SOURCE_BRANCH} to {TARGET_BRANCH}",
        "head": SOURCE_BRANCH,
        "base": TARGET_BRANCH
    }

    response = requests.request(
        "POST",
        url=url,
        headers=headers,
        data=json.dumps(params)
    )


    if response.status_code==201:
        print("PR created successfully.")

        pr_number = response.json()["number"]

        # print(json.dumps(response.json(),indent=4))
        # print("source:",SOURCE_BRANCH)
        # print("target:",TARGET_BRANCH)

    else:
        raise(Exception(response.text))


api_url = f"https://api.github.com/repos/{REPO_SLUG}/"

#api_action = "commits"

api_action = "pulls"

query = f"?q=is:pr+state:open+head:{SOURCE_BRANCH}+base:{TARGET_BRANCH}"

url = api_url + api_action + query

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {AUTH_TOKEN}"
    }

response_get = requests.request(
    "GET",
    url=url,
    headers=headers
)


if response_get.status_code==200:
    jsonvar = response_get.json()
    if len(jsonvar)==0:
        createPullRequest(api_url+api_action)

    else:   
        pr_number = response_get.json()[0]["number"]
        print(f"PR from {SOURCE_BRANCH} to {TARGET_BRANCH} already exists with #{pr_number}.")

    env_file = os.getenv('GITHUB_ENV') # Get the path of the runner file
    # write to the file
    with open(env_file, "a") as env_file:
        env_file.write(f"PR_NUMBER={str(pr_number)}")
else:
    raise(Exception(response_get.text))

