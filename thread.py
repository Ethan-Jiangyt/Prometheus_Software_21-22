import subprocess

process1 = subprocess.Popen(["python3", "graph.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python3", "graph2.py"])
process3 = subprocess.Popen(["python3", "graph3.py"])
process3 = subprocess.Popen(["python3", "graph4.py"])

# process1.wait() # Wait for process1 to finish (basically wait for script to finish)
# process2.wait()
# process3.wait()
# process4.wait()