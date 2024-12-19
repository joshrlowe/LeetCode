import subprocess


def commit(directory, commit_message, readme="README.md"):
    print("Committing to Git...")
    subprocess.run(["git", "add", readme, directory])
    subprocess.run(["git", "commit", "-m", commit_message])
    print("Changes committed successfully!")


def push(remote="origin", branch="main"):
    print("Pushing to Git...")
    subprocess.run(["git", "push", "-u", remote, branch])
    print("Changes pushed successfully!")
