import subprocess
from multiprocessing import Process, Lock, Value

c = 100000000000000000
b = 69696969969696969420
n = 6

def w(t, b):
    baia = 0
    while t < c:
        s = t + 1
        e = min(s + b - 1, c)
        t += (e - s + 1)
        try:
            for i in range(s, e + 1):
                subprocess.run(['git', 'commit', '--allow-empty', '-m', f"Commit {i} of {c}"], check=True)
            baia += (e - s + 1)
            if baia % 1000 == 0:
                subprocess.run(['git', 'push'], check=True)
                print(f"PUSHED on commit {baia}")
            print(f"ON {baia} Total: {t}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            subprocess.run(['rm', '-f', '.git/index.lock'], check=True)
            print("Removed .git/index.lock due to error.")
            continue

if __name__ == "__main__":
    w(0, b)
    print("Done")
