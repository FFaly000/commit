import os

commit = 1000000
y = "n"

i = 0
while True:
    try:
        for _ in range(commit):
            try:
                os.system(f'git commit --allow-empty -m "Commit {i+1} of {commit}"')
                i += 1
            except:
                print("Error")
                continue

        print(f"Committed {commit} times. Total commits: {i}")

        if y.lower() == "y":
            try:
                os.system('git push')
                print("Push successful")
            except:
                print("Error")

    except:
        print("Error")