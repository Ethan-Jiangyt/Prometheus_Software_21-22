import subprocess

python = 'python'

process1 = subprocess.Popen([python, "write_csv.py"])
process2 = subprocess.Popen([python, "graph.py"])