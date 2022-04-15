import subprocess
import time
# Change to python or python3 if u need to
python = 'python'

# process0 = subprocess.Popen([python], "read_serial.py")
process1 = subprocess.Popen([python, "test_csv.py"]) # Create and launch process pop.py using python interpreter
time.sleep(1)
process2 = subprocess.Popen([python, "pt_graph.py"])
process3 = subprocess.Popen([python, "loadcell_graph.py"])
process3 = subprocess.Popen([python, "tc_graph.py"])

# process1.wait() # Wait for process1 to finish (basically wait for script to finish)
# process2.wait()
# process3.wait()
# process4.wait()