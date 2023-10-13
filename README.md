### monitoring_tools
## Overview:
The script monitors multiple git repositories for changes. It fetches the latest updates from the remote repositories and compares them with the local version to inform you if your local repo is up-to-date or behind the remote repo.

# The two repositories used for monitoring are:

Marked.js Repository
Advent of Code 2019

## How It Works:
# Repository Information:

Repositories are detailed in the repos_info list. Each entry in the list contains:
path: The local path to the repository.
branch: The branch to monitor.
url: The URL to the GitHub repository for quick access and reference.


## Monitoring Function - monitor_repo:

For each repository mentioned in repos_info, the script:
Retrieves the latest updates using git fetch.
Determines how many commits the local repository is behind the remote one.
Identifies any files that differ between the local and remote repositories.
The status of each repository, including its URL, is displayed in the console.
Continuous Monitoring:

The script persistently monitors the repositories. After inspecting all repositories,
 it pauses for 60 seconds before the next cycle.

## Output:
Expect outputs such as:

"Repo ./path_to_repo (URL: https://github.com/user/repo_name) is up-to-date." when there are no changes.
"Repo ./path_to_repo (URL: https://github.com/user/repo_name) is behind by X commits." if the local repo lags.
Lists of changed files if there are discrepancies between local and remote versions.
