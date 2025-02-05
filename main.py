import subprocess
import os

# Constants
TOTAL_COMMITS = 1000  # Adjust as needed
BATCH_SIZE = 100      # Number of commits before pushing

def batch_commit(start, batch_size, total_commits):
    """
    Creates a batch of empty commits using a single Git process.
    """
    commit_messages = "\n".join(
        [f"Commit {start + i} of {total_commits}" for i in range(1, batch_size + 1)]
    )

    commit_command = [
        "git",
        "commit",
        "--allow-empty",
        "--file=-"  # Read commit messages from stdin
    ]

    try:
        subprocess.run(commit_command, input=commit_messages, text=True, check=True)
        print(f"Created commits {start + 1} to {start + batch_size}")

    except subprocess.CalledProcessError as e:
        print(f"Error creating commits: {e}")

def main():
    """
    Creates multiple commits efficiently and pushes them in batches.
    """
    current_commit = 0
    while current_commit < TOTAL_COMMITS:
        commits_this_batch = min(BATCH_SIZE, TOTAL_COMMITS - current_commit)
        batch_commit(current_commit, commits_this_batch, TOTAL_COMMITS)
        current_commit += commits_this_batch

        # Push every BATCH_SIZE commits
        subprocess.run(["git", "push"], check=True)
        print(f"Pushed commits up to {current_commit}")

    print("All commits created and pushed.")

if __name__ == "__main__":
    main()
