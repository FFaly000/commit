import os

commit = 1000
y = "y"

i = 0
while True:
    for _ in range(commit):
        os.system(f'git commit --allow-empty -m "Commit {i+1} of {commit}"')
        i += 1

    print(f"Committed {commit} times. Total commits: {i}")

    if y == "y":
        os.system('git push')
