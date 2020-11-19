# gitlog
Utility to generate JSON representing the git history for the current branch of a local git repo.

## Usage
`gitlog.py <log_limit> <project_path> <log_included_paths...>`

1. log_limit - limits the number of lines the log output gives
2. project_path - project directory to examine
3. log_included_paths - includes only commits that are able to explain how these file paths came to be

* Examples:
  * `.\gitlog.py 30 dotnet\runtime\`
  * `.\gitlog.py 100 dotnet\runtime\ ./*`

## Output

```
[
    {
        "commit_hash": "960cef99cf4a33719c300992c33f0a11a5cd0458",
        "commit_author_name": "jteer",
        "commit_author_email": "jteer",
        "commit_date": "Thu, 19 Nov 2020 13:29:47 -0600",
        "commit_messages": [
            "Fix output propert name. Fix error that added the commit marker to the parsing buffer. Fix log file marker."
        ],
        "commit_files": [
            "M\tgitlog.py"
        ],
        "commit_files_renamed": [],
        "commit_files_modified": [
            "gitlog.py"
        ],
        "commit_files_deleted": [],
        "commit_files_added": []
    },
    {
        "commit_hash": "82890b6590b6cf47df985baefa878ed451bc0815",
        "commit_author_name": "jteer",
        "commit_author_email": "jteer",
        "commit_date": "Thu, 19 Nov 2020 13:01:18 -0600",
        "commit_messages": [
            "Update Readme. Update to return json."
        ],
        "commit_files": [
            "M\tREADME.md",
            "M\tgitlog.py"
        ],
        "commit_files_renamed": [],
        "commit_files_modified": [
            "README.md",
            "gitlog.py"
        ],
        "commit_files_deleted": [],
        "commit_files_added": []
    },
    {
        "commit_hash": "21245e824dd0d6f446d7d152da17c7f25e001ec0",
        "commit_author_name": "jteer",
        "commit_author_email": "jteer",
        "commit_date": "Thu, 19 Nov 2020 12:51:39 -0600",
        "commit_messages": [
            "Rename to gitlog"
        ],
        "commit_files": [
            "R084\tgitlog-json.py\tgitlog.py"
        ],
        "commit_files_renamed": [
            {
                "rename_score": "084",
                "old": "gitlog-json.py",
                "new": "gitlog.py"
            }
        ],
        "commit_files_modified": [],
        "commit_files_deleted": [],
        "commit_files_added": []
    }
]
```