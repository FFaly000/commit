import pygit2
import os

# Open the repository at the current directory.
# Change this if your repository is located elsewhere.
repo_path = os.getcwd()
repo = pygit2.Repository(repo_path)

# Define a signature for the commits.
signature = pygit2.Signature("Your Name", "your.email@example.com")

# Retrieve the current HEAD commit.
try:
    parent = repo.head.target
except KeyError:
    raise Exception("Repository has no commits. Please initialize with an initial commit.")

# Total number of commits to create (for testing, use a small number)
TOTAL_COMMITS = 1000  # Adjust as needed (the original constant is huge)
BATCH_SIZE = 100  # Number of commits to create per batch


def create_commits_in_batch(start_count, batch_size, parent, repo, signature):
    """
    Create a batch of commits in a loop.

    Each commit is created by reusing the tree of the parent commit,
    resulting in an 'empty' commit (i.e. no file changes).
    """
    for i in range(batch_size):
        commit_number = start_count + i + 1
        commit_message = f"Commit {commit_number} of {TOTAL_COMMITS}"
        # Reuse the parent's tree. For a real commit, you would update the index.
        tree = repo[parent].tree

        # Create the new commit. The commit is written to HEAD.
        parent = repo.create_commit(
            'HEAD',  # Update HEAD reference
            signature,  # Author
            signature,  # Committer
            commit_message,  # Commit message
            tree,  # Tree (unchanged)
            [parent]  # Parent commit(s)
        )

        if commit_number % 100 == 0:
            print(f"Created commit {commit_number}")
    return parent


# Main loop: Create commits in batches.
current_count = 0
while current_count < TOTAL_COMMITS:
    commits_this_batch = min(BATCH_SIZE, TOTAL_COMMITS - current_count)
    parent = create_commits_in_batch(current_count, commits_this_batch, parent, repo, signature)
    current_count += commits_this_batch
    # Optionally, perform additional operations such as pushing.
    # For example, you might use pygit2's remote.push() here.
    print(f"Batch complete: Total commits so far: {current_count}")

print("All commits created.")
