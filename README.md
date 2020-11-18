# gitlog-json
Utility to generate JSON representing the git history for the current branch of a local git repo.

## Usage
`gitlog-json.py <log_limit> <project_path> <log_included_paths...>`

1. log_limit - limits the number of lines the log output gives
2. project_path - project directory to examine
3. log_included_paths - includes only commits that are able to explain how these file paths came to be

* Examples:
  * `.\gitlog-json.py 30 dotnet\runtime\`
  * `.\gitlog-json.py 100 dotnet\runtime\ ./*`