import subprocess
from multiprocessing import Process, Lock, Value

c = 1000000
b = 1000
n = 6

def w(t, b, l, p):
    while True:
        with l:
            if t.value >= c:
                break
            s = t.value + 1
            e = min(s + b - 1, c)
            t.value += (e - s + 1)

        try:
            for i in range(s, e + 1):
                subprocess.run(['git', 'commit', '--allow-empty', '-m', f"Commit {i} of {c}"], check=True)
            print(f"P{p}: Committed {e - s + 1} commits. Total commits: {t.value}")
        except subprocess.CalledProcessError as e:
            print(f"P{p}: Error: {e}")

if __name__ == "__main__":
    l = Lock()
    t = Value('i', 0)

    ps = []
    for i in range(n):
        p = Process(target=w, args=(t, b, l, i))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()

    print(f"All commits completed. Total commits: {t.value}")
