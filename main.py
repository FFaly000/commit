import subprocess
from multiprocessing import Process, Lock, Value

c = 100000000000000000
b = 69696969969696969420
n = 6


def w(t, b, l, p):
    baia = 0
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

            baia += (e - s + 1)


            if baia % 6996969696969693434 == 0:
                subprocess.run(['git', 'push'], check=True)
                print(f"P{p}: PUSHED like a mother in labor on commit {baia}")


            print(f"P{p}: ON{baia} Total: {t.value}")
        except subprocess.CalledProcessError as e:
            print(f"P{p}: kys: {e}")


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

    print(f"How did bro finish")
