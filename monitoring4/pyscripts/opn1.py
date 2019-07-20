import subprocess
import sys

#subprocess.Popen(r'/usr/bin/gnome-terminal')
#subprocess.call(["ls", "-l"])
#subprocess.call(["ls"])
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
result.stdout

#print (sys.argv)

