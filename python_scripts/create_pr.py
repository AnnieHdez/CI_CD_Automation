import json
import requests
import argparse

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('--head_branch', type= str)


args = parser.parse_args()

SOURCE_BRANCH = args.head_branch

print(SOURCE_BRANCH)