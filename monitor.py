import subprocess
import time

repos_info = [
    {
        'path': './thefuck', 
        'branch': 'master', 
        'url': 'https://github.com/nvbn/thefuck'
    },
    {
        'path': './kubernetes', 
        'branch': 'master',
        'url': 'https://github.com/kubernetes/kubernetes'
    }
]

def monitor_repo(repo_info):
    repo_path = repo_info['path']
    branch_name = repo_info['branch']
    repo_url = repo_info['url']

    subprocess.run(['git', 'fetch'], cwd=repo_path)

    result_commits = subprocess.run(['git', 'rev-list', '--count', f'HEAD..origin/{branch_name}'], cwd=repo_path, capture_output=True, text=True)
    try:
        diff = int(result_commits.stdout.strip())
        if diff:
            print(f"Repo {repo_path} (URL: {repo_url}) is behind by {diff} commits.")
        else:
            print(f"Repo {repo_path} (URL: {repo_url}) is up-to-date.")
    except ValueError:
        print(f"Couldn't parse the number of commits behind for repo {repo_path}.")

    result_files = subprocess.run(['git', 'diff', 'HEAD', f'origin/{branch_name}', '--name-only'], cwd=repo_path, capture_output=True, text=True)
    files = result_files.stdout.splitlines()
    if files:
        print(f"Files changed in repo {repo_path}:")
        for file in files:
            print(file)

while True:
    for repo_info in repos_info:
        monitor_repo(repo_info)
    time.sleep(60*15)
