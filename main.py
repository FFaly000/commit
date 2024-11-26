import subprocess

commit = 1000000
batch_size = 1000 
y = "n"

i = 0
while i < commit:
    try:
        for _ in range(batch_size):
            subprocess.run(['git', 'commit', '--allow-empty', '-m', f"Commit {i+1} of {commit}"], check=True)
            i += 1

        print(f"Committed {batch_size} times. Total commits: {i}")

        if y.lower() == "y":
            subprocess.run(['git', 'push'], check=True)
            print("Push successful")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
