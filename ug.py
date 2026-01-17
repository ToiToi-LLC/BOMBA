import subprocess
for x in range(0, 100000):
    print(x)
    proc = subprocess.Popen(['cmd.exe', '/K', 'python', '-i', 'myscript.py'])
