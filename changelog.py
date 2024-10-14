import os
import subprocess

# Define the directory to look for changes (e.g., aces.vromfs.bin_u)
TARGET_DIR = "aces.vromfs.bin_u"
CHANGELOG_FILE = "CHANGELOG.md"

def get_git_log():
    """
    Get the list of past commits affecting the specified directory.
    """
    log_cmd = f"git log --pretty=format:'%h - %s (%ad) by %an' --date=short -- {TARGET_DIR}"
    result = subprocess.run(log_cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_git_diff(commit_hash):
    """
    Get the diff for a given commit hash affecting the specified directory.
    """
    diff_cmd = f"git diff {commit_hash}~1 {commit_hash} -- {TARGET_DIR}"
    result = subprocess.run(diff_cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def write_changelog():
    """
    Write the changelog based on the git log and diff of past commits.
    """
    # Step 1: Get the past commit logs
    commit_log = get_git_log()
    if not commit_log:
        print(f"No commits found affecting {TARGET_DIR}.")
        return

    # Step 2: Write to the CHANGELOG.md file
    with open(CHANGELOG_FILE, "w") as changelog:
        changelog.write(f"### Full Changelog for `{TARGET_DIR}`\n\n")

        # Step 3: For each commit, append the changes to the changelog
        for line in commit_log.splitlines():
            commit_hash = line.split(" - ")[0]
            changelog.write(f"#### {line}\n")

            # Get the diff for each commit and append it
            diff_output = get_git_diff(commit_hash)
            if diff_output:
                changelog.write("```\n")
                changelog.write(diff_output)
                changelog.write("\n```\n\n")

    print(f"Changelog has been written to {CHANGELOG_FILE}.")

if __name__ == "__main__":
    if not os.path.exists(".git"):
        print("This script must be run inside a Git repository.")
    else:
        write_changelog()
