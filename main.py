import os

commitCount = 1000
autoPush = "y"

i = 0
while True:
    for _ in range(commitCount):
        os.system(f'git commit --allow-empty -m "Commit {i+1} of {commitCount}"')
        i += 1

    print(f"Committed {commitCount} times. Total commits: {i}")

    if autoPush == "y":
        os.system('git push')
