import os
import threading

commit = 1000000
y = "n"

i = 0
lock = threading.Lock()

def commit_task(start, end):
    global i
    for j in range(start, end):
        try:
            os.system(f'git commit --allow-empty -m "Commit {j+1} of {commit}"')
            with lock:
                i += 1
        except Exception as e:
            continue

def create_threads():
    num_threads = 6
    commits_per_thread = commit // num_threads

    threads = []
    for t in range(num_threads):
        start = t * commits_per_thread
        end = (t + 1) * commits_per_thread if t != num_threads - 1 else commit
        thread = threading.Thread(target=commit_task, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Committed {commit} times. Total commits: {i}")

    if y.lower() == "y":
        try:
            os.system('git push')
            print("Push successful")
        except Exception as e:
            print(f"Error during push: {e}")

if __name__ == "__main__":
    create_threads()
