
# `monitoring_tools`

## Overview
The script provides real-time monitoring of multiple git repositories to track changes. By comparing local versions to their remote counterparts, the script can indicate if a local repo is current or if it's lagging behind.

## Repositories Monitored:
- [thefuck](https://github.com/nvbn/thefuck)
- [kubernetes](https://github.com/kubernetes/kubernetes)

## Features

### 1. Repository Information
The `repos_info` list holds the details of all repositories under surveillance. Every entry has:
- `path`: Local directory of the repository.
- `branch`: The targeted branch for monitoring.
- `url`: Direct URL to the GitHub repository.

### 2. Monitoring Function (`monitor_repo`)

For each repository mentioned in repos_info, the script:
- Retrieves the latest updates using git fetch.
- Determines how many commits the local repository is behind the remote one.
- Identifies any files that differ between the local and remote repositories.
- The status of each repository, including its URL, is displayed in the console.

### 3.Continuous Monitoring:

The script persistently monitors the repositories. After inspecting all repositories,
 it pauses for 15 min before the next cycle.



## Output
Expect outputs such as:
- `"Repo ./path_to_repo (URL: https://github.com/user/repo_name) is up-to-date."` when congruence is found between local and remote repositories.
- `"Repo ./path_to_repo (URL: https://github.com/user/repo_name) is behind by X commits."` indicating the local repo needs updating.
- A Lists of changed files if there are discrepancies between local and remote versions.
