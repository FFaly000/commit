import subprocess

c = 100000000000000000  # Total commits
b = 10000               # Commits per batch
push_interval = 100000  # Push every 100,000 commits

# Use well-known empty tree hash (valid for all Git versions)
empty_tree = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

# Disable Git auto garbage collection
subprocess.run(['git', 'config', 'gc.auto', '0'], check=True)

current = 0
while current < c:
    end = min(current + b, c)
    print(f"Creating commits {current+1} to {end}")
    
    # Generate commits using plumbing commands
    subprocess.run([
        'sh', '-c',
        f'''
        parent=$(git rev-parse HEAD)
        for i in $(seq {current+1} {end}); do
            parent=$(git commit-tree -m "Commit $i of {c}" {empty_tree} -p "$parent")
        done
        git reset --hard "$parent"
        '''
    ], check=True)
    
    current = end
    
    # Push at intervals
    if current % push_interval == 0:
        subprocess.run(['git', 'push'], check=True)
        print(f"Pushed up to commit {current}")

# Final push
subprocess.run(['git', 'push'], check=True)
print("All commits pushed successfully")