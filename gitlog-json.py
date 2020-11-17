import sys
import subprocess
import os
import json
import re

Log_Commit_Marker = 'PARSEDGITCOMMIT'
Log_Message_Marker = 'PARSEDGITMESSAGE'
Log_File_Marker = 'PARSEDGITMESSAGE'


def parse_git_log(log_output):
    if not log_output:
        return
    parsed_commits = []
    buffer = []
    for line in log_output:
        if line == Log_Commit_Marker and buffer:
            commit = parse_commit(buffer)
            parsed_commits.append(commit)
            buffer.clear()
        else:
            buffer.append(line)
    if buffer:
        parsed_commits.append(parse_commit(buffer))
    return parsed_commits


def parse_commit(buffer):
    commit = {
        'commit_hash': buffer[0],
        'commit_author_name': buffer[1],
        'commit_author_email': buffer[2],
        'commit_data': buffer[3],
    }

    message_index = buffer.index(Log_Message_Marker)
    files_index = buffer.index(Log_File_Marker)
    commit_files = buffer[files_index+1:]
    commit['commit_messages'] = buffer[message_index + 1:files_index]
    commit['commit_files'] = commit_files

    
    renamed_file_regex = r"^R([0-9]+)\s(.+)\s(.+)"
    modified_file_regex = r"(^M\s)([^\s]+)"
    deleted_file_regex = r"(^D\s)([^\s]+)"
    added_file_regex = r"(^A\s)([^\s]+)"
    def parse_file_changes(file_list, change_pattern):
        return [g[2] for i in file_list if (g := re.match(change_pattern, i))]

    commit['commit_files_renamed'] = [{'rename_score': g[1], 'old':g[2], 'new':g[3]}
                                      for line in commit_files if (g := re.match(renamed_file_regex, line))]
    commit['commit_files_modified'] = parse_file_changes(
        commit_files, modified_file_regex)
    commit['commit_files_deleted'] = parse_file_changes(
        commit_files, deleted_file_regex)
    commit['commit_files_added'] = parse_file_changes(
        commit_files, added_file_regex)

    return commit


if __name__ == "__main__":
    # py .\main.py 30 <project_path>
    args = sys.argv
    log_limit = args[1]
    project_path = args[2]
    git_log_paths = args[3:]

    # https://git-scm.com/docs/pretty-formats
    git_log_format = f'{Log_Commit_Marker}%n%H%n%an%n%ae%n%aD%n{Log_Message_Marker}%n%B%n{Log_File_Marker}'
    git_log_command = ['git', 'log', '--pretty=oneline', '--name-status',
                       f'-{log_limit}', f'--pretty=format:{git_log_format}']
    if git_log_paths:
        git_log_command.extend(['--'] + git_log_paths)

    command_output = subprocess.run(
        git_log_command, stdout=subprocess.PIPE, cwd=project_path, encoding=sys.getdefaultencoding())
    command_output.check_returncode()
    logoutput = command_output.stdout
    logoutput_by_line = list(filter(None, logoutput.splitlines()))
    git_log = parse_git_log(logoutput_by_line)
    git_log_json = json.dumps(git_log, sort_keys=False, indent=4)
    print(git_log_json)
