import subprocess
import time
import os

c = 100000000000000000
b = 69696969969696969420
n = 6
LOCK_FILE = '.git/index.lock'

def is_lock_file_present():
    return os.path.exists(LOCK_FILE)

def remove_lock_file():
    try:
        os.remove(LOCK_FILE)
        print("Removed .git/index.lock due to error.")
    except Exception as e:
        print(f"Failed to remove lock file: {e}")

def commit_with_retry(i, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            subprocess.run(['git', 'commit', '--allow-empty', '-m', f"Commit {i} of {c}"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error during commit {i}: {e}")
            if is_lock_file_present():
                print(f"Lock file detected. Waiting to retry commit {i}...")
                time.sleep(1)  # Sleep for a while before retrying
                retries += 1
            else:
                print(f"Unexpected error during commit {i}, not lock-related.")
                break
    return False

def w(t, b):
    baia = 0
    while t < c:
        s = t + 1
        e = min(s + b - 1, c)
        t += (e - s + 1)
        try:
            for i in range(s, e + 1):
                if commit_with_retry(i):
                    baia += 1
                else:
                    print(f"Failed to commit {i} after retries, skipping...")
                    continue

            if baia % 1000 == 0:
                subprocess.run(['git', 'push'], check=True)
                print(f"PUSHED on commit {baia}")
            print(f"ON {baia} Total: {t}")
        except subprocess.CalledProcessError as e:
            print(f"Error in commit loop: {e}")
            remove_lock_file()  # Remove lock file if something goes wrong
            continue

if __name__ == "__main__":
    w(0, b)
    print("Done")
