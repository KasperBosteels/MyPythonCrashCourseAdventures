import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

repo_dict = repo_dicts[0]
print("Selected information about the first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Starts: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")